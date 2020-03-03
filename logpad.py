import Tkinter,tkFileDialog
import subprocess
m=Tkinter.Tk()
m.title('LogPad')
filename =""

topframe = Tkinter.Frame(m)
topframe.pack( side = Tkinter.TOP )
bottomframe = Tkinter.Frame(m)
bottomframe.pack( side = Tkinter.BOTTOM )

def RunButton():
     global filename
     filename = tkFileDialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
     filepatharea.delete('1.0', Tkinter.END)
     filepathlabel.config(text = "File Path :")
     filepatharea.insert(Tkinter.INSERT,filename )
     
def RunButton2():
     global filename,logtype,cataegory
     logarea.delete('1.0', Tkinter.END)
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

# Select File action button creation and packing to the view area

button = Tkinter.Button(topframe, text='Select File', bg='green',fg='white', command=RunButton)
button.pack(fill="none")

# Get Logs action button creation and packing to the view area

button2 = Tkinter.Button(topframe, text='Get Logs', bg='green',fg='white', command=RunButton2)
button2.pack(fill="none")

# File Path label creation and packing to the view area

filepathlabel = Tkinter.Label(topframe,justify = Tkinter.LEFT)
filepathlabel.pack(anchor=Tkinter.W)

# File Path packing to the view area

filepatharea = Tkinter.Text(topframe,wrap=Tkinter.WORD,width=200, height= 2)
filepatharea.pack(fill="none", expand=Tkinter.TRUE)

# Search box label creation and packing to the view area

searchboxlabel = Tkinter.Label(topframe,justify = Tkinter.LEFT)
searchboxlabel.pack(side=Tkinter.LEFT)
searchboxlabel.config(text = "Search Area")
 
# Search box text area creation and packing to the view area

searchbox=Tkinter.Text(topframe, height=2, width=50, borderwidth=2, relief=Tkinter.GROOVE)
searchbox.pack(side=Tkinter.LEFT)


# Class name Category selection Check Box creation

cataegory = Tkinter.IntVar()
Tkinter.Checkbutton(topframe, text="Display Class Name alone", variable=cataegory).pack(side=Tkinter.LEFT)


# Logs Type ( E - Error, W - Warning, D - Debug, I - Info, V - Verbose , ALL ) Category selection 
# Radio box creation, packing and default option selection.

logtype= Tkinter.StringVar()
Tkinter.Radiobutton(topframe, 
              text="E",     # E - Error Category Radio Button 
              padx = 20, 
              variable=logtype, 
              value='E').pack(side=Tkinter.LEFT)
Tkinter.Radiobutton(topframe, 
              text="W",     # W - Warning Category Radio Button 
              padx = 20, 
              variable=logtype, 
              value='W').pack(side=Tkinter.LEFT)
Tkinter.Radiobutton(topframe, 
              text="D",     # D - Debug Category Radio Button  
              padx = 20, 
              variable=logtype, 
              value='D').pack(side=Tkinter.LEFT)
Tkinter.Radiobutton(topframe, 
              text="I",     # I - Info Category Radio Button 
              padx = 20, 
              variable=logtype, 
              value='I').pack(side=Tkinter.LEFT)
Tkinter.Radiobutton(topframe, 
              text="V",     # D - Debug Category Radio Button 
              padx = 20, 
              variable=logtype, 
              value='V').pack(side=Tkinter.LEFT)
R1=Tkinter.Radiobutton(topframe, 
              text="All",     # V - Verbose Category Radio Button 
              padx = 20, 
              variable=logtype, 
              value='all')
R1.pack(side=Tkinter.LEFT)
R1.select()


bottomframe = Tkinter.Frame(m)
bottomframe.pack( side = Tkinter.BOTTOM )

# Log Area Label creation and packing to the view area

logarealabel = Tkinter.Label(bottomframe,justify = Tkinter.LEFT)
logarealabel.config(text = "Log Area")
logarealabel.pack(anchor=Tkinter.W)

# Log Area creation and packing to the view area

logarea = Tkinter.Text(bottomframe,wrap=Tkinter.WORD,width=200, height= 20, borderwidth=2, relief=Tkinter.GROOVE)
logarea.pack(fill="none", expand=Tkinter.TRUE)

m.mainloop()
