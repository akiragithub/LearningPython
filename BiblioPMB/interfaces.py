# *-*coding:Latin-1 -*

import tkinter, tkinter.messagebox
from PIL import Image, ImageTk

from mabd import Mabd
from mabiblio import Library, Book, User
import Pmw

class Interface :
    def __init__(self):
        """
        I have no idea of constructor for this class.
        Actually I think it is not needed
        """

         #creating the main window
        self.wind = tkinter.Tk()
        self.img = ImageTk.PhotoImage(file=r'new_file1.png')
        self.wind.tk.call('wm', 'iconphoto', self.wind._w, self.img)
        #self.show_add_user_dialog()

        self.is_author_checked = tkinter.IntVar()
        self.is_price_checked = tkinter.IntVar()
        self.is_user_checked = tkinter.IntVar()
        self.is_classe_checked = tkinter.IntVar()
        
        self.BOOK_AVAILABLE = "1"
        self.BOOK_LEND = "0"

    def program_entry(self):
        """This is the entry point of the librairy.
            We aim here to handle everything relative to interfaces"""
        
        
    #   Organizing menu part
        
        #MenuBar
        menubar = tkinter.Menu(self.wind)

        #Entries
        menu1 = tkinter.Menu(menubar, tearoff=0)
        menu2 = tkinter.Menu(menubar, tearoff=0)
        menu3 = tkinter.Menu(menubar, tearoff=0)
    #    menu4 = tkinter.Menu()
        
        #Preparing image file

    #    img = Image.open("new_file1.png")
        real_img = ImageTk.PhotoImage(file = r"new_file1.png")
    ##    im = gtk.Image()

        # adding entries to Menus
        menu1.add_command(label="    creer",  image=real_img, compound="left", command=self.create_book)
        menu1.add_command(label="    enregistrer", image=real_img, compound="left", command=self.confirm_save)
        menu1.add_command(label="    annuler", image=real_img, compound="left", command=self.cancel_without_saving)
        menu1.add_separator()
        menu1.add_command(label="    quitter", image=real_img, compound="left", command=self.confirm_exit)

        menu2.add_command(label="    supprimer", image=real_img, compound="left", command=self.confirm_delete)

        menu3.add_command(label="    A propos", image=real_img, compound="left", command=self.who_are_we)

        #adding menus to menubar
        menubar.add_cascade(label="fichier", menu=menu1)
        menubar.add_cascade(label="edition", menu=menu2)
        menubar.add_cascade(label="aide", menu=menu3)

        self.wind.config(menu=menubar)

    #   Body part
        
        l_frame = tkinter.LabelFrame(self.wind, text="Renseignements du livre")
        l_frame.grid(row=1, column=1, pady=10, padx=10)

        tkinter.Label(l_frame, text="Numero d'enregistrement:").grid(row=1, column=1, sticky="E", padx=5, pady=10)    
        tkinter.Label(l_frame, text="Nom : ").grid(row=2, column=1, sticky="E", padx = 5, pady = 10)
        tkinter.Label(l_frame, text="Auteur : ").grid(row=3, column=1, sticky="E", padx = 5, pady = 10)
        tkinter.Label(l_frame, text="Prix : ").grid(row=4, column=1, sticky="E", padx = 5, pady = 10) 
        tkinter.Label(l_frame, text="ISBN : ").grid(row=5, column=1, sticky="E", padx = 5, pady = 10)
        tkinter.Label(l_frame, text="Classe : ").grid(row=6, column=1, sticky="E", padx = 5, pady = 10)
        #frame for the 2 button radios
        l_frame_2 = tkinter.LabelFrame(l_frame, borderwidth=0)
        l_frame_2.grid(row=7, column=1, sticky="E", padx = 5, pady = 10)
        
        self.status = tkinter.StringVar()
        pret_rbtn = tkinter.Radiobutton(l_frame_2, text="En Pret", variable = self.status, value=self.BOOK_LEND)
        pret_rbtn.grid(row=0, column=0, sticky="W", padx=5, pady=10)
        dispo_rbtn = tkinter.Radiobutton(l_frame_2, text="Disponible", variable = self.status, value=self.BOOK_AVAILABLE)
        dispo_rbtn.grid(row=1, column=0, sticky="W", padx=5, pady=10)
        tkinter.Label(l_frame, text="Mle du Preteur : ").grid(row=8, column=1, sticky="E", padx=5, pady=10)

        #global status
        self.book_reg_num = tkinter.Entry(l_frame, width=30)
        self.book_reg_num.grid(row=1, column=2, sticky="W", padx=25, pady=10)
        self.book_name = tkinter.Entry(l_frame, width=30)
        self.book_name.grid(row=2, column=2, sticky="W", padx=25, pady=10)
        self.book_author = tkinter.Entry(l_frame, width=30)
        self.book_author.grid(row=3, column=2, sticky="W", padx=25, pady=10)
        self.book_price = tkinter.Entry(l_frame, width=30)
        self.book_price.grid(row=4, column=2, sticky="W", padx=25, pady=10)
        self.book_isbn = tkinter.Entry(l_frame, width=30)
        self.book_isbn.grid(row=5, column=2, sticky="W", padx=25, pady=10)
        m_val = ["Tle", "1ere", "2nde", "3eme", "4eme", "5eme","6eme"]
        m_val = m_val[::-1] # Reverse the list values for display
        self.book_classe_spbox = tkinter.Spinbox(l_frame, width=30, values=m_val)
        self.book_classe_spbox.grid(row=6, column=2, sticky="W", padx=25, pady=10)
        self.user_number = tkinter.Entry(l_frame, width=30)
        self.user_number.grid(row=8, column=2, sticky="W", padx=20, pady=20)
        
        l_frame_right = tkinter.LabelFrame(self.wind, text="Prytanee Militaire de Bembereke")
        l_frame_right.grid(row=1,column=2, padx=10)    
        
        logo_image = ImageTk.PhotoImage(file=r'logo_pmb_1.jpg')
        
        canevas = tkinter.Canvas(l_frame_right, bg = "red", width=200, height=263)
        canevas.create_image(102, 133, image=logo_image)
        canevas.grid(row=1, column=1, sticky="W", padx=20)

        save_btn = tkinter.Button(l_frame_right, text="Enregistrer", command=self.confirm_save)
        save_btn.grid(row=3, column=1, padx=20, pady=20)

        # drawing the canvas
        # logo's gray : #FC902E
        # logo's blue : #BBE7EA
        bottom_canvas = tkinter.Canvas(self.wind, bg="#BBE7EA", width=640)
        #bottom_canvas.create_line(0, 2, 780, 2)
        bottom_canvas.grid(row=3, columnspan=2, column=1, sticky="W", padx=20, pady=20)
        
        
        #drawing canvas containing search bar
        search_canvas = tkinter.Canvas(bottom_canvas, bg="#FC902E")
        search_canvas.pack(fill="x", padx=10, pady=5)
        self.auth_chbtn = tkinter.Checkbutton(search_canvas, text="Auteur", bg="#FC902E", variable=self.is_author_checked)
        self.auth_chbtn.grid(row=1, column=1, padx=5, pady=5)
        self.auth_spbox = tkinter.Spinbox(search_canvas, values=("Israel","Elon Musk"))
        self.auth_spbox.grid(row=1, column=2, padx=5, pady=5)
        self.price_chbtn = tkinter.Checkbutton(search_canvas, text="Prix", bg="#FC902E", variable=self.is_price_checked)
        self.price_chbtn.grid(row=1, column=3, padx=5, pady=5)    
        self.price_spbox = tkinter.Spinbox(search_canvas, values=("Israel","Elon Musk"))
        self.price_spbox.grid(row=1, column=4, padx=5, pady=5)
        self.user_chbtn = tkinter.Checkbutton(search_canvas, text="Preteur", bg="#FC902E", variable=self.is_user_checked)
        self.user_chbtn.grid(row=1, column=5, padx=5, pady=5)
        self.pret_spbox = tkinter.Spinbox(search_canvas, values=("Israel","Elon Musk"))
        self.pret_spbox.grid(row=1, column=6, padx=5, pady=5)
        self.classe_chbtn = tkinter.Checkbutton(search_canvas, text="Classe", bg="#FC902E", variable=self.is_classe_checked)
        self.classe_chbtn.grid(row=1, column=7, padx=5, pady=5)
        self.classe_spbox = tkinter.Spinbox(search_canvas, values=("Israel","Elon Musk"))
        self.classe_spbox.grid(row=1, column=8, padx=5, pady=5)
        self.dispo_chbtn = tkinter.Checkbutton(search_canvas, text="Dispo", bg="#FC902E")
        self.dispo_chbtn.grid(row=1, column=9, padx=5, pady=5)
        self.search_label = tkinter.Label(search_canvas, image=real_img, bg="#FC902E")
        self.search_label.grid(row=1, column=10, padx=5, pady=5, sticky="news")
        self.search_label.bind("<Button-1>",func=self.search_books)
        #drawing canvas for result columns names
        columns_names_canvas = tkinter.Canvas(bottom_canvas, bg="#FC902E")
        columns_names_canvas.pack(fill="x", padx=10, pady=5)
        tkinter.Label(columns_names_canvas, text="N°").grid(column=1, row=1, padx=5, pady=5, sticky="news")
        tkinter.Label(columns_names_canvas, text="NOM").grid(column=2, row=1, padx=5, pady=5, sticky="news")
        tkinter.Label(columns_names_canvas, text="AUTEUR").grid(column=3, row=1, padx=5, pady=5, sticky="news")
        tkinter.Label(columns_names_canvas, text="PRIX").grid(column=4, row=1, padx=5, pady=5, sticky="news")
        tkinter.Label(columns_names_canvas, text="CLASSE").grid(column=5, row=1, padx=5, pady=5, sticky="news")
        tkinter.Label(columns_names_canvas, text="DISPO").grid(column=6, row=1, padx=5, pady=5, sticky="news")
        tkinter.Label(columns_names_canvas, text="DATE DE PRET").grid(column=7, row=1, padx=5, pady=5, sticky="news")
        tkinter.Label(columns_names_canvas, text="UTILISATEUR").grid(column=8, row=1, padx=5, pady=5, sticky="news")
        
        #adding columns listboxes
        
        result_num_lbox = tkinter.Listbox(columns_names_canvas)
        result_num_lbox.grid(column=1, row=2, padx=5, pady=5, sticky="E")    
        result_name_lbox = tkinter.Listbox(columns_names_canvas)
        result_name_lbox.grid(column=2, row=2, padx=5, pady=5, sticky="E")    
        result_auth_lbox = tkinter.Listbox(columns_names_canvas)
        result_auth_lbox.grid(column=3, row=2, padx=5, pady=5, sticky="E")    
        result_price_lbox = tkinter.Listbox(columns_names_canvas)
        result_price_lbox.grid(column=4, row=2, padx=5, pady=5, sticky="E")    
        result_classe_lbox = tkinter.Listbox(columns_names_canvas)
        result_classe_lbox.grid(column=5, row=2, padx=5, pady=5, sticky="E")   
        result_dispo_lbox = tkinter.Listbox(columns_names_canvas)
        result_dispo_lbox.grid(column=6, row=2, padx=5, pady=5, sticky="E")     
        result_lend_date_lbox = tkinter.Listbox(columns_names_canvas)
        result_lend_date_lbox.grid(column=7, row=2, padx=5, pady=5, sticky="E")    
        result_user_lbox = tkinter.Listbox(columns_names_canvas)
        result_user_lbox.grid(column=8, row=2, padx=5, pady=5, sticky="E")    
        
        self.wind.mainloop()

    def create_book(self):
        print("create book")

    def save_book(self):
        m_book = Book(self.book_reg_num.get(),
                      self.book_name.get(),
                      self.book_author.get(),
                      self.book_price.get(),
                      self.book_isbn.get(),
                      self.book_classe_spbox.get(),
                      self.user_number.get(),
                      self.status.get())

        
        m_db.add_book_to_db(                                # add book to db
                            reg_num = m_book.get_reg_num(),
                            name = m_book.get_name(),
                            author = m_book.get_author(),
                            price = m_book.get_price(),
                            isbn = m_book.get_isbn(),
                            classe = m_book.get_classe(),
                            status = m_book.get_status()
                            )
        # Doing remaining checking for user and avalability

        #print("status is : ",self.status.get())
        #print("book lend is : ", self.BOOK_LEND)

        if self.status.get()==self.BOOK_LEND :              # if book is being lend
            print("we are in the book_lend")
                
            user = m_db.search_user()                           # checking if user already exists
            print("len user is : ",len(user))
            if len(user)==0 :                                   # if user doesn't exist yet
                self.show_add_user_dialog()                          # add new user with his name
            else :
                m_db.update_book_user(self.book_reg_num.get(),  # add new book lent
                                      self.user_number.get())

            m_db.update_books_read(self.book_reg_num.get(),     # add book into books list user has read
                                       self.user_number.get())
            
        elif self.status.get()==self.BOOK_AVAILABLE :       # if book is being returned
            m_db.delete_entry_from_table(                   # delete it from books_lend
                table_name="BOOKS_LEND",
                entry_name="reg_num",
                entry_value=self.book_reg_num.get())
            
    def show_add_user_dialog(self,
                             user_mle=None):
        self.my_dialog = MyDialog(self.wind,
                                  first_label="Matricule :",
                                  first_entry=self.user_number.get(),
                                  second_label="Nom Prénoms :")

        self.wind.wait_window(self.mydialog.top)
        print("mle : ", self.mydialog.user_mle)
        print("name : ", self.mydialog.user_name)
        

    def abort_book(confirm_save):
        print("abort book")

    def leave_soft(confirm_save):
        print("Leave librairy")

    def delete_book(confirm_save):
        print("delete book")

    def search_books(self, hack):
        "This is the function for books searching. To be defined later"
        print("Searching for book")
        author, price, user_mle, classe, m_status = None, None, None, None, None
       
        if(self.is_author_checked.get()==1):
            author = self.auth_spbox.get()
        if self.is_price_checked.get() == 1:
            price = self.price_spbox.get()
        if self.is_user_checked.get() == 1:
            user_mle = self.pret_spbox.get()
        if self.is_classe_checked.get() == 1:
            classe = self.classe_spbox.get()
        if self.status.get() == 1:
            m_status = self.status.get()

        query_result = m_db.search_book(author, price, user_mle, classe, m_status)
        
        return query_result

    def display_result(self, results):
        for result in results:
            ""
            
        
       

    def who_are_we(self):
        print("who are we ? ")
        my_message = tkinter.messagebox.Message(self.wind, title="BiblioPMB 1.0",
                                                message="""This software is developped by Lt SINGBO Israel.\
                                                        \nTel:+22997816156\
                                                        \ne-mail: sisra1993@yahoo.fr""")
        my_message.show()

        #tkinter.messagebox.showinfo(title="Info 2", message="This software is developped by Lt SINGBO Israel.\n Tel:+22997816156")
        

    ##  Creating tables and views

    def confirm_save(self):
        should_save = tkinter.messagebox.askokcancel(title="Sauvegarder", message="Voulez-vous sauvegarder ce livre ? ")
        if should_save:
            self.save_book()
        #else :
            #Do nothing
    def confirm_delete(self):
        should_del = tkinter.messagebox.askyesno(title="Suppression de livre", message="Etes-vous sûr de vouloir supprimer ce livre ?")
        if should_del:
            self.delete_book()

    def confirm_update(self):
        should_update = tkinter.messagebox.askyesno(title="Mise à jour", message="Voulez-vous enregistrer les modifications ?")
        if should_update:
            self.update_book()
            
    def cancel_without_saving(self):
        should_cancel = tkinter.messagebox.askyesno(title="Annuler l'édition", message="Voulez-vous annuler vos modifications ?")
        if should_cancel:
            self.abort_book

    def confirm_exit(self):
        should_exit = tkinter.messagebox.askyesno(title="Quitter", message="Voulez-vous quitter sans sauvegarder ?")
        if should_exit:
            self.leave_soft(self)


class MyDialog :
    """
            This is a custom dialog with two entryfields and two buttons 
    """
    def __init__(
        self,
        parent=None,
        first_label=None,
        first_entry="",
        first_validate='numeric',
        second_label=None,
        second_entry="",
        second_validate='alphabetic',
        m_command=None
        ):
        top = self.top = tkinter.Toplevel(parent)
        self.first_entry_f = Pmw.EntryField(top,
                                              labelpos='w',
                                              label_text=first_label,
                                              validate=first_validate,
                                              value=first_entry)
        self.second_entry_f = Pmw.EntryField(top,
                                               labelpos='w',
                                               label_text=second_label,
                                               value=second_entry,
                                               validate=second_validate)
        
        self.ok_btn = tkinter.Button(top,text="OK", command=self.ok_command)
        self.cancel_btn = tkinter.Button(top, text="Cancel", command=self.cancel_command)
        self.first_entry_f.pack(anchor='e')
        self.second_entry_f.pack(anchor='e')
        self.ok_btn.pack(anchor='w')
        self.cancel_btn.pack(anchor='e')
        #top.mainloop()
            
    def ok_command(self, m_command):
        if m_command==None:
            self.user_mle = self.first_entry.get()
            self.user_name = self.second_entry.get()
        else:
            return m_command()
        self.top.destroy()

    def cancel_command(self):
        self.top.destroy()
            
    







if __name__ == "__main__":
    
    #
    m_book = Book()

    #connecting to db and creating inexistant tables
    m_db = Mabd(host='localhost',
                user='root',
                passwd='')
    m_db.connect()
    m_db.create_tables_if_not_exists()

    main_interface = Interface()

    main_interface.program_entry()
    
    

    
    
