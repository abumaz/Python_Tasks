import requests, bs4, csv

def adder(li):
    global nos
    res = requests.get(li)
    res.raise_for_status()
    texts = bs4.BeautifulSoup(res.text)
    l=texts.getText().split("\n")
    t=[]
    for chunk in l:
        if chunk=='\n' or chunk=='':
            continue
        t.append(chunk)
    with open('new_quotes.csv','a') as new:
        new_write=csv.writer(new)
        for i in range(74,220,6):
            if len(t[i].split())==1:
                i+=1
            temp=[t[i],t[i+1],[t[i+2],t[i+3],t[i+4],t[i+5]]]
            new_write.writerow(temp)
            nos+=1
'''
with open('new_quotes.csv','r') as printing:
    printer=csv.reader(printing)
    for i in printer:
        print(i)
'''

nos=0
lno=0
links=['https://www.brainyquote.com/topics/motivational-quotes','https://www.brainyquote.com/topics/attitude-quotes','https://www.brainyquote.com/topics/positive-quotes','https://www.brainyquote.com/topics/inspirational-quotes','https://www.brainyquote.com/topics/life-quotes','https://www.brainyquote.com/topics/smile-quotes','https://www.brainyquote.com/topics/friendship-quotes','https://www.brainyquote.com/topics/nature-quotes','https://www.brainyquote.com/topics/education-quotes']
while (nos<500 and lno<9):
    adder(links[lno])
    lno+=1
        