from numpy import append
import pandas as pd
from ftfy import fix_encoding

url = "features_extraction_dataset4.csv"
#record_id,keyword,URL Slug,intro
df1 = pd.read_csv(url, engine= "python", error_bad_lines= False)
namelist = []
features_list = []
description_list = []
output_list = []



for Name,Features,Description,Output in zip(df1["Name"],df1["Features"],df1["Description"],df1["Output"]):
    Output = Output.replace("-","-$$$").split("$$$")
    if "\n" in Output[0]:
        Output[0] = Output[0].replace("\n","")
    Output = "".join(Output)
    print(Output)
    namelist.append(Name)
    features_list.append(Features)
    description_list.append(Description)
    output_list.append(Output)
  
 

    
    

        
    
    
#iw = pd.DataFrame(intro_wordcount,
                     #columns = ['intro_wordcount']) 

id_frame = pd.DataFrame(namelist,
                     columns = ['Name'])
term_frame = pd.DataFrame(features_list,
                     columns = ['Features']) 
context_frame = pd.DataFrame(description_list,
                     columns = ['Description'])
context_list = pd.DataFrame(output_list,
                     columns = ['Output'])    



output_df = pd.concat([id_frame,term_frame,context_frame,context_list], axis=1, join="inner")

output_df.to_csv(r"z_serp_features_test.csv")


    
    
