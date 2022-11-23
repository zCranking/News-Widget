from tkinter import *
from tkinter import ttk
import requests
import json

root = Tk()
root.title("News Widget")
root.geometry("800x600")

newsupdate = Label(root, text="Fox News Update", font=("Helvetica", 25,'bold'))
newsupdate.place(relx=0.5, rely=0.05, anchor=CENTER)

"""set1"""
title1 = Label(root, text="", fg ="red", font=("Helvetica",18, 'bold'), wraplength=500)
title1.place(relx=0.5, rely=0.15, anchor=CENTER)

text1 = Label(root, text="", fg ="black", font=("Helvetica",13, 'normal'), wraplength=500)
text1.place(relx=0.5, rely=0.25, anchor=CENTER)

"""set 2"""
title2 = Label(root, text="", fg ="red", font=("Helvetica",18, 'bold'), wraplength=500)
title2.place(relx=0.5, rely=0.45, anchor=CENTER)

text2 = Label(root, text="", fg ="black", font=("Helvetica",13, 'normal'), wraplength=500)
text2.place(relx=0.5, rely=0.55, anchor=CENTER)

"""set 3"""
title3 = Label(root, text="", fg ="red", font=("Helvetica",18, 'bold'), wraplength=500)
title3.place(relx=0.5, rely=0.75, anchor=CENTER)

text3 = Label(root, text="", fg ="black", font=("Helvetica",13, 'normal'), wraplength=500)
text3.place(relx=0.5, rely=0.85, anchor=CENTER)

therequest = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=7a780f76493c41369b165c39eb6ee2b5")
bbcpage = json.loads(therequest.content)

title1['text'] = bbcpage["articles"][0]["title"]
text1['text'] = bbcpage["articles"][0]["title"]

title2['text'] = bbcpage["articles"][1]["title"]
text2['text'] = bbcpage["articles"][1]["title"]

title3['text'] = bbcpage["articles"][2]["title"]
text3['text'] = bbcpage["articles"][2]["title"]

root.overrideredirect(True)
root.mainloop()