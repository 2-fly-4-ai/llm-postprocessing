
import pandas as pd
from bs4 import BeautifulSoup
import ftfy
import html
#! coding: utf-8

sheet_url = "small_pets_articles - Sheet1.csv"
df1 = pd.read_csv(sheet_url,  encoding= "utf-8")

url_list = []
breadcrumb_list = []
heading_list=[]
text_list = []
wordcount_list = []

for url,breadcrumb,text in zip(df1["url"],df1["breadcrumbs"],df1["text"]):
    breadcrumb = str(breadcrumb).replace("\n","")
    heading = text.replace("</h1>","</h1>$$$").split("$$$")[0]
    text = text.replace("</h1>","</h1>$$$").split("$$$")[-1]
    text = html.unescape(text)
    text = text.replace("> ",">").replace(" <","<").replace("<h2> More","<h2>More").replace("\n","").replace("\n","")
    text = str(text.split("<h2>More")[0])
    text_list_split =text.replace(">",">$$$").replace("<","$$$<").replace(".",".$$$").replace("Â","").replace("$$$$$$","$$$").split("$$$")
    
    #Tabatha, Alycia, vol. Vol. Vol vol Watch Now: 
    #fix_this_shit = &rsquo;   "  "  — ' ' 
    
    text_list_fixed = []
    
    if "picture" in heading or "Picture" in heading:
        continue
    
    for i in text_list_split:
        if ":" in i:
            print(i)
            if i[-1] == ":":
                continue
            else:
                text_list_fixed.append(i)
        else:
            text_list_fixed.append(i)
            
    text_list_fixed_2 = []
    
    for i in text_list_fixed:
        if " Vol " in i or " vol." in i or "Getty" in i or "Alycia" in i or "@" in i or "washington" in i or "Washington" in i or "currently works as a" in i or "Tabitha Kucera" in i  or "Kucera" in i or "and a Certified Cat Behavior Consultant." in i or "is also Fear Free Certified" in i or "is also Fear Free Certified" in i or "wiki" in i  or "Wiki" in i or "is also Fear Free Certified" in i or "Flick" in i or "Jessie Sanders" in i:
            continue
        else:
            text_list_fixed_2.append(i)
       
            
    text = "".join(text_list_fixed_2)
    text = heading + text
    
    
    text = ftfy.fix_text(text)
    text = text.replace("\n","")
    print(text)
    
    # bs_content = BeautifulSoup(text, "lxml")
    # print(bs_content)
    
    
    wordcount= len(text.split(" ")) 
    
    url_list.append(url)
    breadcrumb_list.append(breadcrumb)
    text_list.append(text)
    wordcount_list.append(wordcount)
    heading_list.append(heading)
    
df_url1 = pd.DataFrame (url_list, columns = ['url'])
df_breadCrumb1 = pd.DataFrame (breadcrumb_list, columns = ['breadcrumbs'])
df_text1 = pd.DataFrame (text_list, columns = ['text'])
df_wordcount1 = pd.DataFrame (wordcount_list, columns = ['word_count'])
df_headings = pd.DataFrame(heading_list, columns=["headings"])
    
result1 = pd.concat([df_url1, df_breadCrumb1,df_headings, df_text1,df_wordcount1], axis=1, join="inner")

result1.to_csv("spruce_info_small_animal_articles_dataset_post.csv")
    
    
    
    
        
        
        
        
        
        

        
        
        
        


