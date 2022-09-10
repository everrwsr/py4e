import datetime
import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText
import requests
from lxml import etree

# me


def GetRep():
    # 获取通知
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"
    }
    xaufe_url = "http://www.xaufe.edu.cn/xxgg1.htm"
    response = requests.get(xaufe_url, headers=headers)
    response.encoding = "utf-8"
    rep = response.text
    html = etree.HTML(rep)
    xaufe_title = html.xpath("//body//ul//li/a//@title")[20:-1]
    xaufe_url = html.xpath("//body//ul//li/a//@href")[21:-1]
    # print(xaufe_title)
    # print(xaufe_url)
    xaufe_url_1 = ["http://www.xaufe.edu.cn/" + str(i) for i in xaufe_url]
    xaufe_message = []
    for i in range(0, len(xaufe_title)):
        xaufe_message.append(
            "    \n     "+xaufe_title[i]+"   \n   "+xaufe_url_1[i]+"     ")
    xaufe_message = " \n  ".join(xaufe_message)
    print(xaufe_message)
    return xaufe_message


def send_email():
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "1943608139@qq.com"  # 用户名
    mail_pass = "lrxuqnddtqnmcgci"  # 获取授权码
    sender = '1943608139@qq.com'  # 发件人账号
    receivers = ['1943608139@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    send_content = 'xaufe_notice'
    list = GetRep()
    message = MIMEText(list, 'plain', 'utf-8')  # 第一个参数为邮件内容,第二个设置文本格式，第三个设置编码
    message['From'] = Header("me", 'utf-8')  # 发件人
    message['To'] = Header("me", 'utf-8')  # 收件人
    subject = 'xaufe通知啦'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


def update():
    print('通知系统启动中')
    old_pattern = GetRep()  # 记录原始内容列表
    while True:
        new_pattern = GetRep()  # 记录新内容列表
        if (new_pattern != old_pattern):  # 判断内容列表是否更新
            old_pattern = new_pattern
            print(new_pattern)  # 原始内容列表改变
            send_email()  # 发送邮件
        else:
            now = datetime.datetime.now()
            print(now, "尚无更新")
        time.sleep(300)  # 五分钟检测一次message.as_string())
    # print('通知系统启动中')
    # new_pattern = GetRep()  # 记录新内容列表
    # infile = open("tongzhi.txt", 'r')
    # old_pattern = infile.read()
    # infile.close()
    # CunChuwenjian = open("tongzhi.txt", 'w')
    # CunChuwenjian.write(new_pattern)
    # CunChuwenjian.close()
    # if new_pattern == old_pattern:
    #     print("暂无更新")
    # else:
    #     send_email()

    # while True:
    #     new_pattern = GetRep()  # 记录新内容列表
    #     if (new_pattern != old_pattern):  # 判断内容列表是否更新
    #         old_pattern = new_pattern
    #         print(new_pattern)  # 原始内容列表改变
    #         # send_email()  # 发送邮件
    #     else:
    #         now = datetime.datetime.now()
    #         print(now, "尚无更新")
    #     time.sleep(300)  # 五分钟检测一次message.as_string())

    # 一个很简单的代码我却写了很久，坦白讲没什么成就感，只是有一种释然感，跨年夜头疼欲裂 你让我好沮丧
    # 2022.3.18   大幅改写后发现在2022跨年夜写下的东西。还是很难介怀
    # 2022.5.5    又是一次争吵，或许在此刻结束是比较好的一个选择。
    # 2022.5.8    今日无事 每个人或许都有自己的轨迹 在自己想要的道路上前进也不错
    # 2022.09.8 重启此项目，诸事不顺，大三了，彷徨。
    
if __name__ == "__main__":
    update()
