import pandas as pd
import csv 

url= "gpt_faqs_combined.csv"

with open('gpt_faqs_combined_cleaned.csv', 'w', newline='', encoding="utf-8") as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(["record_id","term","faq"])
    
    
df = pd.read_csv(url)
for record_id,term,faq in zip(df["record_id"],df["term"],df["faq"]):
    headline = headline.replace("<h4>","</p><h4>")
    headline = headline.replace("A.","<p>A.")
    headline = headline.replace("</h3></p><h4>","</h3><h4>").replace("\n","").replace("><",">\n<")
    
    with open('gpt_faqs_batch_2_combined_cleaned.csv', 'a+', newline='', encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([record_id ,term, headline])
    