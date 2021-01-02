import requests
from lxml import html
import os
etree=html.etree
headers={ "User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
url="http://www.jinyongwang.com/book/"
res=requests.get(url,headers=headers)
result=res.content.decode("utf8")
html_result=etree.HTML(result)
h2s=html_result.xpath("//h2[@class='bookname']/span[contains(text(),'修订版')]")[0]
ul=h2s.xpath("../following-sibling::ul[1]/li")
for li in ul:
    p_title=li.xpath("./p[@class='title']/a/text()")[0]
    p_href=li.xpath("./p[@class='title']/a/@href")[0]
    os.makedirs("./book/"+str(p_title))
    url2="http://www.jinyongwang.com"+p_href
    print(url2)
    res2=requests.get(url2,headers=headers)
    result2=res2.content.decode("utf8")
    html_result2=etree.HTML(result2)
    lis=html_result2.xpath("//ul[@class='mlist']/li")
    for li_text in lis:
        sub_title=li_text.xpath("./a/text()")[0]
        print(sub_title)
        sub_href=li_text.xpath("./a/@href")[0]
        print("http://www.jinyongwang.com"+sub_href)
        res3=requests.get("http://www.jinyongwang.com"+sub_href,headers=headers)
        result3=res3.content.decode("utf8")
        with open("test.html","w",encoding="utf8") as f:
            f.write(result3)
        html_result3=etree.HTML(result3)
        result_content=html_result3.xpath("//div[@class='vcon']")[0]
        print(result_content)
        ps=result_content.xpath("./p/text()")
        str_content=""
        for p1 in ps:
            str_content+=p1+"\n"
        with open("book/"+str(p_title)+"/"+str(sub_title)+".txt","w",encoding="utf8") as f:
            f.write(str_content)

    #hrefs=li.xpath("//p[@class='title']/a/@href")
    #print(hrefs)