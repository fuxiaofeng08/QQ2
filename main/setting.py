from queue import Queue
#软件基本配置和公共参数
#服务器地址
ServerIP = '148.70.32.15'
#服务器端口
ServePort = 5555
#客服端
Client = None
#接受服务器消息
ResvMegQ = Queue()
#发送服务器消息
SendMsgQ = Queue()
#登录状体记录
LoadStat = "NOTLOAD"
#服务器连接状态
ConnStat = None
#当前创建窗口
WinDict = {}