import os
mypersons=os.listdir("renwu")
person_list={}
persons=[]
for person in mypersons:
    with open("renwu/"+person,"r",encoding="utf8") as f:
        for line in f.readlines():
            if  person_list.get(line) is None:
                name_line=line.strip()
                person_list[name_line]={}
                persons.append(name_line)
mylist=os.listdir("book")
for mydir in mylist:
    mybooks=os.listdir("book/"+mydir)
    for mybook in mybooks:
        print(mybook)
        with open("book/"+mydir+"/"+mybook,"r",encoding="utf8") as f:
            for line in f.readlines():
                for name1 in persons:
                    for name2 in persons:
                        if line.find(name1)>=0 and line.find(name2)>=0:
                            if name1==name2:
                                continue
                            if person_list[name1].get(name2) is None:
                                person_list[name1][name2]=1
                            else:
                                person_list[name1][name2]+=1
with open('person_list.json',"w",encoding="utf8") as f:
    f.write(str(person_list))