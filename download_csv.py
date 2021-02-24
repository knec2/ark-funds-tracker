import os
import requests
from time import time
import datetime
import shutil

#creating the folder with date
parent_dir = "C:/Users/bally/Projects_Algo/ark-funds-tracker/data/"
today = datetime.date.today()
todaystr = today.isoformat()
path = os.path.join(parent_dir,todaystr)
os.mkdir(path)
print(path)

# fetching the file from the website
def url_response(url):
    path, url = url
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
         for ch in r:
             f.write(ch)


urls = [
("ARKK.csv", "https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv"),
("ARKQ.csv", "https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_AUTONOMOUS_TECHNOLOGY_&_ROBOTICS_ETF_ARKQ_HOLDINGS.csv"),
("ARKW.csv", "https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_NEXT_GENERATION_INTERNET_ETF_ARKW_HOLDINGS.csv"),
("ARKG.csv", "https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_GENOMIC_REVOLUTION_MULTISECTOR_ETF_ARKG_HOLDINGS.csv"),
("ARKF.csv", "https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_FINTECH_INNOVATION_ETF_ARKF_HOLDINGS.csv"),
("PRNT.csv", "https://ark-funds.com/wp-content/fundsiteliterature/csv/THE_3D_PRINTING_ETF_PRNT_HOLDINGS.csv"),
("IZRL.csv", "https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_ISRAEL_INNOVATIVE_TECHNOLOGY_ETF_IZRL_HOLDINGS.csv")]

start = time()
for x in urls:
    url_response(x)

print(f"Time to download: {time() - start}")

# funtion to moving file to the folder
def movefile():
    files = ['ARKG.csv','ARKF.csv','ARKK.csv','ARKQ.csv','ARKW.csv','PRNT.csv','IZRL.csv']
    for f in files:
         shutil.move(f, path)

movefile()