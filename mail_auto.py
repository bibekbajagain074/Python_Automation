import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# def send_local_email(subject, body, sender_email="hydration_reminder@localhost", receiver_email="recipient@localhost"):
#     """
#     Sends an email via a local SMTP server.
#     """
#     smtp_server = "localhost"
#     smtp_port = 1025

#     # Set up the email message
#     msg = MIMEMultipart()
#     msg["From"] = sender_email
#     msg["To"] = receiver_email
#     msg["Subject"] = subject

#     # Attach the body of the email
#     msg.attach(MIMEText(body, "plain"))

#     # Connect to the local SMTP server and send the email
#     try:
#         with smtplib.SMTP(smtp_server, smtp_port) as server:
#             server.sendmail(sender_email, receiver_email, msg.as_string())
#         print(f"{subject} email sent successfully via local SMTP.")
#     except Exception as e:
#         print(f"Error sending local email: {e}")

# send_local_email("THis is test from from function","Hello")

def send_gmail(subject, body, sender_email, receiver_email, password):
    """
    Sends an email via Gmail SMTP server.
    """
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Set up the email message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # Attach the body of the email
    msg.attach(MIMEText(body, "plain"))

    # Connect to the Gmail server and send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"{subject} email sent successfully via Gmail.")
    except Exception as e:
        print(f"Error sending Gmail email: {e}")


send_gmail("This is test email from code","Hello python WOrkshop","absproject7@gmail.com","bibekbajagain074@gmail.com","eyeg fciw ojjz nvpx ")