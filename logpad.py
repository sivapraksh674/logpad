try:
    import Tkinter as tkin # this is for python2
    import tkFileDialog
except:
    import tkinter as tkin # this is for python3
    tkFileDialog=tkin.filedialog

import subprocess
m=tkin.Tk()
m.title('LogPad')
filename =""
bgcolor='black'
fgcolor='green'

topframe = tkin.Frame(m)
topframe.configure(bg=bgcolor)
topframe.pack( side = tkin.TOP )
bottomframe = tkin.Frame(m)
bottomframe.configure(bg=bgcolor)
bottomframe.pack( side = tkin.BOTTOM )

def RunButton():
     global filename
     filename = tkFileDialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
     filepatharea.delete('1.0', tkin.END)
     filepatharea.insert(tkin.INSERT,filename )
     searchquery = "awk '{ print;}' "+ filename
     logarea.insert(tkin.INSERT,subprocess.check_output(searchquery,shell=True))
     
def RunButton2():
     global filename,logtype,cataegory
     logarea.delete('1.0', tkin.END)
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
     logarea.insert(tkin.INSERT,subprocess.check_output(searchquery,shell=True))



# Select File action button creation and packing to the view area

button = tkin.Button(topframe, text='Select File', bg='green',fg='white', command=RunButton)
button.pack(fill="none")

# File Path label creation and packing to the view area

filepathlabel = tkin.Label(topframe,justify = tkin.LEFT)
filepathlabel.config(text = "File Path :",bg=bgcolor,fg=fgcolor)
filepathlabel.pack(anchor=tkin.W)

# File Path creation and packing to the view area

filepatharea = tkin.Text(topframe,wrap=tkin.WORD,width=200, height= 2)
filepatharea.configure(bg=bgcolor,fg=fgcolor,highlightbackground=bgcolor)
filepatharea.pack(fill="none", expand=tkin.TRUE)


# Get Logs action button creation and packing to the view area

button2 = tkin.Button(topframe, text='Search', bg='green',fg='white', command=RunButton2)
button2.pack(fill="none",side=tkin.RIGHT)


# Search box label creation and packing to the view area

searchboxlabel = tkin.Label(topframe,justify = tkin.LEFT)
searchboxlabel.config(text = "Search Area",bg=bgcolor,fg=fgcolor)
searchboxlabel.pack(side=tkin.LEFT)
 
# Search box text area creation and packing to the view area

searchbox=tkin.Text(topframe, height=2, width=50, borderwidth=2, relief=tkin.GROOVE)
searchbox.configure(highlightbackground=bgcolor)
searchbox.pack(side=tkin.LEFT)


# Class name Category selection Check Box creation

cataegory = tkin.IntVar()
classnamecheckbox = tkin.Checkbutton(topframe,variable=cataegory)
classnamecheckbox.config(bg=bgcolor)
classnamecheckbox.pack(side=tkin.LEFT)
# Search box label creation and packing to the view area

classnamecheckboxlabel = tkin.Label(topframe,justify = tkin.LEFT)
classnamecheckboxlabel.config(text = "Display Class Name alone",bg=bgcolor,fg=fgcolor)
classnamecheckboxlabel.pack(side=tkin.LEFT)


# Logs Type ( E - Error, W - Warning, D - Debug, I - Info, V - Verbose , ALL ) Category selection 
# Radio box creation, packing and default option selection.

logtype= tkin.StringVar()
tkin.Radiobutton(topframe, 
              value='E',     # E - Error Category Radio Button  
              variable=logtype, 
              bg=bgcolor,fg=fgcolor).pack(side=tkin.LEFT)
tkin.Label(topframe,justify = tkin.LEFT, text = "E",bg=bgcolor,fg=fgcolor, padx = 20).pack(side=tkin.LEFT)

tkin.Radiobutton(topframe, 
              value='W',     # W - Warning Category Radio Button  
              variable=logtype, 
              bg=bgcolor,fg=fgcolor).pack(side=tkin.LEFT)
tkin.Label(topframe,justify = tkin.LEFT, text = "W",bg=bgcolor,fg=fgcolor, padx = 20).pack(side=tkin.LEFT)

tkin.Radiobutton(topframe, 
              value='D',     # D - Debug Category Radio Button  
              variable=logtype, 
              bg=bgcolor,fg=fgcolor).pack(side=tkin.LEFT)
tkin.Label(topframe,justify = tkin.LEFT, text = "D",bg=bgcolor,fg=fgcolor, padx = 20).pack(side=tkin.LEFT)

tkin.Radiobutton(topframe, 
              value='I',     # I - Info Category Radio Button  
              variable=logtype, 
              bg=bgcolor,fg=fgcolor).pack(side=tkin.LEFT)
tkin.Label(topframe,justify = tkin.LEFT, text = "I",bg=bgcolor,fg=fgcolor, padx = 20).pack(side=tkin.LEFT)

tkin.Radiobutton(topframe, 
              value='V',     # V - Verbose Category Radio Button  
              variable=logtype, 
              bg=bgcolor,fg=fgcolor).pack(side=tkin.LEFT)
tkin.Label(topframe,justify = tkin.LEFT, text = "V",bg=bgcolor,fg=fgcolor, padx = 20).pack(side=tkin.LEFT)

R1=tkin.Radiobutton(topframe, 
              value='all',    # ALL Category Radio Button 
              variable=logtype, 
              bg=bgcolor,fg=fgcolor)
R1.pack(side=tkin.LEFT)
R1.select()
tkin.Label(topframe,justify = tkin.LEFT, text = "ALL",bg=bgcolor,fg=fgcolor, padx = 20).pack(side=tkin.LEFT)


# Log Area Label creation and packing to the view area

logarealabel = tkin.Label(bottomframe,justify = tkin.LEFT)
logarealabel.config(text = "Log Area", bg=bgcolor,fg=fgcolor)
logarealabel.pack(anchor=tkin.W)

# Log Area creation and packing to the view area

logarea = tkin.Text(bottomframe,wrap=tkin.WORD,width=200, height= 30, borderwidth=2, relief=tkin.GROOVE,bg=bgcolor,fg=fgcolor)
logarea.pack(fill="none", expand=tkin.TRUE)
m.config(bg=bgcolor)
m.mainloop()
