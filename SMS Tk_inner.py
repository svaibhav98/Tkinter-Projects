from tkinter import *
from tkinter import ttk



class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System by Vaibhav")
        self.root.geometry("1350x700+0+0")



#tirle frame
        title = Label(self.root, text="Student Management System", bd=10, relief=SUNKEN,font =("Times new roman",40, "bold"),bg= "yellow",fg ="red")
        title.pack(side= TOP, fill = X)





# frame left vaala...frame1 as manage frme
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=450, height=580)


        m_title= Label(Manage_Frame, text= "Manage Students",bg="crimson",fg="white",font =("Times new roman",30, "bold"))
        m_title.grid(row=0, columnspan=2,pady = 20)

        #making roll no text and entry
        lbl_rollno= Label(Manage_Frame, text= "Roll No.",bg="crimson",fg="white",font =("Times new roman",20, "bold"))
        lbl_rollno.grid(row=1,column=0, padx=20,pady = 10, sticky ="w")

        txt_rollno = Entry(Manage_Frame,fg="Black",font =("arial",12, "bold"),bd=5, relief=GROOVE)
        txt_rollno.grid(row=1,column=1, padx=20,pady = 10, sticky ="w")
        #---
        lbl_name = Label(Manage_Frame, text="Name", bg="crimson", fg="white", font=("Times new roman",20, "bold"))
        lbl_name.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        txt_name = Entry(Manage_Frame, fg="Black", font=("arial", 12, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, padx=20, pady=10, sticky="w")
        #_____
        lbl_email = Label(Manage_Frame, text="Email.", bg="crimson", fg="white", font=("Times new roman",20, "bold"))
        lbl_email.grid(row=3, column=0, padx=20, pady=10, sticky="w")

        txt_Email = Entry(Manage_Frame, fg="Black", font=("arial", 12, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, padx=20, pady=10, sticky="w")
        #___________
        lbl_Gender = Label(Manage_Frame, text="Gender", bg="crimson", fg="white",width=5, font=("Times new roman",20, "bold"))
        lbl_Gender.grid(row=4, column=0, padx=20, pady=10, sticky="w")
             #here we will insert combobox using ttk
        combo_gender = ttk.Combobox(Manage_Frame,font=("Times new roman",13, "bold"), state = 'readonly' )    #state = 'readonly' so that you cannot type in that box
          #in this we need to pass value in tuple
        combo_gender ['values']= ("Male", "Female", "Other")
        combo_gender.grid(row=4, column=1,padx=20, pady=10)

        #_______________
        lbl_Contact = Label(Manage_Frame, text="Contact", bg="crimson", fg="white", font=("Times new roman",20, "bold"))
        lbl_Contact.grid(row=5, column=0, padx=20, pady=10, sticky="w")

        txt_Contact = Entry(Manage_Frame, fg="Black", font=("arial", 12, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        #+++++++++++++++++++++++

        lbl_Dob = Label(Manage_Frame, text="D.O.B", bg="crimson", fg="white", font=("Times new roman",20, "bold"))
        lbl_Dob.grid(row=6, column=0, padx=20, pady=10, sticky="w")

        txt_Dob = Entry(Manage_Frame, fg="Black", font=("arial", 12, "bold"), bd=5, relief=GROOVE)
        txt_Dob.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        #===================
        lbl_Address = Label(Manage_Frame, text="Address", bg="crimson", fg="white", font=("Times new roman",20, "bold"))
        lbl_Address.grid(row=7, column=0, padx=20, pady=10, sticky="w")

        txt_Address = Text(Manage_Frame, width =27 , height=3, font=("",10))
        txt_Address.grid(row=7, column=1, padx=20,pady=10, sticky="w")


#-------------BUtton Frame_____________
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=15, y=500, width=420)


        Addbtn= Button(btn_Frame,text="add", width=10).grid(row=0, column=0, padx=10, pady=10)
        updatebtn = Button(btn_Frame, text="Update", width=10).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_Frame, text="Delete", width=10).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_Frame, text="Clear", width=10).grid(row=0, column=3, padx=10, pady=10)













#detail frame Right vaala
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=820, height=580)

#==================================================================================
        lbl_search = Label(Detail_Frame, text="Search By", bg="crimson", fg="white",
                            font=("Times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,width=10, font=("Times new roman", 13, "bold"),
                                    state='readonly')  # state = 'readonly' so that you cannot type in that box
        # in this we need to pass value in tuple
        combo_search['values'] = ("Roll no", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)



        txt_Search = Entry(Detail_Frame, fg="white", font=("Times new roman",13, "bold"), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, padx=20, pady=10, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", width=10,pady=5).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Show all", width=10,pady=5).grid(row=0, column=4, padx=10, pady=10)


#+=========================================Table Frame Rhs below inside detail frame+++++++++++++

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        #add scroll bar for x and y axis ...
        scroll_x= Scrollbar(Table_Frame,orient= HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)

        # use ttk for tree view   as ttk.Treeview
        Student_table=ttk.Treeview(Table_Frame, columns=("Roll","Name","Email","Contact","Gender","DOB","Address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)  #37.56

        Student_table.heading("Roll",text= "Roll No.")
        Student_table.heading("Name", text="Name")
        Student_table.heading("Email", text="Email")
        Student_table.heading("Gender", text="Gender")
        Student_table.heading("Contact", text="Contact")
        Student_table.heading("DOB", text="DOB")
        Student_table.heading("Address", text="Address")

        Student_table['show']='headings'
        Student_table.column("Roll", width=100)
        Student_table.column("Name", width=100)
        Student_table.column("Email", width=100)
        Student_table.column("Gender", width=100)
        Student_table.column("Contact", width=100)
        Student_table.column("DOB", width=100)
        Student_table.column("Address", width=150)

        #But normal pack will onlu fill the table in half frame
        # Student_table.pack()
        #therefore pack using fill=BOTH, expand=1 ...
        #expad is used because it will fill according to our table frame on in the main frame
        Student_table.pack(fill=BOTH, expand=1)















#===========================================================================================================================================

root =Tk()
obj= Student(root)
root.mainloop()