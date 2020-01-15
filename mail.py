import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

# Email you want to send the update from (only works with gmail)
fromEmail = '123456789@qq.com'
# You can generate an app password here to avoid storing your password in plain text
# https://service.mail.qq.com/cgi-bin/help?subtype=1&no=166&id=28
fromEmailPassword = 'password'

# Email you want to send the update to
toEmail = 'email2@gmail.com'

def sendEmail(image):
	msgRoot = MIMEMultipart('mixed')
    msgRoot['Subject'] = 'Security Update'
    msgRoot['From'] = fromEmail
    msgRoot['To'] = toEmail
	msgRoot.preamble = 'Raspberry pi security camera update'

	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)
	msgText = MIMEText('Smart security cam found object')
	msgAlternative.attach(msgText)

	msgText = MIMEText('<img src="cid:image1">', 'html')
	msgAlternative.attach(msgText)

	msgImage = MIMEImage(image)
	msgImage.add_header('Content-ID', '<image1>')
	msgRoot.attach(msgImage)

	client = smtplib.SMTP_SSL(host = 'smtp.qq.com')
    client.connect('smtp.qq.com')
    client.login(fromEmail, fromEmailPassword)
    #发件人和认证地址必须一致
    client.sendmail(fromEmail, [toEmail], msgRoot.as_string())
    client.quit()