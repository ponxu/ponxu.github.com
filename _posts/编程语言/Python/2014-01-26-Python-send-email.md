---
layout: post
title: Python发送邮件
description: Python发送邮件
category: Python
tags: Python
comments: yes
---

{% highlight python %}
#coding: utf-8
import smtplib
from email.mime.text import MIMEText


def send_mail(to, subject, content):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = to
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

    smtp = smtplib.SMTP()
    smtp.connect(SMTP_SERVER, "25")
    smtp.login(SMTP_USER, SMTP_PWD)
    smtp.sendmail(EMAIL_FROM, to.split(';'), msg.as_string())
    smtp.quit()

    print 'sendto', to, subject

send_mail('email1@test.com;email2@test.com', 'hello title', 'just for test!!')

{% endhighlight %}