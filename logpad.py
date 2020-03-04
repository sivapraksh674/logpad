try:
    import Tkinter as tkin # this is for python2
    import tkFileDialog
    import tkMessageBox
except:
    import tkinter as tkin # this is for python3
    tkFileDialog=tkin.filedialog
    tkMessageBox=tkin.messagebox

import subprocess
m=tkin.Tk()
m.title('LogPad')
m.resizable(0,0) 
filename =""
bgcolor='black'
fgcolor='green'

logscolorcode = {'E':'red', 'W':'yellow','D':'green', 'I':'white','V':'blue','all':'white'} 

topframe = tkin.Frame(m)
topframe.configure(bg=bgcolor)
topframe.pack( side = tkin.TOP, expand=tkin.TRUE)
searchframe = tkin.Frame(m)
searchframe.configure(bg=bgcolor)
searchframe.pack( side = tkin.TOP,expand=tkin.TRUE )
bottomframe = tkin.Frame(m)
bottomframe.configure(bg=bgcolor)
bottomframe.pack( side = tkin.TOP, expand=tkin.TRUE )

def SelectFile():
     global filename
     print("hit")
     filename = tkFileDialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
     if len(filename) == 0 :
         return
     filepatharea.delete('1.0', tkin.END)
     filepatharea.insert(tkin.INSERT,filename )
     searchquery = "awk '{ print;}' "+ filename
     logarea.config(fg=logscolorcode[logtype.get()]) 
     logarea.insert(tkin.INSERT,subprocess.check_output(searchquery,shell=True))
     
def SearchFunction():
     global filename,logtype,cataegory
     if len(filename) == 0 :
         tkMessageBox.showerror("Error", "Please select the log file to perform search")
         return
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
         searchquery = searchquery+" | grep \""+ searchbox.get("1.0",'end-1c') + "\" "
     print ( searchquery )  
    
     logarea.config(fg=logscolorcode[logtype.get()]) 
     logarea.insert(tkin.INSERT,subprocess.check_output(searchquery,shell=True))


def HandleKeyRelease (e) :
    print ( "Keypressed" , e.char )
    SearchFunction()



# File Path label creation and packing to the view area

filepathlabel = tkin.Label(topframe,justify = tkin.LEFT)
filepathlabel.config(text = "File Path :",bg=bgcolor,fg=fgcolor)
filepathlabel.pack(anchor=tkin.W)

# File Path creation and packing to the view area

filepatharea = tkin.Text(topframe,wrap=tkin.WORD,width=200, height= 2)
filepatharea.configure(bg=bgcolor,fg=fgcolor,highlightbackground=bgcolor)
filepatharea.pack(fill="none", expand=tkin.TRUE)

# Select File action button creation and packing to the view area

selectfilebutton = tkin.Button(topframe, text='SELECT FILE',command=SelectFile)
selectfilebutton.pack(side=tkin.BOTTOM)

# ( Deprecated ) Get Logs action button creation and packing to the view area

#searchbutton = tkin.Button(topframe, text='Search', bg='green',fg='white', command=SearchFunction)
#searchbutton.pack(fill="none",side=tkin.RIGHT)

# Search box label creation and packing to the view area

searchboxlabel = tkin.Label(searchframe,justify = tkin.LEFT)
searchboxlabel.config(text = "Search Area",bg=bgcolor,fg=fgcolor)
searchboxlabel.pack(side=tkin.LEFT)
 
# Search box text area creation and packing to the view area

searchbox=tkin.Text(searchframe, height=2, width=50, borderwidth=2, relief=tkin.GROOVE)
searchbox.configure(highlightbackground=bgcolor)
searchbox.bind('<KeyRelease>',HandleKeyRelease)
searchbox.pack(side=tkin.LEFT)


# Class name Category selection Check Box creation

cataegory = tkin.IntVar()
classnamecheckbox = tkin.Checkbutton(searchframe,variable=cataegory,command=SearchFunction)
classnamecheckbox.config(bg=bgcolor)
classnamecheckbox.pack(side=tkin.LEFT)
# Search box label creation and packing to the view area

classnamecheckboxlabel = tkin.Label(searchframe,justify = tkin.LEFT)
classnamecheckboxlabel.config(text = "Search Class Name Alone",bg=bgcolor,fg=fgcolor)
classnamecheckboxlabel.pack(side=tkin.LEFT)


# Logs Type ( E - Error, W - Warning, D - Debug, I - Info, V - Verbose , ALL ) Category selection 
# Radio box creation, packing and default option selection.

logtype= tkin.StringVar()
tkin.Radiobutton(searchframe, 
              value='E',     # E - Error Category Radio Button  
              variable=logtype, 
              command=SearchFunction,
              bg=bgcolor,fg=fgcolor).pack(side=tkin.LEFT)
tkin.Label(searchframe,justify = tkin.LEFT, text = "E",bg=bgcolor,fg=logscolorcode['E'], padx = 20).pack(side=tkin.LEFT)

tkin.Radiobutton(searchframe, 
              value='W',     # W - Warning Category Radio Button  
              variable=logtype, 
              command=SearchFunction,
              bg=bgcolor,fg=fgcolor).pack(side=tkin.LEFT)
tkin.Label(searchframe,justify = tkin.LEFT, text = "W",bg=bgcolor,fg=logscolorcode['W'], padx = 20).pack(side=tkin.LEFT)

tkin.Radiobutton(searchframe, 
              value='D',     # D - Debug Category Radio Button  
              variable=logtype, 
              command=SearchFunction,
              bg=bgcolor,fg=fgcolor).pack(side=tkin.LEFT)
tkin.Label(searchframe,justify = tkin.LEFT, text = "D",bg=bgcolor,fg=logscolorcode['D'], padx = 20).pack(side=tkin.LEFT)

tkin.Radiobutton(searchframe, 
              value='I',     # I - Info Category Radio Button  
              variable=logtype,
              command=SearchFunction, 
              bg=bgcolor,fg=fgcolor).pack(side=tkin.LEFT)
tkin.Label(searchframe,justify = tkin.LEFT, text = "I",bg=bgcolor,fg=logscolorcode['I'], padx = 20).pack(side=tkin.LEFT)

tkin.Radiobutton(searchframe, 
              value='V',     # V - Verbose Category Radio Button  
              variable=logtype, 
              command=SearchFunction,
              bg=bgcolor,fg=fgcolor).pack(side=tkin.LEFT)
tkin.Label(searchframe,justify = tkin.LEFT, text = "V",bg=bgcolor,fg=logscolorcode['V'], padx = 20).pack(side=tkin.LEFT)

R1=tkin.Radiobutton(searchframe, 
              value='all',    # ALL Category Radio Button 
              variable=logtype, 
              command=SearchFunction,
              bg=bgcolor,fg=fgcolor)
R1.pack(side=tkin.LEFT)
R1.select()
tkin.Label(searchframe,justify = tkin.LEFT, text = "ALL",bg=bgcolor,fg=logscolorcode['all'], padx = 20).pack(side=tkin.LEFT)


# Log Area Label creation and packing to the view area

logarealabel = tkin.Label(bottomframe,justify = tkin.LEFT)
logarealabel.config(text = "Log Area", bg=bgcolor,fg=fgcolor)
logarealabel.pack(anchor=tkin.W)

# Log Area creation and packing to the view area

logarea = tkin.Text(bottomframe,wrap=tkin.WORD,width=200, height= 30, borderwidth=2, relief=tkin.GROOVE,bg=bgcolor,fg=fgcolor)
logarea.pack(fill="none", expand=tkin.TRUE)
m.config(bg=bgcolor)
m.mainloop()
