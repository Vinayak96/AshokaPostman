import imaplib
import email
from email.header import Header, decode_header, make_header
name,email_addr,email_subject,email_body

def FetchMail():
    HOST = 'imap.gmail.com'
    USERNAME = 'ashokapostman@gmail.com'
    PASSWORD = 'DIBYENDU1997'
    m = imaplib.IMAP4_SSL(HOST, 993)
    m.login(USERNAME, PASSWORD)
    m.select('INBOX')
    global
    result, data = m.uid('search', None, "UNSEEN")
    if result == 'OK':
        for num in data[0].split()[:5]:
            result, data = m.uid('fetch', num, '(RFC822)')
            if result == 'OK':
                # Get raw message
                email_message_raw = email.message_from_bytes(data[0][1])

                # Decode headers
                email_from = str(make_header(decode_header(email_message_raw['From'])))
                email_subject = str(make_header(decode_header(email_message_raw['Subject'])))


                # Print each name and email and body
                name, email_addr = email_from.split('<')
                email_addr.replace(">", "")
                for part in email_message_raw.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True)
                        email_body=body.decode('utf-8')
                    else:
                        continue

                return(name,email_addr,email_subject,email_body)

    m.close()
    m.logout()
    print(name,email_addr)

import smtplib

def send_email(user, pwd, recipient, subject, body):


    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")

'''
FROM=''
TO=''
message=''

server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server_ssl.ehlo() # optional, called by login()
server_ssl.login('ashokapostman@gmail.com','DIBYENDU1997')  
# ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
server_ssl.sendmail(FROM, TO, message)
#server_ssl.quit()
server_ssl.close()
print('successfully sent the mail')'''