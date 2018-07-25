import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender ="liubinghong@dbgo.cn"
receiver ="1207164150@qq.com"
#发送邮件主题
subject = 'Python email test'
#发送邮箱服务器
smtpserver = 'smtp.qiye.163.com'
#发送邮箱用户/密码
username = 'liubinghong@dbgo.cn'
password = 'surui1016...'


#HTML邮件正文
Html_url ="C:\\Users\\Administrator\\.spyder-py3\\Test_object\\report\\20180717-14-58-36.html"
with open(Html_url,'r',encoding='utf-8') as e :
    # with open("C:\\Users\\Administrator\\.spyder-py3\\Test_object\\report\\tes.html",'w+',encoding='utf-8') as d:
    aa = e.readlines()
    Html_msg =''.join(aa)
        # print(bb)
        # d.write(bb)
#编写text 类型的邮件正文
msg = MIMEText(Html_msg,'html','utf-8')
msg['Subject'] = Header(subject, 'utf-8')
smtp = smtplib.SMTP()
try:
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
except Exception as e:
    print(e)
finally:
    smtp.quit()