from tkinter import *
import backend
def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()
    print(index)
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    
    
def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)
def search_command():
    list1.delete(0,END)
    for row in backend.search(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get()):
        list1.insert(END,row)
def insert_command():
    backend.insert(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get())
    list1.delete(0,END)
    list1.insert(END,(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get()))
def delete_command():
    backend.delete(selected_tuple[0])
def update_command():
    backend.update(selected_tuple[0],e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get())

window=Tk()
window.wm_title("Bookstore")
l1=Label(window,text="Title")
l1.grid(row=0,column=0)
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)
l2=Label(window,text="Year")
l2.grid(row=1,column=0)
e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=1,column=1)
l3=Label(window,text="Author")
l3.grid(row=0,column=4)
e3_value=StringVar()
e3=Entry(window,textvariable=e3_value)
e3.grid(row=0,column=5)
l4=Label(window,text="ISBN")
l4.grid(row=1,column=4)
e4_value=StringVar()
e4=Entry(window,textvariable=e4_value)
e4.grid(row=1,column=5)
b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(row=2,column=5)
b2=Button(window,text="Search entry",width=12,command=search_command)
b2.grid(row=3,column=5)
b3=Button(window,text="Add entry",width=12,command=insert_command)
b3.grid(row=4,column=5)
b4=Button(window,text="UpdateSelected",width=12,command=update_command)
b4.grid(row=5,column=5)
b5=Button(window,text="DeleteSelected",width=12,command=delete_command)
b5.grid(row=6,column=5)
b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=5)
list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=1,rowspan=6,columnspan=2)
sb1=Scrollbar(window)
sb1.grid(row=2,column=3,rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>',get_selected_row)
window.mainloop()


