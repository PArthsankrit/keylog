import smtplib, ssl

def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "sankritparth064@gmail.com"
    password = "Kuroko@123"
    receiver_email = "sankritparth064@gmail.com"

    context = ssl.create_default_context()

    try:
        server =smtplib.SMTP(smtp_server,port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email,password)
        server.sendmail(sender_email,recover_email,message)

    except Exception as e:
        print(e)
    finally:
        server.quit()
