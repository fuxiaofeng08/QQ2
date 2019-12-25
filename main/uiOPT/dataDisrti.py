import json

from .. import setting
def dataDistri(data):
    data = json.loads(data)
    for key in data:
        info = key
    if info in setting.WinDict:
        setting.WinDict[info].recvMsg(data)
    if info == 'searchFriend':
        setting.WinDict['friends'].displaySearchRst(data)
    if info == 'addFriend':
        setting.WinDict['friends'].addResp(data)
