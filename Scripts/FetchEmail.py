import imaplib
import email
from email.header import Header, decode_header, make_header

def FetchMail():
    HOST = 'imap.gmail.com'
    USERNAME = 'ashokapostman@gmail.com'
    PASSWORD = 'DIBYENDU1997'
    m = imaplib.IMAP4_SSL(HOST, 993)
    m.login(USERNAME, PASSWORD)
    m.select('INBOX')

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

