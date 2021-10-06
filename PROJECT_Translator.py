from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from speech_recognition import Recognizer,Microphone,UnknownValueError
from googletrans import Translator
from textblob import TextBlob
#NEW FEATURES
from gtts import gTTS
import playsound
import os

#speech reconition
r=Recognizer()
def record_audio():
    with Microphone() as source:
        print('Speak Now')
        #Feature controls noice
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio=r.listen(source)
    try:
        #speech to text
        voice_data=r.recognize_google(audio)
        print(voice_data)
        data1.set(voice_data)
        word=TextBlob(voice_data)
        lang=word.detect_language()
        l1.set(get_key(lang))
    except UnknownValueError:
        data2.set('sorry, I did not get that')
#Translation
def trans():
    translator = Translator()
    word=TextBlob(data1.get())
    lang=word.detect_language()
    l1.set(get_key(lang))
    translated = translator.translate(word,src=select1.get(),dest=select2.get())
    data2.set(translated.text)
    #New Feature More Language TRanslation
    if(select3.get()=='select-language'):
        data3.set('Select Language')
    else:
        translated2 = translator.translate(word,src=select1.get(),dest=select3.get())
        data3.set(translated2.text)
    if(select4.get()=='select-language'):
        data4.set('Select Language')
    else:
        translated3 = translator.translate(word,src=select1.get(),dest=select4.get())
        data4.set(translated3.text)

#SPEAK BUTTON
def speakop2():
    print(data2.get())
    output1=gTTS(text=data2.get(),lang=get_val(select2.get()),slow=False)
    output1.save("output1.mp3")
    playsound.playsound("output1.mp3")
    os.remove("output1.mp3")
def speakop3():
    print(data3.get())
    output2=gTTS(text=data3.get(),lang=get_val(select3.get()),slow=False)
    output2.save("output2.mp3")
    playsound.playsound("output2.mp3")
    os.remove("output2.mp3")
def speakop4():
    print(data4.get())
    output3=gTTS(text=data4.get(),lang=get_val(select4.get()),slow=False)
    output3.save("output3.mp3")
    playsound.playsound("output3.mp3")
    os.remove("output3.mp3")
#EXIT BUTTON
def main_exit():
    p=messagebox.askyesnocancel('Notification','Are you want to exit !',parent=app)
    if(p==True):
        app.destroy()
def get_key(lang):
    for key, value in LANGUAGES.items(): 
        if lang == value: 
            return key
def get_val(lang):
    for key, value in LANGUAGES.items(): 
        if lang == key: 
            return value

#GUI
app=Tk()
app.geometry('650x500')
app.title('VHV Translator')
appName=Label(app,text='VHV Translator',font=('times',22,'bold')
				,bg='green',fg='goldenrod1',height=2)
appName.pack(side=TOP,fill=BOTH,pady=0)
app.config(bg='light blue')
app.iconbitmap('Translate.ico')

#ENTRYS
data1=StringVar()
data2=StringVar()
data3=StringVar()
data4=StringVar()
entry1=Entry(app,width=40,textvariable=data1,font=('times',16))
entry1.place(x=150,y=100,height=30)

entry2=Entry(app,width=40,textvariable=data2,font=('times',16))
entry2.place(x=150,y=170,height=30)

entry3=Entry(app,width=40,textvariable=data3,font=('times',16))
entry3.place(x=150,y=240,height=30)

entry4=Entry(app,width=40,textvariable=data4,font=('times',16))
entry4.place(x=150,y=310,height=30)

#LABELS
label1=Label(app,text='RECORDED :',font=('times',13,'bold'),bg='light blue')
label1.place(x=10,y=100)

label2=Label(app,text='TRANSLATED1 :',font=('times',13,'bold'),bg='light blue')
label2.place(x=10,y=170)
label4=Label(app,text='TRANSLATED2 :',font=('times',13,'bold'),bg='light blue')
label4.place(x=10,y=240)
label5=Label(app,text='TRANSLATED3 :',font=('times',13,'bold'),bg='light blue')
label5.place(x=10,y=310)
#label3=Label(app,text='TO',font=('times',13,'bold'),bg='light blue')
#label3.place(x=238,y=78)

#BUTTTONS
imagbt1=PhotoImage(file='mic.png')
imagbt2=PhotoImage(file='logout.png')
imagbt3=PhotoImage(file='touch.png')
imagbt4=PhotoImage(file='speaker.png')

imagbt1=imagbt1.subsample(16,16)
imagbt2=imagbt2.subsample(16,16)
imagbt3=imagbt3.subsample(16,16)
imagbt4=imagbt4.subsample(32,32)

btn1=Button(app,text='MIC',bd=10,bg='limegreen',activebackground='darkgreen',width=110,font=('times',15,'bold'),image=imagbt1,compound=RIGHT,command=record_audio)
btn1.place(x=100,y=380)

btn2=Button(app,text='Exit',bd=10,bg='orangered',activebackground='red',width=110,font=('times',15,'bold'),image=imagbt2,compound=RIGHT,command=main_exit)
btn2.place(x=410,y=380)

btn3=Button(app,text='Translate',bd=10,bg='gold',activebackground='yellow',width=110,font=('times',15,'bold'),image=imagbt3,compound=RIGHT,command=trans)
btn3.place(x=255,y=380)

btn4=Button(app,text='',bd=5,bg='darkgreen',activebackground='lawngreen',width=30,font=('times',10,'bold'),image=imagbt4,compound=RIGHT,command=speakop2)
btn4.place(x=600,y=170)
btn5=Button(app,text='',bd=5,bg='darkgreen',activebackground='lawngreen',width=30,font=('times',10,'bold'),image=imagbt4,compound=RIGHT,command=speakop3)
btn5.place(x=600,y=240)
btn6=Button(app,text='',bd=5,bg='darkgreen',activebackground='lawngreen',width=30,font=('times',10,'bold'),image=imagbt4,compound=RIGHT,command=speakop4)
btn6.place(x=600,y=310)

#COMBO BOXS 
l1=StringVar()
l2=StringVar()
l3=StringVar()
l4=StringVar()

LANGUAGES={'detect-language':'vhv','select-language':'slv','afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 
'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
langs=list(LANGUAGES.keys())

select1=Combobox(app,width=23,textvariable=l1,state='writeonly')
select1['values']=[e for e in langs]
select1.place(x=434,y=80)
select1.current(0)

select2=Combobox(app,width=23,textvariable=l2,state='readonly')
select2['values']=[e for e in langs]
select2.current(39)
select2.place(x=434,y=150)

select3=Combobox(app,width=23,textvariable=l3,state='readonly')
select3['values']=[e for e in langs]
select3.current(1)
select3.place(x=434,y=220)

select4=Combobox(app,width=23,textvariable=l4,state='readonly')
select4['values']=[e for e in langs]
select4.current(1)
select4.place(x=434,y=290)

app.mainloop()