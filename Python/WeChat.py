import itchat
import time
itchat.auto_login(hotReload=True)
friend_data = itchat.get_friends(update=True)
users = itchat.search_friends(remarkName=u'李花花')
# users = itchat.search_friends(remarkName=u'测试')
userName = users[0]['UserName']
while 1:
    current_time = time.strftime("%Y年%m月%d日%H点%M分%S秒", time.localtime())
    message = '现在是' + current_time + '，请起身眺望远方，舒展身体，下一次提醒将在一小时后送达。'
    itchat.send(message,toUserName=userName)
    time.sleep(3600)

