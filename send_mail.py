

def sending_mail(filepdf):

    import smtplib, ssl
    import socket
    import getpass
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders


    email_user = "juanivannb142@gmail.com"
    email_send = "coldcram14@hotmail.com"
    subject = 'JINB'
        #password = getpass.getpass("Type your password and press enter: ")
        #password = 'obgekeoucjsoborx'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'Hi mister this is your ticket!'
    msg.attach(MIMEText(body,'plain'))

    #filename = 'ticket.txt'
    filename = filepdf
    attachment = open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment: filename = ' + filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, 'obgekeoucjsoborx')

    server.sendmail(email_user,email_send,text)
    server.quit()

    return 'mail ok'

#print(sending_mail('ticket.txt'))