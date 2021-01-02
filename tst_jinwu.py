import requests
from lxml import html
etree=html.etree
headers={ "User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
res=requests.get("http://www.jinyongwang.com/data/wugong/",headers=headers)
result=res.content.decode("utf8")
html1=etree.HTML(result)
novels=html1.xpath("//h2[@class='dataname']")
for novel in novels:
    title=novel.xpath("./span/text()")[0]
    datas=novel.xpath("./following-sibling::div[1]")
    for data in datas:
        names= data.xpath("./a/text()")
        for name in names:
            with open('wugong/' + title + ".txt", "a", encoding="utf8") as f:
                f.write(name+"\n")
