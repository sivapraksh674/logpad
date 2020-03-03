import Tkinter,tkFileDialog
import subprocess
m=Tkinter.Tk()
m.title('LogPad')
filename =""

def RunButton():
     global filename
     filename = tkFileDialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
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

# Select File action button creation and packing to the view area

button = Tkinter.Button(m, text='Select File', bg='green',fg='white', command=RunButton)
button.pack(fill="none")

# Get Logs action button creation and packing to the view area

button2 = Tkinter.Button(m, text='Get Logs', bg='green',fg='white', command=RunButton2)
button2.pack(fill="none")

# File Path label creation and packing to the view area

filepathlabel = Tkinter.Label(m,justify = Tkinter.LEFT)
filepathlabel.pack(anchor=Tkinter.W)

# File Path packing to the view area

filepatharea = Tkinter.Text(m,wrap=Tkinter.WORD,width=200, height= 2)
filepatharea.pack(fill="none", expand=Tkinter.TRUE)

# Search box label creation and packing to the view area

searchboxlabel = Tkinter.Label(m,justify = Tkinter.LEFT)
searchboxlabel.pack(anchor=Tkinter.E)
searchboxlabel.config(text = "Search Area")
 
# Search box text area creation and packing to the view area

searchbox=Tkinter.Text(m, height=2, width=50)
searchbox.pack(anchor=Tkinter.E)


# Class name Category selection Check Box creation

cataegory = Tkinter.IntVar()
Tkinter.Checkbutton(m, text="Display Class Name alone", variable=cataegory).pack(anchor=Tkinter.W)


# Logs Type ( E - Error, W - Warning, D - Debug, I - Info, V - Verbose , ALL ) Category selection 
# Radio box creation, packing and default option selection.

logtype= Tkinter.StringVar()
Tkinter.Radiobutton(m, 
              text="E",     # E - Error Category Radio Button 
              padx = 20, 
              variable=logtype, 
              value='E').pack(anchor=Tkinter.W)
Tkinter.Radiobutton(m, 
              text="W",     # W - Warning Category Radio Button 
              padx = 20, 
              variable=logtype, 
              value='W').pack(anchor=Tkinter.W)
Tkinter.Radiobutton(m, 
              text="D",     # D - Debug Category Radio Button  
              padx = 20, 
              variable=logtype, 
              value='D').pack(anchor=Tkinter.W)
Tkinter.Radiobutton(m, 
              text="I",     # I - Info Category Radio Button 
              padx = 20, 
              variable=logtype, 
              value='I').pack(anchor=Tkinter.W)
Tkinter.Radiobutton(m, 
              text="V",     # D - Debug Category Radio Button 
              padx = 20, 
              variable=logtype, 
              value='V').pack(anchor=Tkinter.W)
R1=Tkinter.Radiobutton(m, 
              text="All",     # V - Verbose Category Radio Button 
              padx = 20, 
              variable=logtype, 
              value='all')
R1.pack(anchor=Tkinter.W)
R1.select()

# Log Area Label creation and packing to the view area

logarealabel = Tkinter.Label(m,justify = Tkinter.LEFT)
logarealabel.pack()

# Log Area creation and packing to the view area

logarea = Tkinter.Text(m,wrap=Tkinter.WORD,width=200, height= 20)
logarea.pack(fill="none", expand=Tkinter.TRUE)

m.mainloop()
