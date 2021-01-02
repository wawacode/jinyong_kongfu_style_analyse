import os
import jieba
from wordcloud import WordCloud
from matplotlib import pyplot
filelist=os.listdir("book/神雕侠侣")
names=[]
with open("renwu/神雕侠侣.txt","r",encoding="utf8") as f:
    with open("renwu1.txt","a",encoding="utf8") as fa:
        for  line in f.readlines():
            line=line.strip()
            print(line)
            fa.write(line+"\t"+"n"+"\t"+"5"+"\n")
            names.append(line)
she_str=""
jieba.load_userdict("renwu1.txt")
for file in filelist:
    print(file)

    with open("book/神雕侠侣/"+file,"r",encoding="utf8") as f:
        for line in f.readlines():
            if line.find("杨过")>=0 and line.find("小龙女")>=0:
                line_str=" ".join(jieba.cut(line))
                she_str+=line_str+" "
print(she_str)
stopwords=[]
with open("stopwords.txt","r",encoding="utf8") as f:
    for line in f.readlines():
        stopwords.append(line)

she_arr=she_str.split(" ")
for she in she_arr:
    if she in stopwords or she in names or len(she)==1 and not '\u4e00' <= she <= '\u9fff':
        she_arr.remove(she)
word_str=""
for she in she_arr:
    word_str+=she+" "
background_img=pyplot.imread("rocket.jpg")
word=WordCloud(
    background_color="white",
    max_font_size=150,
    min_font_size=50,
    max_words=100,
    random_state=50,
    font_path="华康俪金黑W8.TTF",
    mask=background_img
)
print(word_str)
word.generate_from_text(word_str)
word.to_file("杨过小龙女.png")