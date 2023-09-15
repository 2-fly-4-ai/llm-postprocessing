import pandas as pd

url = "input.csv"


df1 = pd.read_csv(url, engine="python" , encoding= "utf-8")
# df1.info()
# df1 = df1.head()

url_list_best = []
breadcrumb_list_best = []
text_list_best = []
wordcount_best = []

     
url_list_info = []
breadcrumb_list_info = []
text_list_info = []
wordcount_info = []

for url,breadcrumb,text in zip(df1["url"],df1["breadcrumb"],df1["text"]):
    breadcrumb = str(breadcrumb).replace("\n","")
    wordcount=len(text.split(" "))
    text = text.replace("<html><body>","").replace("</body></html></html>","")
    
    
    
    if "Best" in text:
        
        url_list_best.append(url)
        breadcrumb_list_best.append(breadcrumb)
        text_list_best.append(text)
        wordcount_best.append(wordcount)
    else:
        
        url_list_info.append(url)
        
        breadcrumb_list_info.append(breadcrumb)
        
        text_list_info.append(text)
        
        wordcount_info.append(wordcount)
        
        
df_url1 = pd.DataFrame (url_list_best, columns = ['url'])
df_breadCrumb1 = pd.DataFrame (breadcrumb_list_best, columns = ['breadcrumbs'])
df_text1 = pd.DataFrame (text_list_best, columns = ['text'])
df_wordcount1 = pd.DataFrame (wordcount_best, columns = ['word_count'])
    
df_url2 = pd.DataFrame (url_list_info, columns = ['url'])
df_breadCrumb2 = pd.DataFrame (breadcrumb_list_info, columns = ['breadcrumbs'])
df_text2 = pd.DataFrame (text_list_info, columns = ['text'])
df_wordcount2 = pd.DataFrame (wordcount_info, columns = ['word_count'])
    
    
result1 = pd.concat([df_url1, df_breadCrumb1, df_text1,df_wordcount1], axis=1, join="inner")
result2 = pd.concat([df_url2, df_breadCrumb2, df_text2,df_wordcount2], axis=1, join="inner")
    
result1.to_csv("best_pets_dataset.csv")
result2.to_csv("info_pets_dataset.csv")
    
    
    
    
        
        
        
        
        
        

        
        
        
        

