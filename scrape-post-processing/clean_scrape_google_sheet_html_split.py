# Import necessary libraries
import pandas as pd
from bs4 import BeautifulSoup
import ftfy

# Define the Google Sheets URL
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSO1MYSadh0LbiaTpGMf63pDoJVK_lAPPy5UHxT9VyO6fvKGGKjtzb5Y-XlCF_eXFnZjRbDbRIEJRuY/pub?output=csv"

# Read data from the Google Sheets CSV
df1 = pd.read_csv(sheet_url, encoding="utf-8")

# Initialize lists to store extracted data
url_list = []
breadcrumb_list = []
heading_list = []
text_list = []
wordcount_list = []

# Iterate through the rows of the DataFrame
for url, breadcrumb, text in zip(df1["source"], df1["tax"], df1["text"]):
    # Clean up the breadcrumb
    breadcrumb = str(breadcrumb).replace("\n", "")

    # Extract heading and text from HTML content
    heading = text.replace("</h1>", "</h1>$$$").split("$$$")[0]
    text = text.replace("</h1>", "</h1>$$$").split("$$$")[-1]
    
    # Clean up text formatting
    text = text.replace(">", ">$$$").replace("<", "$$$<").replace(".", ".$$$").replace("$$$$$$", "$$$")
    text = text.replace(" >", ">").replace(" <", "<").replace("<h2> More", "<h2>More").replace("\n", "")
    text = str(text.split("<h2>More")[0])
    
    # Split text content into sections
    text_list_split = text.split("$$$")
    
    text_list_fixed = []
    
    # Remove unnecessary colons from text sections
    for i in text_list_split:
        if ":" in i:
            if i[-1] == ":":
                continue
            else:
                text_list_fixed.append(i)
        else:
            text_list_fixed.append(i)
    
    # Reconstruct the cleaned text
    text = "".join(text_list_fixed)
    
    # Fix any text encoding issues
    text = ftfy.fix_text(text)
    
    # Calculate word count
    wordcount = len(text.split(" ")) 
    
    # Append data to lists
    url_list.append(url)
    breadcrumb_list.append(breadcrumb)
    text_list.append(text)
    wordcount_list.append(wordcount)
    heading_list.append(heading)

# Create DataFrames from lists
df_url1 = pd.DataFrame(url_list, columns=['url'])
df_breadCrumb1 = pd.DataFrame(breadcrumb_list, columns=['breadcrumbs'])
df_text1 = pd.DataFrame(text_list, columns=['text'])
df_wordcount1 = pd.DataFrame(wordcount_list, columns=['word_count'])
df_headings = pd.DataFrame(heading_list, columns=["headings"])

# Concatenate DataFrames
result1 = pd.concat([df_url1, df_breadCrumb1, df_headings, df_text1, df_wordcount1], axis=1, join="inner")

# Save the result to a CSV file
result1.to_csv("test.csv")
