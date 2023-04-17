from bs4 import BeautifulSoup
import requests
from datetime import datetime
#import urllib3 

#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
start = datetime.now()

# if a company has more than one website

with open("sites.txt", "r") as f:
    text = f.read()

result = text.split("|")

with open("urls.txt", "w") as f:
    for item in result:
        f.write(f"{item}\n")        

bitrix = []

with open("urls.txt") as urls:
    for url in urls:
        try:
            page = requests.get("http://"+url.strip('\n'), verify=False)
            soup = BeautifulSoup(page.content, "html.parser")
            script_soup = soup.find_all("script")
            script_soup = str(script_soup)

            for i in url:    
                if script_soup.find("bitrix") >= 0 or script_soup.find("b24") >= 0:
                    bitrix.append(url)
                    break
        except requests.exceptions.RequestException:
            pass

with open("bitrix.txt", "w") as f:
    for _ in bitrix:
        f.write(_)

finish = datetime.now()
print(finish - start)