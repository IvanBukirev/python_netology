import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MailClient:

    def __init__(self, login, password, smtp_server='smtp.gmail.com', imap_server='imap.gmail.com'):
        self.login = login
        self.password = password
        self.smtp_server = smtp_server
        self.imap_server = imap_server

    def send_message(self, recipients, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        with smtplib.SMTP(self.smtp_server, 587) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.login, self.password)
            server.sendmail(self.login, recipients, msg.as_string())

    def receive_message(self, mailbox='inbox', header=None):
        mail = imaplib.IMAP4_SSL(self.imap_server)
        mail.login(self.login, self.password)
        mail.select(mailbox)

        criterion = f'(HEADER Subject "{header}")' if header else 'ALL'
        _, data = mail.uid('search', None, criterion)

        if not data[0]:
            mail.logout()
            return None

        latest_email_uid = data[0].split()[-1]
        _, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        mail.logout()

        return email_message


if __name__ == '__main__':
    mail_client = MailClient(
            login='login@gmail.com',
            password='pass'
    )

    # Отправка письма
    mail_client.send_message(
            recipients=['test@test.com'],
            subject='Subject',
            message='Message'
    )

    # Получение последнего письма
    received_message = mail_client.receive_message()
    print(received_message)