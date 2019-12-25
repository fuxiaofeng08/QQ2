import socket
from threading import Thread, Lock
from pymongo import MongoClient
import json
class QQserver():
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('0.0.0.0', 5555))
        self.server.listen(20)
        self.conn = {}#存储用户连接
        self.onlineUsr = set()
        self.lock = Lock()
        self.dbOpt()
    #数据库连接
    def dbOpt(self):
        try:
            dbclnt = MongoClient('mongodb://127.0.0.1:27017')
            db = dbclnt['QQ']
            self.usrCol = db.userInfo
            print("数据库连接成功")
        except:
            print("数据库连接失败")
    #用户登录
    def login(self, msg, ip):
        usrInfo = msg['LoadInfo']
        usrInfo = json.loads(usrInfo)
        usrName = usrInfo['usrName']
        pwd = usrInfo['pwd']
        usr = self.usrCol.find_one({'usrName':usrName})
        if usr and usr.get('pwd') == pwd:
            usr['ip'] = ip
            usr['state'] = 1
            self.usrCol.update({'usrName':usrName}, usr)
            print("用户", usrName, '登陆成功')
            del usr['_id']
            del usr['pwd']
            del usr['ip']
            self.onlineUsr.add(usrName)
            resp = json.dumps(usr)
            sendMsg = {
                "loadInfo": resp
            }
            return ip, sendMsg
        else:
            return 'NO'
    #用户注册
    def register(self, msg, ip):
        usrData = msg['Register']
        usrInfo = {
            "usrName": usrData['usrName'],
            "pwd": usrData['pwd'],
            'sex': usrData['sex'],
            "autograph": "这个人很懒，什么也没留下！",
            "friends": [],
            "ip": ip
        }
        sendIP = ip
        if self.usrCol.find_one({'usrName': usrData['usrName']}):
            sendMsg = {
                'Register': 'Exist'
            }
        else:
            try:
                self.usrCol.insert_one(usrInfo)
                sendMsg = {
                    'Register': 'OK'
                }
            except:
                sendMsg = {
                    'Register': 'NO'
                }
        return sendIP, sendMsg
    #加载好友列表
    def loadfriends(self, msg, ip):
        sendIP = ip
        usr = self.usrCol.find_one({'ip': list(ip)})
        friends = usr['friends']
        resp = []
        for friend in friends:
            item = {}
            rst = self.usrCol.find_one({'usrName': friend})
            item['usrName'] = friend
            item['autograph'] = rst['autograph']
            item['state'] = 0
            if friend in self.onlineUsr:
                item['state'] = 1
            resp.append(item)
        sendMsg = {'friends': json.dumps(resp)}
        return sendIP, sendMsg
    #添加好友
    def addfriend(self, msg, ip):
        if 'YES' in msg['addFriend']:
            usr = self.usrCol.find_one({'ip': list(ip)})
            lst = usr['friends']
            friend = msg['addFriend'].split('YES')[1]
            lst.append(friend)
            usr['friends'] = list(set(lst))
            self.usrCol.update({'ip': list(ip)}, usr)
            friendItem = self.usrCol.find_one({"usrName": friend})
            lst2 = friendItem['friends']
            lst2.append(usr['usrName'])
            friendItem['friends'] = list(set(lst2))
            self.usrCol.update({"usrName": friend}, friendItem)
            sendIP = tuple(friendItem['ip'])
            sendMsg = {
                'addFriend': 'YES'
            }
            print('添加好友请求处理完毕')
        elif 'NO' in msg['addFriend']:
            item = msg['addFriend'].split('NO')
            usr = self.usrCol.find_one({"usrName": item})
            sendIP = tuple(usr['ip'])
            sendMsg = {
                'addFriend': 'NO'
            }
            print("拒绝添加好友信息发送成功")
        else:
            toUsr = msg['addFriend']
            usr = self.usrCol.find_one({"usrName": toUsr})
            reqUsr = self.usrCol.find_one({'ip': list(ip)})
            sendIP = tuple(usr['ip'])
            sendMsg = {
                'addFriend': reqUsr['usrName']
            }
            print("请求添加好<%s>友信息转发成功" % toUsr)
        return sendIP, sendMsg
    #搜索好友
    def searchfriend(self, msg, ip):
        usrName = msg['searchFriend']
        import re
        print(type(usrName), usrName)
        usrs = self.usrCol.find({"usrName": re.compile(usrName, re.IGNORECASE)})
        Results = []
        for usr in usrs:
            print(usr)
            rst = usr.get('usrName')
            Results.append(rst)
        sendIP = ip
        sendMsg = {
            'searchFriend': Results
        }
        return sendIP, sendMsg
    #消息转发
    def msgforward(self, msg, ip):
        for key in msg:
            toUsrName = key
            tempmsg = msg[key]
        toUsr = self.usrCol.find_one({'usrName': toUsrName})
        sendIP = tuple(toUsr['ip'])
        fromUsr = self.usrCol.find_one({'ip': list(ip)})
        fromUsrName = fromUsr['usrName']
        sendMsg = {
            fromUsrName: tempmsg
        }
        self.lock.acquire()
        if not self.conn.get(sendIP):
            sendIP = ip
            sendMsg = {
                toUsrName: '用户不在线'
            }
        self.lock.release()
        return sendIP, sendMsg
###################消息格式说明#####################
#   msg = {‘flag’:msg}
#   flag == LoadInfo 表示本次请求为登录请求
#   flag == LoadFriends 表示本次请求为获取好友列表请求
#   flag == {Friend} 表示发送消息至Friend
#   flag == {addFriend}表示发送请求添加好友消息
#   flag == {searchFriend}表示请求搜索好友消息
#################################################

    #消息调度
    def msgOpt(self, msg, ip):
        msg = json.loads(msg)
        print('来自<%s>的消息:%s'%(ip, msg))
        #判断是否为登录操作
        if 'LoadInfo' in msg:
            sendIP, sendMsg = self.login(msg, ip)
        #用户注册
        elif 'Register' in msg:
            sendIP, sendMsg = self.register(msg, ip)
        #判断是否为初始化好友列表
        elif 'LoadFriends' in msg:
            sendIP, sendMsg = self.loadfriends(msg, ip)
        #添加好友addFriend
        elif 'addFriend' in msg:
            sendIP, sendMsg = self.addfriend(msg, ip)
        #搜索用户信息
        elif 'searchFriend' in msg:
            sendIP, sendMsg = self.searchfriend(msg, ip)
        else:
            sendIP, sendMsg = self.msgforward(msg, ip)
        self.lock.acquire()
        conn = self.conn.get(sendIP)
        self.lock.release()
        sendMsg = json.dumps(sendMsg)
        print("发送消息<%s>成功"%(sendMsg))
        conn.send(sendMsg.encode('utf-8'))
        print("消息->", ip ,"->处理成功")
    def logout(self, addr):
        usr = self.usrCol.find_one({'ip':list(addr)})
        self.conn.pop(addr)
        if usr and usr['usrName'] in self.onlineUsr:
            self.onlineUsr.remove(usr['usrName'])
            return
        else:
            return
    def threadrun(self, conn, addr):
        print(addr, '用户连接成功')
        self.lock.acquire()
        if not self.conn.get(addr):
            clt = {addr:conn}
            self.conn.update(clt)
        self.lock.release()
        while True:
            try:
                resvmsg = conn.recv(2048).decode("utf-8")
                self.msgOpt(resvmsg, addr)
            except:
                print(addr,'用户断开连接')
                self.logout(addr)
                return
    def run(self):
        while True:
            conn, addr = self.server.accept()
            thread = Thread(target=self.threadrun, args=[conn, addr])
            thread.start()

if __name__ == "__main__":
    server = QQserver()
    server.run()
