import deepcut
from nltk import word_tokenize as eng_tokens
from pythainlp.corpus import stopwords as thaisw
from nltk.corpus import stopwords as engsw
import pandas as pd

#dfList=dfIn['Comment'].values.tolist()
#print(' len => ',len(dfList))

def CommentCut(dfList):

    Outcome=[]
    for r in dfList:
        Dummy=[]
        tokens=[]
        tokens=list(eng_tokens(r))
        lowered = [t.lower() for t in tokens]
        #print(' Dummy : ',lowered)
        lowered=" ".join(lowered)

        #print(lowered)
           
        ### Custom Deepcut Tokenize
        Dummy=deepcut.tokenize(lowered,custom_dict=[u'ข้าวมันไก่',u'การบินไทย',u'ข้าวตัมบาทเดียว',u'สถานีรถไฟ',u'วังน้อย',u'โอกาส',u'สิบทิศ',u'สนับสนุน'])
            
        print(' Dummy 2 : ',Dummy)
        Outcome.append(Dummy)


    ThaiWord=list(thaisw.words('thai'))
    #print(' tw : ',ThaiWord)
    EngWord=list(set(engsw.words('english')))
    #print(' ew : ',EngWord, ' : ', type(EngWord))    
    Morewords=[u'การ',u'การทำงาน',u'ทำงาน',u'เสมอ',u'krub',u'Test', u'nan',u'test',u'.',u'ท่าน',
                    u',',u'ดัน',u'ทำ',u'มือ',u'ลัก',u'พ',u'งาน',u'ดี',u'กา',u'/',u'\u200b',u')',u'(',u'จ้อ',
                    u'< /p >', u'< /p > ',u'< p >',u' < p >',u'< p > ',u'< br >',u'< br > ',u'< br > & ', u'< br > &',u'nbsp',u'สถาน',u'ประกอบ'
                    u'ผู้',u'เดินทาง',u'ตรงข้าม',u'ที่', u'นั่ง', u'เดิน', u'ทาง', u'สาย',u'บิน',u'หน้า',u'ทาง',u'บวช',u'ศพ',u'บ้านเลข',u'บ้าน',u'เลข']                                    
    All_Stop_Word=ThaiWord+EngWord+Morewords

    NoStop=[]
    Dummy2=[]
    for k in Outcome:
        Dummy=[]
        Dummy=[word for word in k if word not in All_Stop_Word]
        Dummy2.append("".join(Dummy))
        NoStop.append(Dummy)

    print(' ==>',Dummy2, ' == > ',len(Dummy2))
    return Dummy2
