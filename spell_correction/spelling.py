
import csv
import urllib.request
import time
import pandas as pd
from autocorrect import Speller

spell = Speller(lang='en')


with open("fix_spelling.csv", 'w', newline='', encoding="utf-8") as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(["Term","sv-ahrefs"])
    
    
url = 'URL Tracker - Best Brands Corp (BBC) - shop_bbc.csv'
df = pd.read_csv(url, encoding="utf-8", engine="python", error_bad_lines=False)
df = df

for v, w in zip(df["term"], df["sv-ahrefs"]):
    spell = Speller(lang='en')
    Term = spell(v)
    print(Term)

    # BLACKLIST
  
    with open('fix_spelling.csv', 'a+', newline='', encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([Term, w]) #Index,Term,Context,Introduction,Blog1





