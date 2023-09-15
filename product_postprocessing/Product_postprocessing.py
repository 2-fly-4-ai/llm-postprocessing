import csv
from bs4 import BeautifulSoup
import urllib.request
import time
import pandas as pd
import sys
import re
import random
import math
import ast

url = 'z_merge_test_27062022.csv'
df = pd.read_csv(url, encoding="utf8", engine="python", error_bad_lines=False)
#df = df.head(1000)
#df = df.drop_duplicates(subset=['keyword'])
#id,asin,total_ratings,product_features,final_titles,brand,final_features,final_adverts

ID_list = []
asin_list = []
rating_list = []
brand_list = []
image_url_list = []
name_list = []
finaladverts_list = []
product_features_list = []

x = float('nan')

fucked_ones = 0
for a,b,c,d,e,f,g,h in zip(df["id"],df["asin"],df["total_ratings"],df["brand"],df["product_features"],df["final_features"],df["final_titles"],df["final_adverts"]):
    fixed_aida =  str(h).split("\n")[0]
    e = str(e)
    d = str(d)
    if len(d.split(" ")) > 1:
        d = d
    else:
        x = e.replace("{","").replace("}","").split(",")
        for i in x:
            if "Brand" in i:
                ##print("DINGDING")
                i = i.replace("'Brand': ","").replace("'","")
                if i[0] == " ":
                    d = i[1:]
                else:
                    d = i
                
    if f == "nan":
        f = ""
        
    if d == "nan":
        d = ""
        
    if e == "nan":
        e = ""
       
    #features
    f = f.replace("-","$$$-")
    f = f.split("$$$")
    newlist = ""
    for i in f:
        x_num = i.split(" ")
        if len(x_num) > 25:
            i = ""
        newlist += i
    
    f = newlist
    #print(f)   
     
     
    #sys.exit()   
    if len(fixed_aida.split(" ")) < 30:
        fucked_ones += 1
        #print(fucked_ones)
        continue
    
    ID_list.append(a)
    asin_list.append(b)
    rating_list.append(c)
    brand_list.append(d)
    product_features_list.append(e)
    image_url_list.append(f)
    name_list.append(g)
    finaladverts_list.append(fixed_aida)
    
record_id = pd.DataFrame(ID_list,columns = ['record_id'])
asin = pd.DataFrame(asin_list,columns = ['asin'])
total_ratings = pd.DataFrame(rating_list,columns = ['total_ratings'])
brand = pd.DataFrame(brand_list,columns = ['brand']) 
product_features= pd.DataFrame(product_features_list,columns = ['product_features']) 
image_urls= pd.DataFrame(image_url_list,columns = ['features']) 
name = pd.DataFrame(name_list,columns = ['name']) 
aida = pd.DataFrame(finaladverts_list,columns = ['aida']) 

  
  
test1 = pd.concat([record_id,asin,total_ratings,brand,image_urls,name,aida], axis=1, join="inner")

test1.to_csv(r"Gls_product_pp.csv")
 

