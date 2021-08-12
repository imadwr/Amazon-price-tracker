from amazonscraper import AmazonScraper
from emailManager import EmailManager


product_preset_price = 80


amz = AmazonScraper()
amz.get_product_price()
print(amz.product_price)

if amz.product_price <= product_preset_price:
    email = EmailManager()
    email.send_email(product_actual_price=amz.product_price, product_name=amz.product_title)
    print("email sent successfully")
else:
    print("No price drop.")






