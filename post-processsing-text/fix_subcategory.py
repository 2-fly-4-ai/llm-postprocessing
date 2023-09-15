
import pandas as pd
from bs4 import BeautifulSoup
import ftfy
#! coding: utf-8


sheet_url = "dog_beds_furniture_final - dog_beds_furniture_final.csv"
df1 = pd.read_csv(sheet_url,  encoding= "utf-8")

sheet_url2 = "2022-12-13-product-a9c821bb-3e8b-0227-e014-a1d641605190.csv"
df2 = pd.read_csv(sheet_url2,  encoding= "utf-8")

asin_list = []
taxonomy_list = []


for asin,taxonomy,subcategory in zip(df1["ASIN"],df1["product_taxonomy"],df1["primary_subcategory"]):
    if str(subcategory) != "nan":
        new_tax = str(taxonomy)+" > "+str(subcategory)
    else:
        new_tax = str(taxonomy)
        
  
    asin_list.append(asin)
    taxonomy_list.append(new_tax)
  
    
asin_df = pd.DataFrame (asin_list, columns = ['ASIN'])
tax_df = pd.DataFrame (taxonomy_list, columns = ['NEW_TAXONOMY'])

    
result1 = pd.concat([asin_df,tax_df ], axis=1, join="inner")

final = df2.merge(result1, how="outer", on='ASIN')
final.to_csv("dog_beds_furniture_with_categories.csv")
    
    
    
    
        
        
        
        
        
        

        
        
        
        


