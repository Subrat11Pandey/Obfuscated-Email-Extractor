import re
import requests
from bs4 import BeautifulSoup

# url = "https://techbaj.com/fake-emails-and-password/"
# url = "https://fauxid.com/tools/fake-email-list"
url = input("Please paste your url :- ")


response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


# decoding encripted email

encoded_emails = soup.select("a.__cf_email__")   #sare css class ke select kar raha hi jispe bhi <a> tag hai and class '__cf_email__' hai
def decode_email(encoded_email):
    r = int(encoded_email[:2], 16)
    email = ''.join([chr(int(encoded_email[i:i+2], 16) ^ r) for i in range(2, len(encoded_email), 2)])
    return email



#decode_email() function ko loop me run karna hi , taki sare email list me append ho jaye

decoded_emails =[]
for e in encoded_emails:
  decoded_emails.append(decode_email(e["data-cfemail"]))

# using RE for finding email non encripted , jo normally available hai

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, response.text)


#printing decoded and normal email separately 

if len(emails) >0:
  print(emails)
if len(decoded_emails) >0: 
  print(decoded_emails)
