import smtplib
import os


email = os.getenv("from_email")
password = os.getenv("password")
to_email = os.getenv("to_email")


class EmailManager:

    def send_email(self, product_actual_price, product_name):

        message = f"{product_name}, are now ${product_actual_price}, below your preset price."

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=to_email,
                msg=f"Subject: Amazon price Alert!\n\n{message}"
            )
