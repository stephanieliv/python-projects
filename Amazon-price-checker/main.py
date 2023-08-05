from bs4 import BeautifulSoup
import lxml
import requests
import smtplib

url = "https://www.amazon.co.uk/Tefal-EY401840-Fryer-Precision-Portions/dp/B07D1LTRGW/ref=sr_1_3?keywords=air+fryers&qid" \
      "=1653060504&sprefix=air+%2Caps%2C245&sr=8-3"
headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
               "(KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
            "Accept-Language":
                "en-US,en;q=0.9"
            }
my_email = "teststephanie58@gmail.com"
my_password = "RhH3uWkOur55"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "lxml")
price = float(soup.find(class_="a-offscreen").get_text().split("£")[1])
print(price)

if price <= 69.99:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="stephanie.livingstone44@googlemail.com",
                            msg=f"Subject: Amazon Price Alert\n\nThe air fryer is now £{price}!\n\n"
                                f"hop on and buy it here:{url}")
