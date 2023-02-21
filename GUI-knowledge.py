from tkinter import *
from tkinter import ttk  #theme of tk
from tkinter import messagebox


GUI = Tk()                  #นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')


B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
B1.pack(ipadx=20,ipady=20)        #internal 


L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)
##############################
def Button2():          #ชื่อ function สามารถเปลี่ยนแปลงได้
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)
    #messagebox.showwarn
    #messagebox.showerr
    
FB1 = Frame(GUI)
FB1.place(x=100,y=300)

B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)

#internal 
###############################
"""
B2 = Button(GUI,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack()
"""

GUI.mainloop()
