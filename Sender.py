import smtplib
from email.mime.text import MIMEText
import config
server=smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

EMAIL=config.EMAIL
PASSWORD=config.PASSWORD
server.login(EMAIL,PASSWORD)

message=MIMEText("Sent from python code")
message["From"]=EMAIL
message["To"]=EMAIL
message["Subject"]="Auto Email Sender using the SMTP protocol from python"


server.sendmail(EMAIL,EMAIL,message.as_string())

print("Mail sent successfully")