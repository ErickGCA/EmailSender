import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import time
from dotenv import load_dotenv

load_dotenv()

def ler_emails_de_arquivo(caminho_arquivo):
    emails = []
    try:
        with open(caminho_arquivo, 'r') as f:
            for linha in f:
                linha = linha.strip()
                if '@' in linha: 
                    emails.append(linha)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
    return emails

def enviar_email(remetente, senha, destinatario, assunto, mensagem):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remetente, senha)

        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = destinatario
        msg['Subject'] = assunto
        msg.attach(MIMEText(mensagem, 'plain'))

        server.sendmail(remetente, destinatario, msg.as_string())
        server.quit()

        print(f"Email enviado para: {destinatario}")
    except Exception as e:
        print(f"Erro ao enviar email para {destinatario}: {e}")


def main():
    email_remetente = os.getenv('EMAIL_SENDER') 
    senha_remetente = os.getenv('EMAIL_PASSWORD')  
    assunto = "Titulo de Email"
    mensagem = "Corpo do Email"

    lista_emails = ler_emails_de_arquivo("emailsf.txt")

    if not lista_emails:
        print("Nenhum email encontrado no arquivo.")
        return

    for destinatario in lista_emails:
        enviar_email(email_remetente, senha_remetente, destinatario, assunto, mensagem)
        time.sleep(10)  # Intervalo de 10 segundos entre os e-mails

    print("Emails enviados com sucesso!")

if __name__ == "__main__":
    main()
