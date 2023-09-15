from numpy import append
import pandas as pd
from ftfy import fix_encoding

url = "GLS/version2/intro_test_2_generated (2).csv"
#record_id,keyword,URL Slug,intro
df1 = pd.read_csv(url, engine= "python", error_bad_lines= False)
id_list = []
intro_list = []

for ID,INTRO in zip(df1["id"],df1["final_intros"]):
    ix_1 = "@"
    ix_2 = "www"
    ix_3 = ".com"
    ix_4 = "$"
    ix_5 = "amazon"
    ix_6 = "ebay"
    ix_7 = "/"
    ix_8 = "online"
    ix_9 = "available in"
    INTRO = str(INTRO)
    
    INTRO = fix_encoding(INTRO)
    intro_split = INTRO.replace("??","").replace("? ?","").replace("??","").replace("?  ?","").replace("Â®","").replace("®","").replace("Â","").replace("€™","'").replace(". ",". $$$").replace("? ","? $$$").replace("! ","! $$$").split("$$$")
    if "\n" in intro_split[0]:
        intro_split[0]= intro_split[0].replace("\n","")
    
    
    intro_split_clean = []
    for i in intro_split:
        
        occurence_count1 = i.count(".")
        occurence_count2 = i.count("/")
        occurence_count3 = i.count("-")
        if ix_1 in i or ix_2 in i or ix_3 in i or ix_4 in i or ix_5 in i or ix_6 in i or ix_7 in i or ix_8 in i or ix_9 in i:
            i=""
        elif occurence_count1 > 2:
            i = ""
        elif occurence_count2 > 0:
            i = ""
        elif occurence_count3 > 2:
            i = ""
        intro_split_clean.append(i)
    
    
    intro_split_join = "".join(intro_split_clean)
    intro_split_join_split = intro_split_join.split("\n")
    
    intro_split_clean2 = []
    for i in intro_split_join_split:
        i = f"<p>{i}</p>"
        intro_split_clean2.append(i)
        
    intro_split_join2 = "".join(intro_split_clean2)
    
    id_list.append(ID)
    intro_list.append(intro_split_join2)

id_frame = pd.DataFrame(id_list,
                     columns = ['record_id'])

context_frame = pd.DataFrame(intro_list,
                     columns = ['intro'])




output_df = pd.concat([id_frame,context_frame], axis=1, join="inner")

output_df.to_csv(r"gls_intro_p_tags.csv")
#leftover_output_df.to_csv("serp_intro_leftoversq17.csv")

    
    
