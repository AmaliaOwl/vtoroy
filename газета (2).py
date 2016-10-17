import re
import os
import sys
import csv
import urllib.request
import locale
locale.setlocale(locale.LC_ALL, '')


def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        text = page.read().decode('utf-8')
        return text
    except:
        print('Error at', pageUrl)
        return 'Error'

    

commonUrl = 'http://www.kvgazeta.ru/latest-news/'

regPostAutor = re.compile('  <meta name="author" content="(.*?)" />', flags=re.U | re.DOTALL)
regPostHeader = re.compile('  <meta name="title" content="(.*?)" />', flags=re.U | re.DOTALL)
regPostCreated = re.compile('<td valign="top" class="createdate">\n\t\t(.*?)	</td>', flags=re.U | re.DOTALL)
regPostArticle = re.compile('<td valign="top">(.*?)<table align="center" class="pagenav">', flags=re.U | re.DOTALL)


regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)  # это рег. выражение находит все тэги
regScript = re.compile('<script>.*?</script>', flags=re.U | re.DOTALL) # все скрипты
regComment = re.compile('<!--.*?-->', flags=re.U | re.DOTALL)  # все комментарии

#regSlash = re.compile('\n|\r|[|]|]t', flags=re.U | re.DOTALL)  # все комментарии

regSlash = re.compile('\\\\n|\\\\r|\\\\t|\\\\f', flags=re.U | re.DOTALL)  # все 

regStart = re.compile('\[.*?nbsp.*?20\\d\\d', flags=re.U | re.DOTALL)  # все 

regSent = re.compile('Сент', flags=re.U | re.DOTALL)  # все
regJun = re.compile('Июнь', flags=re.U | re.DOTALL)  # все
regJul = re.compile('Июль', flags=re.U | re.DOTALL)  # все
regMar = re.compile('Март', flags=re.U | re.DOTALL)  # все
regNov = re.compile('Нояб.', flags=re.U | re.DOTALL)  # все
regMay = re.compile('Май', flags=re.U | re.DOTALL)  # все

ln=0
lk=0

directory0='D:\\python\\project\\kvgazeta'#com1

directory='D:\\python\\project\\kvgazeta\\plain'  #com1
directory2='D:\\python\\project\\kvgazeta\\mystem-plain'  #com1

directory3='D:\\python\\project\\kvgazeta\\mystem-xml'#com1

os.chdir(directory0)



for i in range(8, 9270):
    directory0='D:\\python\\project\\kvgazeta'#com1 copy
    directory='D:\\python\\project\\kvgazeta\\plain'  #com1 copy
    directory2='D:\\python\\project\\kvgazeta\\mystem-plain'  #com1 copy
    directory3='D:\\python\\project\\kvgazeta\\mystem-xml'#com1 copy

    os.chdir(directory0)


    pageUrl = commonUrl + str(i)
    
    text = download_page(pageUrl)

    if not text=='Error':
    
        Author = regPostAutor.findall(text)
        Author=str(Author)[:-2]
        Author=str(Author)[2:]

        if Author=='':
            Author='Noname'

        #print(Author)

        Header = regPostHeader.findall(text)
        Header=str(Header)[:-2]
        Header=str(Header)[2:]

        #print(Header)

        Created = regPostCreated.findall(text)

        Created = regSent.sub("Сен", str(Created))
        Created = regJun.sub("Июн.", str(Created))
        Created = regJul.sub("Июл.", str(Created))
        Created = regMar.sub("Мар.", str(Created))
        Created = regNov.sub("Ноя.", str(Created))
        Created = regMay.sub("Май.", str(Created))
        if Created == '[]':
            continue
        

        print(Created)

        Year=str(Created)[-6:-2]

        #print(Year)

        from datetime import datetime
        d = datetime.strptime(str(Created), "['%d %b. %Y']")
        dated=d.strftime('%d.%m.%Y')

        #print(dated)

        monthd=d.strftime('%m')

        #print(monthd)
        

        Article = regPostArticle.findall(text)

        c_text = regScript.sub("", str(Article))
        c_text = regComment.sub("", c_text)
        c_text = regTag.sub("", c_text)
        c_text = regSlash.sub("", c_text)
        c_text = regStart.sub("", c_text)

        c_text=str(c_text)[:-2]
        c_text=str(c_text)[2:]
        
        #print(Article)

        #print(c_text)

 
        
        directory=directory+'\\'+str(Year)+'\\'+str(monthd)+'\\'
        directory2=directory2+'\\'+str(Year)+'\\'+str(monthd)+'\\'
        directory3=directory3+'\\'+str(Year)+'\\'+str(monthd)+'\\'

        if not os.path.exists(directory):
            os.makedirs(directory)

        if not os.path.exists(directory2):
            os.makedirs(directory2)

        if not os.path.exists(directory3):
            os.makedirs(directory3)

        c_textrw='@au '+Author+'\n@ti '+Header+'\n@da '+dated+'\n@topic \n@url '+pageUrl+'\n'+c_text
        
        directory=directory

        os.chdir(directory)

        dir_work = os.listdir(directory)            # dir_work получается массивом, хранящим имена файлов 
        numbf = len (dir_work)   

        pfile='статья'+str(numbf+1)+'.txt'

        pfile2='article'+str(numbf+1)+'.txt'

        pfile3='article'+str(numbf+1)+'.xml'

        pfile4='статья'+str(numbf+1)+'.xml'

        if lk==0:
            A = [directory +  pfile,Author,Header,dated,pageUrl,Year]
        else:
            A.append(directory +  pfile)
            A.append(Author)
            A.append(Header)
            A.append(dated)
            A.append(pageUrl)
            A.append(Year)


        #print(A)

        ln=ln+len(c_text)
        lk=lk+1
        print(ln)
        print(lk)
        
        
        f = open(pfile, 'w', encoding = 'utf-8')
        f.write(c_textrw + '\n')
        f.close()

        os.chdir(directory0)

        f = open(pfile2, 'w', encoding = 'utf-8')
        f.write(c_text + '\n')
        f.close()

        print(directory +  pfile)

        print(directory2 +  pfile)



        os.system(r"C:\Users\Samsung\.local\bin\mystem.exe -e UTF-8 -dicg " + directory0 + os.sep +  pfile2 +" "+ directory2 +  pfile2)#com1

        os.system(r"C:\Users\Samsung\.local\bin\mystem.exe -e UTF-8 -dicg --format xml " + directory0 + os.sep +  pfile2 +" "+ directory3 +  pfile3)#com1

        #print(r"C:\Users\Samsung\.local\bin\mystem.exe -e UTF-8 " + directory0 + os.sep +  pfile2 +" "+ directory2 +  pfile2)#com1

        os.rename(directory2 +  pfile2,directory2 +  pfile)

        os.rename(directory3 +  pfile3,directory3 +  pfile4)

        os.remove(directory0 + os.sep +  pfile2)
        if ln >= 150000:
            break


os.chdir(directory0)
fieldnames=['path','author','sex','birthday','header','created','sphere',
            'genre_fi','type','topic','chronotop','style',
            'audience_age','audience_level','audience_size','source',
            'publication','publisher','publ_year',
            'medium','country','region','language']

with open('metadata.csv', 'w') as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()

    for j in range(0, lk):
        writer.writerow({'path':A[6*j+0],'author':A[6*j+1],'header':A[6*j+2],
                         'created':A[6*j+3],'source':A[6*j+4],'publ_year':A[6*j+5],
                         'style':'нейтральный','audience_age':'н-возраст','audience_level':'н-уровень','audience_size':'районная'})
          
    csvfile.close()
