import Tkinter,tkFileDialog
import subprocess
m=Tkinter.Tk()
m.title('LogPad')
filename =""
bgcolor='black'
fgcolor='green'

topframe = Tkinter.Frame(m)
topframe.configure(bg=bgcolor)
topframe.pack( side = Tkinter.TOP )
bottomframe = Tkinter.Frame(m)
bottomframe.configure(bg=bgcolor)
bottomframe.pack( side = Tkinter.BOTTOM )

def RunButton():
     global filename
     filename = tkFileDialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
     filepatharea.delete('1.0', Tkinter.END)
     filepatharea.insert(Tkinter.INSERT,filename )
     
def RunButton2():
     global filename,logtype,cataegory
     logarea.delete('1.0', Tkinter.END)
     if cataegory.get() :
         if logtype.get() == "all" :
            searchquery = "awk '{ print $6;}' "+ filename +" | sort -u "
         else :
             searchquery = "awk '{ if( $5 == \""+logtype.get()+"\" ) print $6;}' " + filename + " | sort -u "
     else :
         if logtype.get() == "all" :
            searchquery = "awk '{ print;}' "+ filename
         else :
             searchquery = "awk '{ if( $5 == \""+logtype.get()+"\" ) print;}' "+ filename 
     if searchbox.get("1.0",'end-1c') :
         searchquery = searchquery+" | grep "+ searchbox.get("1.0",'end-1c') + " "
     print ( searchquery )   
     logarea.insert(Tkinter.INSERT,subprocess.check_output(searchquery,shell=True) )


# Select File action button creation and packing to the view area

button = Tkinter.Button(topframe, text='Select File', bg='green',fg='white', command=RunButton)
button.pack(fill="none")

# File Path label creation and packing to the view area

filepathlabel = Tkinter.Label(topframe,justify = Tkinter.LEFT)
filepathlabel.config(text = "File Path :",bg=bgcolor,fg=fgcolor)
filepathlabel.pack(anchor=Tkinter.W)

# File Path creation and packing to the view area

filepatharea = Tkinter.Text(topframe,wrap=Tkinter.WORD,width=200, height= 2)
filepatharea.configure(bg=bgcolor,fg=fgcolor,highlightbackground=bgcolor)
filepatharea.pack(fill="none", expand=Tkinter.TRUE)


# Get Logs action button creation and packing to the view area

button2 = Tkinter.Button(topframe, text='Get Logs', bg='green',fg='white', command=RunButton2)
button2.pack(fill="none",side=Tkinter.RIGHT)


# Search box label creation and packing to the view area

searchboxlabel = Tkinter.Label(topframe,justify = Tkinter.LEFT)
searchboxlabel.config(text = "Search Area",bg=bgcolor,fg=fgcolor)
searchboxlabel.pack(side=Tkinter.LEFT)
 
# Search box text area creation and packing to the view area

searchbox=Tkinter.Text(topframe, height=2, width=50, borderwidth=2, relief=Tkinter.GROOVE)
searchbox.configure(highlightbackground=bgcolor)
searchbox.pack(side=Tkinter.LEFT)


# Class name Category selection Check Box creation

cataegory = Tkinter.IntVar()
classnamecheckbox = Tkinter.Checkbutton(topframe,variable=cataegory)
classnamecheckbox.config(bg=bgcolor)
classnamecheckbox.pack(side=Tkinter.LEFT)
# Search box label creation and packing to the view area

classnamecheckboxlabel = Tkinter.Label(topframe,justify = Tkinter.LEFT)
classnamecheckboxlabel.config(text = "Display Class Name alone",bg=bgcolor,fg=fgcolor)
classnamecheckboxlabel.pack(side=Tkinter.LEFT)


# Logs Type ( E - Error, W - Warning, D - Debug, I - Info, V - Verbose , ALL ) Category selection 
# Radio box creation, packing and default option selection.

logtype= Tkinter.StringVar()
Tkinter.Radiobutton(topframe, 
              value='E',     # E - Error Category Radio Button  
              variable=logtype, 
              bg=bgcolor,fg=fgcolor).pack(side=Tkinter.LEFT)
Tkinter.Label(topframe,justify = Tkinter.LEFT, text = "E",bg=bgcolor,fg=fgcolor, padx = 20).pack(side=Tkinter.LEFT)

Tkinter.Radiobutton(topframe, 
              value='W',     # W - Warning Category Radio Button  
              variable=logtype, 
              bg=bgcolor,fg=fgcolor).pack(side=Tkinter.LEFT)
Tkinter.Label(topframe,justify = Tkinter.LEFT, text = "W",bg=bgcolor,fg=fgcolor, padx = 20).pack(side=Tkinter.LEFT)

Tkinter.Radiobutton(topframe, 
              value='D',     # D - Debug Category Radio Button  
              variable=logtype, 
              bg=bgcolor,fg=fgcolor).pack(side=Tkinter.LEFT)
Tkinter.Label(topframe,justify = Tkinter.LEFT, text = "D",bg=bgcolor,fg=fgcolor, padx = 20).pack(side=Tkinter.LEFT)

Tkinter.Radiobutton(topframe, 
              value='I',     # I - Info Category Radio Button  
              variable=logtype, 
              bg=bgcolor,fg=fgcolor).pack(side=Tkinter.LEFT)
Tkinter.Label(topframe,justify = Tkinter.LEFT, text = "I",bg=bgcolor,fg=fgcolor, padx = 20).pack(side=Tkinter.LEFT)

Tkinter.Radiobutton(topframe, 
              value='V',     # V - Verbose Category Radio Button  
              variable=logtype, 
              bg=bgcolor,fg=fgcolor).pack(side=Tkinter.LEFT)
Tkinter.Label(topframe,justify = Tkinter.LEFT, text = "V",bg=bgcolor,fg=fgcolor, padx = 20).pack(side=Tkinter.LEFT)

R1=Tkinter.Radiobutton(topframe, 
              value='all',    # ALL Category Radio Button 
              variable=logtype, 
              bg=bgcolor,fg=fgcolor)
R1.pack(side=Tkinter.LEFT)
R1.select()
Tkinter.Label(topframe,justify = Tkinter.LEFT, text = "ALL",bg=bgcolor,fg=fgcolor, padx = 20).pack(side=Tkinter.LEFT)


# Log Area Label creation and packing to the view area

logarealabel = Tkinter.Label(bottomframe,justify = Tkinter.LEFT)
logarealabel.config(text = "Log Area", bg=bgcolor,fg=fgcolor)
logarealabel.pack(anchor=Tkinter.W)

# Log Area creation and packing to the view area

logarea = Tkinter.Text(bottomframe,wrap=Tkinter.WORD,width=200, height= 30, borderwidth=2, relief=Tkinter.GROOVE,bg=bgcolor,fg=fgcolor)
logarea.pack(fill="none", expand=Tkinter.TRUE)
m.config(bg=bgcolor)
m.mainloop()
