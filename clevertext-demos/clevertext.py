from bs4 import BeautifulSoup

def delete_dupe_sentences(blog):
    blog_newlist = ["",""]
    blog = blog.replace("<","$$$<").replace(">",">$$$").replace(". <",".<").replace(".<",". $$$<").replace(". A",". $$$A").replace(". B",". $$$B").replace(". C",". $$$C").replace(". D",". $$$D").replace(". E",". $$$E").replace(". F",". $$$F").replace(". G",". $$$G").replace(". H",". $$$H").replace(". I",". $$$I").replace(". J",". $$$J").replace(". K",". $$$K").replace(". L",". $$$L").replace(". M",". $$$M").replace(". N",". $$$N").replace(". O",". $$$O").replace(". P",". $$$P").replace(". Q",". $$$Q").replace(". R",". $$$R").replace(". S",". $$$S").replace(". T",". $$$T").replace(". U",". $$$U").replace(". V",". $$$V").replace(". W",". $$$W").replace(". X",". $$$X").replace(". Y",". $$$Y").replace(". Z",". $$$Z").split("$$$")
    tag_id = "<"
    blog = [x for x in blog if x != '']
    blog = [x for x in blog if x != '\n']
    
    list_no_dupes_check = []
    for i in blog:  ######print(i)
        if tag_id not in i:
            #####print(i)
            if i[0] == " ":
                i = i[1:-1]
            list_no_dupes_check.append(i)  
        x = list_no_dupes_check.count(i)
        #####print(x)
        if x > 1:
                ####print(f"{ID} -WORKING - {i}")
                i = ""
        blog_newlist.append(i)
        final = "".join(blog_newlist)
        return final
        ######print(list_no_dupes_che
         
def soup_clean(blog):
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
    blog = ''.join([str(tag) for tag in soupfinal])
    return blog
    
    
def header_fix_normalize_htags(blog):
    pre2 = blog.replace("</h2>","</h2>$$").replace("<html><body>","").replace("<html><body>","").replace("</body></html>","").replace("-->","").replace("<!--","").replace("<h5>","<h3>").replace("</h5>","</h3>").replace("/n","").replace("&lt;","").replace("<h4>;","<h3>").replace("</h4>;","</h3>")
    
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
    return heading

def web_occurence_check(blog):
    blog = blog.replace("<","$$$<").replace(">",">$$$").replace(". ",". $$$").split("$$$")
    cleanlist3 = []
    for i in blog:
      Occurence_count = i.count(".")#Checks fot the occurence of this particular character and sets threshold. if over a certain amount it needs to skip and just use the input as the output. THis is for haandling those rare, repeated phone number outputs we get. 
      Occurence_count2 = i.count("www")
      Occurence_count3 = i.count("/")
      
    if Occurence_count > 2 or Occurence_count2 > 0 :
        i =""
    elif Occurence_count > 0 and Occurence_count3 > 0:
        i = ""
    cleanlist3.append(i)
    blog = "".join(cleanlist3)
    return blog

def black_list(blog):
        newray = blog.replace("<", "$$$<").replace(">", ">$$$").replace(
        ". ", ".$$$ ").replace("?", "?$$$").replace("!", "!$$$")
        newray = newray.split("$$$")
        BLACKLIST = ["Title:","Blog article:","order any of these items","please visit our","Bio:","Tags:","Author:","About us:","Facebook","Instragram","written by","=>","=<",">=","since ancient times","online store","have been around since ancient times","Review","top 10","Published","Copyright","11)","12)","13)","14)",")","15)","16)","17)","18)","19)","20)","21)","22)","23)","24)","25)","26)","27)","28)","29)","30)","31)","32)","33)","34)","35)","36)","37)","38)","39)","40)","41)","42)","43)","44)","45)","46)","47)","48)","49)","50)","51)","52)","53)","54)","55)","56)","57)","58)","59)","Amazon","amazon","Add To Cart","<img>","<a>","1-800","www",'$','http', 'ebay',"Walmart","Ebay","Costco","BestBuy","€","shipping", "costco","PayPal", "paypal", ".biz",  "bestbuy","blog","author","About us","About us","Visit the site","contact us","This website",".org",".com",".biz","Here are two good resources","@",".net","This item includes","best-buy","Specifications", 'email', "call-us","call us","give us a call","Give us a call", " seo " , "we are a ","our website","buy online at","money back guarantee","Final Thoughts", "In Conclusion","Final thoughts", "In conclusion"]

        cleanlist2 = []
        for i in newray:
            for substring in BLACKLIST:
                if substring in i:
                    i = ""
            cleanlist2.append(i)
            blog = "".join(cleanlist2)
            return blog

    
def black_list(blog):
    newray = ""
    cleanlist = blog.replace("<","$$$<").replace(">",">$$$").split("$$$")
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
    return newray