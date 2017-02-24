import smtplib

fromaddr = 'odane.peck24@gmail.com'

toaddr  = ['odane.peck24@gmail.com']

#message = """From: {} <{odane@gmail.com}>

#To: {To Person} <{odane.com}>

#Subject: {SMTP e-mail test}

#{}"""
message = """Love is beautiful"""
Subject = "To everyone"
messagetosend = message.format(
                             fromaddr,


                             toaddr,


                             message)

# Credentials (if needed)

username = ''

password = ''


# Prepare actual message

message = """\
fromaddr: %s
toaddr: %s
messagetosend: %s
%s
""" % (fromaddr, ", ".join(toaddr), messagetosend, Subject)

# Send the mail

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddr, messagetosend)

server.quit()