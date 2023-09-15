from numpy import append
import pandas as pd
from ftfy import fix_encoding

url = "serp-canonicals.csv"
#record_id,keyword,URL Slug,intro
df1 = pd.read_csv(url, engine= "python", error_bad_lines= False)
namelist = []




for canonicals in zip(df1["canonical_link"]):
    canonicals = str(canonicals[0]).replace("https://www.amazon.com/","").replace("-"," ").split("/")[0].lower().split("%")[0]
    print(canonicals)
    namelist.append(canonicals)
    
#iw = pd.DataFrame(intro_wordcount,
                     #columns = ['intro_wordcount']) 

id_frame = pd.DataFrame(namelist,
                     columns = ['TERM'])
id_frame  =  id_frame.drop_duplicates(subset=["TERM"], keep='first', inplace=False)

output_df = pd.concat([id_frame], axis=1, join="inner")

output_df.to_csv(r"canonical_test.csv")


    
    
