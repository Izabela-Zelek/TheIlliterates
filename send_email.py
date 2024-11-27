import smtplib
from email.message import EmailMessage

#Set the sender email and password and recipient emaiç
from_email_addr ="theilliteratespi@gmail.com"
from_email_pass ="dlhp fcho dqnm ehds"
to_email_addr ="immatureluna@gmail.com"

# Create a message object
msg = EmailMessage()

# Set the email body
body ="Hello, I am advocating for illiterate people. If you just take a look at this brochure, it says...uhh...so right here it says...ummm...is- is that an L or a Q..."
msg.set_content(body)

# Set sender and recipient
msg['From'] = from_email_addr
msg['To'] = to_email_addr

# Set your email subject
msg['Subject'] = 'Illiterate Lives Matter'

# Connecting to server and sending email
# Edit the following line with your provider's SMTP server details
server = smtplib.SMTP('smtp.gmail.com', 587)

# Comment out the next line if your email provider doesn't use TLS
server.starttls()
# Login to the SMTP server
server.login(from_email_addr, from_email_pass)

# Send the message
server.send_message(msg)

print('Email sent')

#Disconnect from the Server
server.quit()