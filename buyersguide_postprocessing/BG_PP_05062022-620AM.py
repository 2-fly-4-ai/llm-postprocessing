import csv
from bs4 import BeautifulSoup
import urllib.request
import time
import pandas as pd
import sys
import re
import random

url = 'compulsive_pre_bg.csv'
df = pd.read_csv(url, encoding="utf8", engine="python", error_bad_lines=False)
#df = df.drop_duplicates(subset=['keyword'])
df = df

ID_list = []
term_list = []
intro_list = []
blog_list = []
intro_wordcount = []
blog_wordcount = []
leftoverKeywords = []
leftoverID = []
context_list = []

for x ,v, y in zip(df["keyword_id"],df["keyword"],df["guide"]):
    Term = v
    ID = x
    blog = str(y)
    blog = blog.replace("<","$$$<").replace(">",">$$$").replace(". <",".<").replace(".<",". $$$<").replace(". A",". $$$A").replace(". B",". $$$B").replace(". C",". $$$C").replace(". D",". $$$D").replace(". E",". $$$E").replace(". F",". $$$F").replace(". G",". $$$G").replace(". H",". $$$H").replace(". I",". $$$I").replace(". J",". $$$J").replace(". K",". $$$K").replace(". L",". $$$L").replace(". M",". $$$M").replace(". N",". $$$N").replace(". O",". $$$O").replace(". P",". $$$P").replace(". Q",". $$$Q").replace(". R",". $$$R").replace(". S",". $$$S").replace(". T",". $$$T").replace(". U",". $$$U").replace(". V",". $$$V").replace(". W",". $$$W").replace(". X",". $$$X").replace(". Y",". $$$Y").replace(". Z",". $$$Z").split("$$$")
    
    
    blog_newlist = ["",""]
    tag_id = "<"
    
    
    blog = [x for x in blog if x != '']
    blog = [x for x in blog if x != '\n']
    
    list_no_dupes_check = []
    for i in blog:  #####print(i)
        if tag_id not in i:
            if i != "Yes. " and i != "No. " and i != "A: Yes. " and i != "A: No. ":
                if i[-1] == " ":
                    i = i[0:-1]
                list_no_dupes_check.append(i) 
        x = list_no_dupes_check.count(i)
        
        ####print(x)
        if x > 1:
            
                print(f"{ID} -WORKING - {i}")
                i = ""
                #print(f"Triggered = {x}")
        blog_newlist.append(i)
        #####print(list_no_dupes_check)        
    #print(list_no_dupes_check)
    blog = "".join(blog_newlist)
    ################print(blog)

##########################################################################################################################
####################################### BS4 DECOMPOSER ###################################################################  

    soup = BeautifulSoup(blog)
    for div in soup("div"):
        div.decompose()
    for table in soup("table"):
        table.decompose()
    for span in soup("span"):
        span.decompose()
    for break1 in soup("br"):
        break1.decompose()
    for img in soup("img"):
        img.decompose()
    for break2 in soup("hr"):
        break2.decompose()
    for script1 in soup("script"):
        script1.decompose()
    for script2 in soup("noscript"):
        script2.decompose()
    for style in soup("style"):
        style.decompose()
    for style in soup("style"):
        style.decompose()
    for link in soup("a"):
        link.decompose()
    for link in soup("tr"):
        link.decompose()
    for link in soup("td"):
        link.decompose()
    for iframe in soup("iframe"):
        iframe.decompose()
    soupfinal = soup

  
    pre2 = ''.join([str(tag) for tag in soupfinal])
    
########################################################################################################################## 
####################################### GRABS THE HEADING ################################################################
    
    pre2 = pre2.replace("</h2>","</h2>$$").replace("<html><body>","").replace("<html><body>","").replace("</body></html>","").replace("-->","").replace("<!--","").replace("<h5>","<h3>").replace("</h5>","</h3>").replace("/n","").replace("&lt;","").replace("<h4>;","<h3>").replace("</h4>;","</h3>")
    split1 = pre2.split("$$")
    heading = split1[:1]
    heading= "".join(heading)
    heading = heading.replace("<h2>","<h2>$$$").replace("</h2>","$$$</h2>").split("$$$")
    hstringtest ="<h2>"
    hstringtest2 ="</h2>"
    heading2 = ""
    for i in heading:
        if hstringtest not in heading or hstringtest2 not in heading:
            heading2 += i
        else:
            i = i.title()
            heading2 += i   
    
    heading = heading2.replace("H2","h2")
    #if Term.lower()[-1] == "s" and "with" not in Term.lower() and Term.lower()[-2] != "a" and Term.lower()[-2] != "i" and Term.lower()[-2] != "o" and Term.lower()[-2] != "u":
                    #heading = heading.lower()
                    #i = i.replace("what is the purpose of a","what is the purpose of")
                    #i = i.title().replace("H3","h3")
                    ###############print(i)
                    
    #################print(heading)
    
    body = split1[1:]
    body = "".join(body)
    
    body = body.split(" ") ####YOU CHANGED THIS!@ BEWARE 

##########################################################################################################################
####################################### TRYING TO FIND WEB ADRESSES ######################################################

    cleanlist3 = []
    for i in body:
      Occurence_count = i.count(".")#Checks fot the occurence of this particular character and sets threshold. if over a certain amount it needs to skip and just use the input as the output. THis is for haandling those rare, repeated phone number outputs we get. 
      Occurence_count2 = i.count("www")
      if Occurence_count + Occurence_count2 > 3:
          del i
      else:
        cleanlist3.append(i)

    cleanlist4 = []
    for i in cleanlist3:
      Occurence_count = i.count(".")#Checks fot the occurence of this particular character and sets threshold. if over a certain amount it needs to skip and just use the input as the output. THis is for haandling those rare, repeated phone number outputs we get. 
      Occurence_count2 = i.count("www")
      
      if Occurence_count > 3 or Occurence_count2 > 1:
          del i
      else:
        cleanlist4.append(i)

##########################################################################################################################
####################################### FIND MISSING GENERATIONS IN PARAGRAPHS ###########################################

    body_presplit_split = " ".join(cleanlist3)
    body_split1 = body_presplit_split.replace("<p>","$$$<p>").replace("</p>","</p>$$$").replace("<p></p>", "").split("$$$")
    
    
    substring_identify_p = "<p>"
    substring_punc1 = "."
    substring_punc2 = "!"
    substring_punc3 = "?"
    substring_endless_ordered_list1 = "eleventh"
    substring_endless_ordered_list2 = "Eleventh"

##########################################################################################################################
####################################### REPLACEMENT & DECODING ###########################################################
    
    body_join1 = "".join(body_split1)
    body_presplit_split = body_join1.replace("<", "$$$<").replace(">", ">$$$").replace(
        ". ", ".$$$ ").replace("? ", "?$$$ ").replace("! ", "!$$$ ").replace("&lt;", "").replace("&;lt", "").replace('â€“', "-").replace("â€™","'").replace("/ul&gt;","").replace("&nbsp;","")# THAT FUCKING DECODING ISSUE
    
    body_split = body_presplit_split.split("$$$")
    
##########################################################################################################################
####################################### SOLVING THE ENDLESS LIST ISSUE ###################################################
        
    newray = ""
    
    for i in body_split:
        i = i.replace(",",",$$$")
        i = i.split("$$$")
        i = i[:15]
        i = "".join(i)
        newray+= i
        
    newray = newray.replace("<", "$$$<").replace(">", ">$$$").replace(
        ". ", ".$$$ ").replace("?", "?$$$").replace("!", "!$$$")
    newray = newray.split("$$$")
    
    
        
##########################################################################################################################
####################################### BLACKLIST ########################################################################
        
    BLACKLIST = ["Title:","Blog article:","order any of these items","please visit our","Bio:","Tags:","Author:","About us:","Facebook","Instragram","written by","=>","=<",">=","since ancient times","online store","have been around since ancient times","Review","top 10","Published","Copyright","11)","12)","13)","14)",")","15)","16)","17)","18)","19)","20)","21)","22)","23)","24)","25)","26)","27)","28)","29)","30)","31)","32)","33)","34)","35)","36)","37)","38)","39)","40)","41)","42)","43)","44)","45)","46)","47)","48)","49)","50)","51)","52)","53)","54)","55)","56)","57)","58)","59)","Amazon","amazon","Add To Cart","<img>","<a>","1-800","www",'$','http', 'ebay',"Walmart","Ebay","Costco","BestBuy","€","shipping", "costco","PayPal", "paypal", ".biz",  "bestbuy","blog","author","About us","About us","Visit the site","contact us","This website",".org",".com",".biz","Here are two good resources","@",".net","This item includes","best-buy","Specifications", 'email', "call-us","call us","give us a call","Give us a call", " seo " , "we are a ","our website","buy online at","money back guarantee","Final Thoughts", "In Conclusion","Final thoughts", "In conclusion"]

    cleanlist2 = []
    for i in newray:
        for substring in BLACKLIST:
            if substring in i:
                i = ""
        cleanlist2.append(i)
#########################################################################################################################
########################################## REPLACEMENT PATTERNS 1########################################################

    cleanlist = "".join(cleanlist2)
    ###print(cleanlist)
    
    
    
    cleanlist = cleanlist.replace("<li ", "").replace("<h1>", "<h3>").replace("<h2>", "<h3>").replace("</h2>","</h3>").replace("<br>", "").replace("</h1>","</h3>").replace("<ul>", "").replace("</ul>", "").replace("<ol>", "").replace(
        "<p></p>", "").replace("</ol>", "").replace("<li>", "<p>").replace("</li>", "</p>").replace("<h3></h3>", "").replace("<p></p>", "").replace("<h2></h2>", "").replace("<strong>", "").replace("</strong>", "").replace("</p></p>", "</p>").replace("</p></p>", "</p>").replace("</p></p>", "</p>").replace("</p></h3>", "</p>").replace("</p></p>", "</p>").replace(".A", ". A").replace(".A", ". A").replace(".B", ". B").replace(".C", ". C").replace(".D", ". D").replace(".E", ". E").replace(".F", ". F").replace(".G", ". G").replace(".H", ". H").replace(".I", ". I").replace(".J", ". J").replace(".K", ". K").replace(".L", ". L").replace(".M", ". M").replace(".N", ". N").replace(".O", ". O").replace(".P", ". P").replace(".Q", ". Q").replace(".R", ". R").replace(".S", ". S").replace(".T", ". T").replace(".U", ". U").replace(".V", ". V").replace(".W", ". W").replace(".X", ". X").replace(".Y", ". Y").replace(".Z", ". Z").replace('<h3="""">','')
    cleanlist = cleanlist.replace("<", "$$$<").replace(">", ">$$$").replace(
        ". ", ".$$$ ").replace("?", "?$$$").replace("!", "!$$$")
    cleanlist = cleanlist.replace("$$$<h3>$$$","$$$<h3>").replace("$$$</h3>$$$","</h3>$$$").replace("$$$</h3>","</h3>")
    
    cleanlist = cleanlist.split("$$$")
    
####################### FINDS EMAILS CHECKS FOR WEB & ADRESSES PHONE NUMBERS ############################################
#########################################################################################################################
    for i in cleanlist:
      
      Occurence_count1 = i.count(".")
      Occurence_count2 = i.count("@")
      Occurence_count3 = i.count("-")
      Occurence_count4 = i.count("/")
      Occurence_count5 = i.count("<")
      Occurence_count6 = i.count(">")
      Occurence_count7 = i.count("<!")
      Occurence_count8 = i.count("=")
      Occurence_count9 = i.count("clientproxy") #DELETE on new version
      Occurence_count10 = i.count("forefront") #DELETE on new version
     
      if Occurence_count1 > 3:
            del i
      elif Occurence_count2 > 0:
            del i
      elif Occurence_count3 > 2:
            del i
      elif Occurence_count4 > 0:
            del i
      elif Occurence_count5 == 1:
            del i
      elif Occurence_count6 == 1:
            del i
      elif Occurence_count7 == 1:
            del i
      elif Occurence_count8 == 1:
            del i
      elif Occurence_count9 == 1:
            del i
      elif Occurence_count10 == 1:
            del i
            
    cleanlist2 = ""
  
########################## CHECKS TO SEE IF HTML OR SENTENCE OR OTHER OCCURENCE #################################  
#########################################################################################################################  
  
    substring = "<"
    substring2 = "."
    substring3 = "!"
    substring4 = "?"
    substring5 = "-"
    substring6 = ":"
    substring7 = "<p>"
    substring8 = "</p>"
    substring9 = "<h3>"
    substring10 = "</h3>"
    substring10 = "<h2>"
    substring10 = "</h2>"

    newray = ""

    for i in cleanlist:
        if substring in i:
            if substring7 in i or substring8 in i or substring9 in i or substring10 in i:
                newray+=i
            else:
                del i
        elif substring2 in i : 
            newray+=i
        elif substring3 in i : 
            newray+=i
        elif substring4 in i : 
            newray+=i
        #elif substring5 in i : 
            #newray+=i
        elif substring6 in i : 
            newray+=i
        #elif len(i) <= 10 and len(i) >= 4:  #### NEW ADDITION BEWARE
            #newray+=i
        else:
            i = ""
            newray+=i

#########################################################################################################################       
  ####################################### REPLACEMENT PATTERNS 1 ########################################################                  
        
    fixed = newray
    #########################print("hello")
    
    
    fixed = fixed.replace("<h1>", "<h3>").replace("<h2>", "<h3>").replace("</h2>","</h3>").replace("<br>", "").replace("</h1>","</h3>").replace("<h4>","<h3>").replace("</h4>","</h3>").replace("<ul>", "").replace("</ul>", "").replace("<ol>", "").replace(
        "<p></p>", "").replace("</ol>", "").replace("<li>", "<p>").replace("</li>", "</p>").replace("<h3></h3>", "").replace("<p> </p>", "").replace("<p></p>", "").replace("<h2></h2>", "").replace("<strong>", "").replace("</strong>", "").replace("</p></p>", "</p>").replace("</p></p>", "</p>").replace("</p></p>", "</p>").replace("</p></h3>", "</p>").replace("</p></p>", "</p>").replace("<p></p>", "")
    
    
########################################################################################################################
  ####################################### FIND IF EXACT DUPES WORDS NEXT TO ONE ANOTHER ################################
    
    
    final = fixed.split()
  
    p = None
    o = []
    for n in final:
        if n == p:
            continue
        o.append(n)
        p = n 

    final = ' '.join(o)
    ####################print(final)
    
    
    ###################### NEW CHANGES FROM HERE PETE ###################### 18/04/2022
    final = final.replace("<h3>","$$$<h3>").replace("</h3>","</h3>$$$").replace("<p>","$$$<p>").replace("</p>","</p>$$$")
    
    final = final.split("$$$")
    
    substringID1 = "<p>"
    substringID2 = "."
    substringID3 = "<"
    substringID4 = "!"
    substringID5 = "?"
    substringID6 = ":"
    substringID7 = "-"
    #Less destructive way to find incomplete generations & Delete short bullet points 
    removed_short_p = ""
    for i in final:
        if substringID1 in i:
            if len(i.split(" ")) < 15: #ADD RULE HERE- GREMLINS
                del i
            else:
                removed_short_p += i    
        else:
            removed_short_p += i  
    
    final = removed_short_p
    
    final = final.replace("<h3>","$$$<h3>").replace("</h3>","</h3>$$$").replace("<p>","$$$<p>").replace("</p>","</p>$$$")
    final = final.split("$$$")
    
    newtestx = ""
    for i in final:
        #(i)
        if substringID1 in i:
                z = i.replace(".",".$$$").replace("!","!$$$").replace("?","?$$$").replace("<p>","$$$<p>$$$").replace("</p>","$$$</p>")
                z = z.split("$$$")
    
                if len(z) > 5:
                    for x in z:
                        if substringID2 in x or substringID3 in x or substringID4 in x or substringID5 in x or x == " " or substringID6 in x or substringID7 in x :
                            xxx = ""
                        else:
                            i = i.replace(x,"")
        newtestx += i
                          
    final = newtestx
    final = final.replace("<h3>","$$$<h3>").replace("</h3>","</h3>$$$")
    
    Check_4_ptag = "<p>"
    final = final.split("$$$")
    
    newtestx2 = ""
    for i in final:
        if Check_4_ptag in i:
            x = i.replace("<p>","$$$<p>").replace("</p>","</p>$$$").split("$$$")
            if len(x) > 6:
                x = x[:20]
                x = "".join(x)
                i = x
                
                newtestx2 += i
            else:
                newtestx2+= i
        else:
            newtestx2 += i
 
    final = newtestx2

    final = final.replace(",",",$$$")
    final = final.split("$$$")
    
    p = None
    o = []
    for n in final:
        if n == p:
            continue
        o.append(n)
        p = n 

    final = ' '.join(o) 
    
    final = final.replace("<p>","<p> ").replace("<","$$$<").replace(">",">$$$").replace(".",".$$$").replace("!","!$$$").replace("?","?$$$")
    final = final.split("$$$")

    p = None
    o = []
    for n in final:
        if n == p:
            continue
        o.append(n)
        p = n 
    
    final = ''.join(o)
    
    final = final.replace("<p>","<p> ").replace("<","$$$<").replace(">",">$$$").replace(".",".$$$").replace("!","!$$$").replace("?","?$$$")
    final = final.split("$$$")
    
    final = "".join(final)
    final = final.replace("  "," ").replace("<","$$$<").replace(">",">$$$").replace(".",".$$$").replace("!","!$$$").replace("?","?$$$").replace("$$$<h3>$$$","$$$<h3>").replace("$$$</h3>$$$","</h3>$$$")
    final = final.split("$$$")
    substring1 = "<"
    substring2 = " "
    
    finalnew = ""
    for i in final:
        if substring1 not in i and substring2 not in i:
            del i
        else:
            finalnew+= i
            
#########################################################################################################################  
########################################## TO find last words not in html ###############################################
    
    substring1 = "<"
    substring2 = ">"
    final = finalnew.replace("<","$$$<").replace(">",">$$$").replace("<h2>$$$","<h2>").replace("<h3>$$$","<h3>").replace("<p>$$$","<p>").replace("$$$</h2>","</h2>").replace("$$$</h3>","</h3>").replace("$$$</p>","</p>")
    final = final.split("$$$")
    if substring1 not in final[-1] and substring2 not in final[-1]:
        del final[-1]
    final = "".join(final)
    
  #########################################################################################################################  
    ########################################## REPLACEMENT PATTERNS 1######################################################
    
    final = final.replace("</h3><p><h3>","</h3><h3>").replace("<", "$$$<").replace(">", ">$$$")#.replace(".", ".$$$").replace("?", "?$$$").replace("!", "!$$$")
    final = final.replace("<p> </p>","<p></p>").replace("</p><p>","").replace("</h3> <h3>","</h3><h3>").replace("$$$<h3>$$$","$$$<h3>").replace("$$$</h3>$$$","</h3>$$$").replace("</h3>$$$$$$<h3>","</h3><h3>").replace("$$$</h3>","</h3>")
    
    ########################################################################################################################
    ####################################### PATTERN TO GET RID OF EMPTY H3 HEADINGS ########################################
    
    newray = final.split("$$$")
    
    newray = [x for x in newray if x != '']
    
    newrayX = ""
    substring = "<h3>"
    for i in newray:
        if substring in i:
            if i.count("h3") < 2:
                del i
                continue
            elif i.count("h3") == 2:
                if Term.lower()[-1] == "s" or "with" not in Term.lower() or Term.lower()[-2] != "a" or Term.lower()[-2] != "i" or Term.lower()[-2] != "o" or Term.lower()[-2] != "u":
                    i = i.lower()
                    ##############print(Term.lower()[-1])
                    ##############print(i)
                    
                    i = i.replace("what is a ","what are ").replace("who needs a ","who needs ").replace("the importance of purchasing a quality ","the importance of purchasing quality ").replace("features to consider when buying a ","features to consider when buying ").replace("why should i buy a ","why should i buy ").replace("how do you use a ","how do you use ")
                    i = i.title().replace("H3","h3")
                    ##############print(i)
                else:
                    i = i.title().replace("H3","h3")
        i = i.replace("</h3> <h3>","</h3><h3>").replace("</h3>  <h3>","</h3><h3>").replace("</h3><h3>","</h3>$$$<h3>").replace("</h3> <h3>","</h3>$$$<h3>")
        i = i.split("$$$")
        
        i = i[-1]
        
        newrayX+= i
    
    newrayX  = newrayX .replace("</h3><p><h3>","</h3><h3>").replace("<", "$$$<").replace(">", ">$$$")#.replace(".", ".$$$").replace("?", "?$$$").replace("!", "!$$$")
    newrayX  = newrayX .replace("<p> </p>","<p></p>").replace("</p><p>","").replace("</h3> <h3>","</h3><h3>").replace("$$$<h3>$$$","$$$<h3>").replace("$$$</h3>$$$","</h3>$$$").replace("</h3>$$$$$$<h3>","</h3><h3>").replace("$$$</h3>","</h3>").replace("</h3>$$$ $$$<h3>","</h3><h3>")
    
    newray = newrayX.split("$$$")
    ########################print(newray)
    newray = [x for x in newray if x != '']
    
    newrayX2 = ""
    substring = "<h3>"
    for i in newray:
        if substring in i:
            if i.count("h3") < 2:
                del i
                continue
            else:
                i = i
        i = i.replace("</h3> <h3>","</h3><h3>").replace("</h3>  <h3>","</h3><h3>").replace("</h3><h3>","</h3>$$$<h3>").replace("</h3> <h3>","</h3>$$$<h3>")
        i = i.split("$$$")
        
        i = i[-1]
        newrayX2+= i
    #########################################################################################################################
    ########################################## REPLACEMENT PATTERNS 1########################################################
    
    final2 = newrayX2.replace(">H3<","><").replace("</h3></h3>","").replace("</h></p>","").replace("</h3></p>","</h3>").replace("<h4></h4>","")
    
    blog = heading + final2
    
    
    final2 = final2.replace("<","$$$<").replace(">",">$$$").replace("<","$$$<").replace(">",">$$$").split("$$$")
    
    testray = []
    
    for i in final2:
        sep = 'Eleventh'
        stripped = i.split(sep, 1)[0]
        testray.append(stripped)
        
    final2 = "".join(testray)

    #Normalize Whitespace

    final2 = final2.replace("<","$$$<").replace(">",">$$$").replace("<","$$$<").replace(">",">$$$").replace("$$$</h3>$$$","</h3>$$$").replace("$$$<h3>$$$","$$$<h3>").replace("<h3>$$$","$$$<h3>").replace("$$$</h3>","</h3>").replace("<em>","").replace("</em>","").replace("</p></p></p>","</p>").replace("</p></p>","</p>").replace("<p  ","").replace("câ€™","'").replace("â€³",'"')
    final2 = final2.split("$$$")
    final2  = [x for x in final2 if x != '']
    
     ########################################################################################################################
    ########################################## DROP WHOLE BLOG IF THESE OCCURENCES FOUND ####################################
    
    substringfinalh3 = "h3"
    
    try:
        if substringfinalh3 in final2[-1]:
            del final2[-1]
    except:
        pass
        
    final2 = "".join(final2)
    blog = final2.replace("<h3><p>",'</h3><p>').replace("<p  ","").replace("<p  ","").replace("/ul&gt;","").replace("&nbsp;","").replace("<p> </p>","").replace("<p></p>","").replace("< ","").replace(" >","").replace('<h3="""">',"")
    final = blog.replace("</h3><p><h3>","</h3><h3>").replace("<", "$$$<").replace(">", ">$$$")#.replace(".", ".$$$").replace("?", "?$$$").replace("!", "!$$$")
    final = final.replace("<p> </p>","<p></p>").replace("<p></p>","").replace("</h3> <h3>","</h3><h3>").replace("$$$<h3>$$$","$$$<h3>").replace("$$$</h3>$$$","</h3>$$$").replace("</h3>$$$$$$<h3>","</h3><h3>").replace("$$$</h3>","</h3>") ###FIRST CHANGE 04/05/2022
    
    newray = final.split("$$$")
    
    newray = [x for x in newray if x != '']
    
    newrayX = ""
    substring = "<h3>"
    for i in newray:
        if substring in i:
            if i.count("h3") < 2:
                del i
                continue
            else:
                i = i
        i = i.replace("</h3> <h3>","</h3><h3>").replace("</h3>  <h3>","</h3><h3>").replace("</h3><h3>","</h3>$$$<h3>").replace("</h3> <h3>","</h3>$$$<h3>").replace('""','"')
        i = i.split("$$$")
        i = i[-1]
        newrayX+= i
  
    blog = newrayX 
    blog = blog.replace("<p> ","<p>")
    
#######################################################

    ########print(ray1)
    blog = blog.replace('""','"').replace("''","'").replace("</p> .","</p>").replace("</p>.</p>","</p>")
    
    
    substringptester1 = "<h3>"
    substringptester2 = "</h3>"
    blog = blog.replace("<p>","$$$<p>$$$").replace("</p>","$$$</p>$$$").split("$$$")
    blog = [x for x in blog if x != '']
   
    
    
    #stop forever fullstops - bad generation vibes
    
    blog_list2 = []
    for i in blog:
        if substringptester1 not in i:
            ##print(i)
            x = i.replace("<p>","").replace("</p>","").replace(". ",". $$$")
            x = x.split("$$$")
            x = [x for x in x if x != '']
            if len(x) > 10:
                #print(x)
                #print(ID)
                x = x[0:10]
                x = "".join(x)
                i = f"{x}"
            else:
                i = i
        
        blog_list2.append(i)
    
        
        
    blog =  "".join(blog_list2)
    blog = heading + blog.replace('""','"') ########################print(blog)
    blog = blog.replace("<p> ","<p>").replace("'S","'s")
    wordcount = int(len(blog.split()))
    ##print(blog)
    ##########print(blog)
    ##########print(wordcount)
    
    ############################################################################################################################
    ########################################## DROP WHOLE BLOG IF LESS THAN 800 WORDS ##########################################
    
    if wordcount < 900:
        leftoverKeywords.append(Term)
        leftoverID.append(ID)
        continue
    else:
        
        wordcount = wordcount
    #Word_count_intro = len(Introduction.split())
    ###############print(blog)
    ID_list.append(ID)
    term_list.append(Term)
    #intro_list.append(Introduction)
    blog_list.append(blog)
    #intro_wordcount.append(Word_count_intro)
    blog_wordcount.append(wordcount)
    
    # BLACKLIST
ID = pd.DataFrame(ID_list,
                     columns = ['keyword_id'])

t = pd.DataFrame(term_list,
                     columns = ['keyword']) 

i = pd.DataFrame(intro_list,
                     columns = ['intro']) 

b = pd.DataFrame(blog_list,
                     columns = ['guide']) 




#iw = pd.DataFrame(intro_wordcount,
                     #columns = ['intro_wordcount']) 

bw = pd.DataFrame(blog_wordcount,
                     columns = ['guide_wordcount']) 




  
  
test1 = pd.concat([ID,t,b,bw], axis=1, join="inner")

test1.to_csv(r"EXPORT/compulsive_bg_post.csv")
leftoverID_df = pd.DataFrame(leftoverID,columns = ['ID']) 
leftoverKW_df = pd.DataFrame(leftoverKeywords,columns = ['TERM']) 
test2 = pd.concat([leftoverID_df,leftoverKW_df], axis=1, join="inner")
test2.to_csv(f"LEFTOVERS/compulsive_bg_leftovers.csv")