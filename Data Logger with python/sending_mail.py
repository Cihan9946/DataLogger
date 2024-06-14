import redis
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import json


# E-posta gönderenin bilgileri
sender_email = "deneme@gmail.com"
sender_password = "icpm zsxk pqwm pmjo"  # E-posta şifreniz
# E-posta alıcının adresi
receiver_email = "deneme2@gmail.com"

# E-posta başlığı ve içeriği
def sendMail(receiver_email, body,rec):
    receiver_email = rec
    # SMTP sunucu bilgileri
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    # E-posta oluşturma
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message.attach(MIMEText(body, 'plain'))

    # SMTP bağlantısı kurma
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # E-postayı gönderme
        server.sendmail(sender_email, rec, message.as_string())
        print("E-posta başarıyla gönderildi!")

    except Exception as e:
        print("E-posta gönderme hatası:", str(e))

    finally:
        # SMTP bağlantısını kapatma
        server.quit()


redis_conn = redis.Redis(
    host='localhost',
    port=6379,
    charset="utf-8",
    decode_responses=True
)

# Redis üzerindeki "channel" isimli kanalı dinle
pubsub = redis_conn.pubsub()
pubsub.subscribe("channel")
print("Başlıyor....")
for message in pubsub.listen():
    if message['type'] == 'message':
        try:
            data = json.loads(message['data'])  # message['data'] geçerli bir JSON dizesi olarak kabul ediliyor

            to = data.get('to', '')
            subject = data.get('subject', '')
            body = data.get('body', '')
            
            print(f"To: {to}")
            print(f"Subject: {subject}")
            print(f"Body: {body}")
            try:

            # İşlemleri gerçekleştir (örneğin, e-posta gönderme)
                print("okokk")
                sendMail(receiver_email, body,to)

            except:
                print("hata oluştu")

        except json.decoder.JSONDecodeError:
            print("Mesaj verisinde geçersiz JSON formatı.")
        except Exception as e:
            print("Ana işlem hatası:", str(e))
