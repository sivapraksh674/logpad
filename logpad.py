import Tkinter,tkFileDialog
import subprocess
m=Tkinter.Tk()
m.title('LogPad')
filename =""
logarea = Tkinter.Text(m,wrap=Tkinter.WORD,width=200, height= 20)
filepatharea = Tkinter.Text(m,wrap=Tkinter.WORD,width=200, height= 2)
classnamesearch = Tkinter.Text(m,wrap=Tkinter.WORD,width=200, height= 20)


def RunButton():
     global filename
     filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
     filepatharea.delete('1.0', Tkinter.END)
     filepathlabel.config(text = "File Path :")
     filepatharea.insert(Tkinter.INSERT,filename )
     
def RunButton2():
     global filename,logtype,cataegory
     logarea.delete('1.0', Tkinter.END)
     logarealabel.config(text = "Log Area")
     if cataegory.get() :
         if logtype.get() == "all" :
            searchquery = "awk '{ print $6;}' "+ filename +" | sort -u"
         else :
             searchquery = "awk '{ if( $5 == \""+logtype.get()+"\" ) print $6;}' "+ filename +" | sort -u"
     else :
         if logtype.get() == "all" :
            searchquery = "awk '{ print;}' "+ filename +" | sort -u"
         else :
             searchquery = "awk '{ if( $5 == \""+logtype.get()+"\" ) print;}' "+ filename +" | sort -u"
     logarea.insert(Tkinter.INSERT,subprocess.check_output(searchquery,shell=True) )


button = Tkinter.Button(m, text='Select File', bg='green',fg='white', command=RunButton)
button.pack(fill="none")
button2 = Tkinter.Button(m, text='Get Logs', bg='green',fg='white', command=RunButton2)
button2.pack(fill="none")
filepathlabel = Tkinter.Label(m,justify = Tkinter.LEFT)
filepathlabel.pack(anchor=Tkinter.W)
filepatharea.pack(fill="none", expand=Tkinter.TRUE)
cataegory = Tkinter.IntVar()
Tkinter.Checkbutton(m, text="Display Class Name alone", variable=cataegory).pack(anchor=Tkinter.W)
logtype= Tkinter.StringVar()
Tkinter.Radiobutton(m, 
              text="E",
              padx = 20, 
              variable=logtype, 
              value='E').pack(anchor=Tkinter.W)
Tkinter.Radiobutton(m, 
              text="W",
              padx = 20, 
              variable=logtype, 
              value='W').pack(anchor=Tkinter.W)
Tkinter.Radiobutton(m, 
              text="D",
              padx = 20, 
              variable=logtype, 
              value='D').pack(anchor=Tkinter.W)
Tkinter.Radiobutton(m, 
              text="I",
              padx = 20, 
              variable=logtype, 
              value='I').pack(anchor=Tkinter.W)
R1=Tkinter.Radiobutton(m, 
              text="All",
              padx = 20, 
              variable=logtype, 
              value='all')
R1.pack(anchor=Tkinter.W)
R1.select()
logarealabel = Tkinter.Label(m,justify = Tkinter.LEFT)
logarealabel.pack()
logarea.pack(fill="none", expand=Tkinter.TRUE)
m.mainloop()
