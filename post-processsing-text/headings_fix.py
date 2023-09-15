import pandas as pd
import csv

with open('pets_intros_combined_last_cleaned.csv', 'w',newline='' , encoding="utf-8") as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    # writing the fields 
    csvwriter.writerow(["record_id","term","headline"])

df = pd.read_csv("pets_intros_last_combined.csv")


for record_id,term,headline in zip(df["record_id"],df["term"],df["headline"]):
    headline = headline.replace("\n","")
    
    with open('pets_intros_combined_last_cleaned.csv', 'a+', newline='', encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([record_id, term, headline])