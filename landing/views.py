from django.shortcuts import render
import imaplib
import email
import sqlite3
import re
from .models import EMAIL

def landing(request):
    mail = imaplib.IMAP4_SSL('imap.yandex.ru')
    mail.login('testMAIL1997@yandex.ru', 'gejpeypqmdxucrtz')

    mail.list()
    mail.select("inbox")

    result, data = mail.search(None, "ALL")

    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]

    result, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')

    email_message = email.message_from_string(raw_email_string)
    sender = email.utils.parseaddr(email_message['From'])
    s = sender[1]

    if email_message.is_multipart():
        for payload in email_message.get_payload():
            body = payload.get_payload(decode=True).decode('utf-8')
            b += re.sub("\r\n", "", body)
    else:
        body = email_message.get_payload(decode=True).decode('utf-8')
        b = re.sub("\r\n", "", body)

    em = EMAIL(email=s, text=b)
    em.save()

    return render(request, 'landing/landing.html', locals())