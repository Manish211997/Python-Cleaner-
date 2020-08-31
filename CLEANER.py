import os
import shutil
import tkinter as tk

root= tk.Tk()


def cleaner():
    
    #  Demo dictionary which contain file extension with names 

    demod={"py":"Python","java":"JAVA","class":"JAVA","cpp":"C++","c":"C","html":"HTML","bat":"BATCH","css":"CSS",
    "txt":"TEXT","docx":"Document","doc":"Document","pdf":"PDF","odt":"OpenOffice","gif":"IMAGES","png":"IMAGES",
    "jpg":"IMAGES","jpeg":"IMAGES","mp3":"MUSIC","mp4":"VIDEOS","aif":"MUSIC","wav":"MUSIC",
    "rar":"COMPRESSED","zip":"COMPRESSED","tar":"COMPRESSED","exe":"EXECUTABLE","dll":"EXECUTABLE",
    "ppt":"PRESENTATION","pptx":"PRESENTATION","svg":"IMAGES","pps":"PRESENTATION","spec":"SPECIFICATION","php":"PHP","js":"JAVASCRIPT"}

    # Making list of files inside the current directory

    d=[f for f in os.listdir('.') if os.path.isfile(f)]

    # Initializing dictionary which will contain the all 
    # the files extension and names which the current directory has.

    filedict={}

    # Looping through the list of files and adding the extensions
    # with there name and ignoring the cleaner application and files which are not in demo dictionary [demod]

    for i in d:
        typ=i.split(".")
        typ=typ[len(typ)-1]
        if i.split(".")[0]=="CLEANER":
            pass
        elif typ not in demod:
            filedict[typ]="OTHER" 
        else:
            filedict[typ]=demod[typ]

    # Getting the currrent working directory 

    path1=os.getcwd()

    # Creating the directories which are required for the files 
    # and Ignoring if the directory already exist

    for i in filedict:
        path=os.path.join(path1,filedict[i])
        if not os.path.isdir(path):
            os.mkdir(path)
        else:
            pass

    # Moving the files to there respective directories and
    # and ignoring cleaner application and if the file already
    # exist in the directory then showing a warning " Already exist "

    j=0
    for i in d:
        typ=i.split(".")
        typ=typ[len(typ)-1]
        if i.split(".")[0]=="CLEANER":
            pass
        else:
            try:
                shutil.move(i,filedict[typ])
            except:
                v=i+" Already inside "+filedict[typ]
                l=tk.Label(root, text= v, fg='red', font=('helvetica', 8, 'bold'))
                canvas1.create_window(175, 230+j, window=l)
                j+=20
    label1 = tk.Label(root, text= 'Successfully Cleaned !', fg='green', font=('helvetica', 16, 'bold'))
    canvas1.create_window(175, 200, window=label1)


# Made a GUI for the User to easily clean the files with just a button click


canvas1 = tk.Canvas(root, width = 350, height = 300)
canvas1.pack()


label1 = tk.Label(root, text= 'Take this application to the place where all the Files exist \n Click on the clean button cleaner will automatically clean the file \n putting them in respective folder', fg='blue', font=('helvetica', 9, 'italic'))
canvas1.create_window(175, 20, window=label1)    
    
button1 = tk.Button(text='CLEAN',command=cleaner, bg='brown',fg='white')
canvas1.create_window(175, 150, window=button1)



root.title("SPACE CLEANER")


root.mainloop()