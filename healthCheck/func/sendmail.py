import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from healthCheck.variaveis import var

def reportEmail():
    global server
    serversmtp = var.serverSmtp
    port = var.porta
    senderEmail = var.remetente
    password = var.senha
    receiverEmail = var.destinatario
    subject = 'ALERTA'
    body = """
    <p>Olá,</p>
    <p>Site esta fora do ar, tentativa de acesso sem scuesso.</p>
      <p>Favor verificar! </p>
    """

    message = MIMEMultipart()
    message["From"] = senderEmail
    message["To"] = receiverEmail
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))

    #conection
    try:
        #server SMTP
        server = smtplib.SMTP(serversmtp, port)
        server.starttls()
        #login
        server.login(senderEmail, password)
        #Destino
        server.sendmail(senderEmail, receiverEmail, message.as_string())
        print('email enviado')
    except Exception as e:
        error = e
        print(error)
    finally:
        server.quit()

