import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class Email:

    def __init__(self, login, password, header=None, smtp='smtp.gmail.com', imap='imap.gmail.com'):
        self.login = login
        self.password = password
        self.header = header
        self.smtp = smtp
        self.imap = imap

    def create_message(self, subject, recipients, message_text):
        message = MIMEMultipart()
        message['From'] = self.login
        message['To'] = ', '.join(recipients)
        message['Subject'] = subject
        message.attach(MIMEText(message_text))
        return message

    def send_message(self, message):
        ms = smtplib.SMTP(self.smtp, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, message.as_string())
        ms.quit()

    def receive_message(self):
        mail = imaplib.IMAP4_SSL(self.imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select('inbox')
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        return email_message


if __name__ == '__main__':
    email_account = Email('login@gmail.com', 'qwerty')
    outgoing_message = email_account.create_message('Subject', ['vasya@email.com', 'petya@email.com'], 'Message')
    email_account.send_message(outgoing_message)
    incoming_message = email_account.receive_message()
