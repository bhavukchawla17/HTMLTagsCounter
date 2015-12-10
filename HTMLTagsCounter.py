from tkinter import *
from bs4 import BeautifulSoup
import urllib.request
root=Tk()
root.resizable(width=FALSE, height=FALSE)
root.wm_title("HTML Tags Counter")
urlLabel = Label(root,text="URL : ")
urlLabel.grid(row=0,column=0,sticky="E",padx=(5,5),pady=(5,0))
urlBox = Entry(root,width=40)
urlBox.insert(0,"http://")
urlBox.grid(row=0,column=1,padx=(5,5),pady=(5,0))
taglabel = Label(root,text="Tag Name : ")
taglabel.grid(row=1,column=0,sticky="E",padx=(5,5))
tagBox = Entry(width=40)
tagBox.grid(row=1,column=1,padx=(5,5))
countLabel = Label(root,text="Count : ")
countLabel.grid(row=2,column=0,sticky="E",padx=(5,5))
countBox = Label(root,text="                                                                                ",bd=1,relief=SUNKEN)
countBox.grid(row=2,column=1,padx=(5,5))

def updateStatus(str):
    status.config(text=str)


def submit():
    url = urlBox.get()
    flag=1
    if(len(url)==0):
        updateStatus("Please enter a Url.")
    else:
        try:
            html=urllib.request.urlopen(url).read()
            updateStatus("Connected.")
        except:
            flag=0
            updateStatus("Sorry can't fetch data from this page. Try another one.")
        if flag==1:
            try:
                data=html.decode("utf-8")
                data='""" '+ data + ' """'
                soup=BeautifulSoup(data,"html.parser")
                tagname = tagBox.get()
                if len(tagname)==0:
                    updateStatus("Please enter a tagname.")
                else:
                    NoTag=soup.find_all(tagname)
                    countBox.config(text=str(len(NoTag)))
                    updateStatus("Done")
            except:
                updateStatus("Sorry can't fetch data from this page. Try another one.")

            
button = Button(None,text="Submit",command=submit)
button.grid(columnspan=2,pady=(5,5))

status = Label(root,text="Status..",bd=1,relief=SUNKEN)
status.grid(columnspan=2,sticky="E")
root.mainloop()

