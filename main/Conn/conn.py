import socket
from .. import setting

class client():
    def __init__(self):
        self.clt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(">创建客户端连接初始化")
    def sendMsg(self, data):
        print(">发送信息模块运行")
        self.clt.send(data.encode('utf-8'))

    def recvMsg(self):
        print(">接受消息模块运行")
        data = self.clt.recv(2048)
        msg= data.decode("utf-8")
        return msg

    def run(self):
        print("尝试连接服务器")
        self.clt.connect((setting.ServerIP, setting.ServePort))
        print("服务器连接成功")
        setting.ConnStat = True

    def close(self):

        self.clt.close()
