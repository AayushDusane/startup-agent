import smtplib
from email.message import EmailMessage
from pathlib import Path


def send_email_with_attachment(
    sender_email,
    app_password,
    receiver_email,
    attachment_path
):
    msg = EmailMessage()
    msg["Subject"] = "Daily YC Startup Jobs 🚀"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.set_content(
        "Hey 👋\n\n"
        "Attached is today's list of YC startups hiring.\n\n"
        "Go get them 😤\n"
    )

    attachment_path = Path(attachment_path)
    with open(attachment_path, "rb") as f:
        file_data = f.read()

    msg.add_attachment(
        file_data,
        maintype="text",
        subtype="csv",
        filename=attachment_path.name
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)
