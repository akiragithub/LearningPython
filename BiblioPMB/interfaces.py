# *-*coding:Latin-1 -*

import tkinter
import tkinter.messagebox

import TkTreectrl
from PIL import ImageTk

import Pmw
import config
from mabd2 import Mabd
from mabiblio import Book
from os import path


class Interface:
    def __init__(self):
        """
        I have no idea of constructor for this class.
        Actually I think it is not needed
        """

        # creating the main window
        # self.root = tkinter.Tk()
        self.wind = tkinter.Tk()
        # self.wind.geometry("800x800")
        self.wind.grid_columnconfigure(0, weight=1)
        self.wind.grid_rowconfigure(0, weight=1)
        logo_path = path.join(path_to_bundle, 'logo_pmb_r.jpg')
        # self.img = ImageTk.PhotoImage(file=r'logo_pmb_r.jpg')
        self.img = ImageTk.PhotoImage(file=logo_path)
        self.wind.tk.call('wm', 'iconphoto', self.wind._w, self.img)

        self.is_author_checked = tkinter.IntVar()
        self.is_price_checked = tkinter.IntVar()
        self.is_user_checked = tkinter.IntVar()
        self.is_classe_checked = tkinter.IntVar()
        self.is_dispo_checked = tkinter.IntVar()

        self.BOOK_AVAILABLE = "1"
        self.BOOK_LEND = "0"

        self.classes_t_v = tkinter.StringVar(self.wind)

        self.result_numbers = []
        self.result_names = []
        self.result_authors = []
        self.result_prices = []
        self.result_classes = []
        self.result_status = []

    def program_entry(self):
        """This is the entry point of the librairy.
            We aim here to handle everything relative to interfaces"""

        #   Organizing menu part

        # MenuBar
        menubar = tkinter.Menu(self.wind)

        # Entries
        menu1 = tkinter.Menu(menubar, tearoff=0)
        menu2 = tkinter.Menu(menubar, tearoff=0)
        menu3 = tkinter.Menu(menubar, tearoff=0)
        #    menu4 = tkinter.Menu()

        # Preparing image files
        about_us_img_path = path.join(path_to_bundle, 'about_us_r.png')
        delete_img_path = path.join(path_to_bundle, 'delete_r.png')
        create_new_img_path = path.join(path_to_bundle, 'create_new_r.png')
        save_img_path = path.join(path_to_bundle, 'save_r.png')
        cancel_img_path = path.join(path_to_bundle, 'cancel_r.png')
        quit_img_path = path.join(path_to_bundle, 'exit_r.png')
        #    img = Image.open("new_file1.png")
        about_us_img = ImageTk.PhotoImage(file=about_us_img_path)
        delete_img = ImageTk.PhotoImage(file=delete_img_path)
        create_new_img = ImageTk.PhotoImage(file=create_new_img_path)
        save_img = ImageTk.PhotoImage(file=save_img_path)
        cancel_img = ImageTk.PhotoImage(file=cancel_img_path)
        quit_img = ImageTk.PhotoImage(file=quit_img_path)

        ##    im = gtk.Image()

        # adding entries to Menus
        menu1.add_command(label="    creer", image=create_new_img, compound="left", command=self.create_book)
        menu1.add_command(label="    enregistrer", image=save_img, compound="left", command=self.confirm_save)
        menu1.add_command(label="    annuler", image=cancel_img, compound="left", command=self.cancel_without_saving)
        menu1.add_separator()
        menu1.add_command(label="    quitter", image=quit_img, compound="left", command=self.confirm_exit)

        menu2.add_command(label="    supprimer", image=delete_img, compound="left", command=self.confirm_delete)

        menu3.add_command(label="    A propos", image=about_us_img, compound="left", command=self.who_are_we)

        # adding menus to menubar
        menubar.add_cascade(label="fichier", menu=menu1)
        menubar.add_cascade(label="edition", menu=menu2)
        menubar.add_cascade(label="aide", menu=menu3)

        self.wind.config(menu=menubar)

        #   Body part

        l_frame = tkinter.LabelFrame(self.wind, text="Renseignements du livre")  # , bg="blue")
        l_frame.grid(row=1, column=1, pady=10, padx=20, sticky="NEWS")
        l_frame.grid_rowconfigure(1, weight=1)
        l_frame.grid_columnconfigure(1, weight=1)

        tkinter.Label(l_frame, text="Numero d'enregistrement:").grid(row=1, column=1, sticky="E", padx=5, pady=5)
        tkinter.Label(l_frame, text="Nom : ").grid(row=2, column=1, sticky="E", padx=5, pady=5)
        tkinter.Label(l_frame, text="Auteur : ").grid(row=3, column=1, sticky="E", padx=5, pady=5)
        tkinter.Label(l_frame, text="Prix : ").grid(row=4, column=1, sticky="E", padx=5, pady=5)
        tkinter.Label(l_frame, text="ISBN : ").grid(row=5, column=1, sticky="E", padx=5, pady=5)
        tkinter.Label(l_frame, text="Classe : ").grid(row=6, column=1, sticky="E", padx=5, pady=5)
        # frame for the 2 button radios
        l_frame_2 = tkinter.LabelFrame(l_frame, borderwidth=0)
        l_frame_2.grid(row=7, column=1, sticky="E", padx=5, pady=5)

        self.status = tkinter.StringVar()
        pret_rbtn = tkinter.Radiobutton(l_frame_2, text="En Pret", variable=self.status, value=self.BOOK_LEND)
        pret_rbtn.grid(row=0, column=0, sticky="W", padx=5, pady=5)
        dispo_rbtn = tkinter.Radiobutton(l_frame_2, text="Disponible", variable=self.status, value=self.BOOK_AVAILABLE)
        dispo_rbtn.grid(row=1, column=0, sticky="W", padx=5, pady=5)
        dispo_rbtn.select()
        tkinter.Label(l_frame, text="Mle du Preteur : ").grid(row=8, column=1, sticky="E", padx=5, pady=5)

        # global status
        self.book_reg_num = tkinter.Entry(l_frame, width=30)
        self.book_reg_num.grid(row=1, column=2, sticky="W", padx=25, pady=5)
        self.book_name = tkinter.Entry(l_frame, width=30)
        self.book_name.grid(row=2, column=2, sticky="W", padx=25, pady=5)
        self.book_author = tkinter.Entry(l_frame, width=30)
        self.book_author.grid(row=3, column=2, sticky="W", padx=25, pady=5)
        self.book_price = tkinter.Entry(l_frame, width=30)
        self.book_price.grid(row=4, column=2, sticky="W", padx=25, pady=5)
        self.book_isbn = tkinter.Entry(l_frame, width=30)
        self.book_isbn.grid(row=5, column=2, sticky="W", padx=25, pady=5)
        r_classes = classes[::-1]  # Reverse the list values for display
        self.book_classe_spbox = tkinter.Spinbox(l_frame, width=28, values=r_classes, textvariable=self.classes_t_v)
        self.book_classe_spbox.grid(row=6, column=2, sticky="W", padx=25, pady=5)
        self.user_number = tkinter.Entry(l_frame, width=30)
        self.user_number.grid(row=8, column=2, sticky="W", padx=25, pady=10)

        l_frame_right = tkinter.LabelFrame(self.wind, text="Prytanee Militaire de Bembereke")  # , bg="red")
        l_frame_right.grid(row=1, column=2, sticky="W", padx=(55, 15), pady=10)

        logo_image_path = path.join(path_to_bundle, 'logo_pmb_1.jpg')
        logo_image = ImageTk.PhotoImage(file=logo_image_path)

        canevas = tkinter.Canvas(l_frame_right, bg="red", width=200, height=263)
        canevas.create_image(102, 133, image=logo_image)
        canevas.grid(row=1, column=1, sticky="W", padx=20)

        save_btn = tkinter.Button(l_frame_right, text="Enregistrer", command=self.confirm_save)
        save_btn.grid(row=3, column=1, padx=20, pady=20)

        # drawing the canvas
        # logo's gray : #FC902E
        # logo's blue : #BBE7EA
        bottom_full_canvas = tkinter.Canvas(self.wind, height=25)
        bottom_full_canvas.grid(row=3, columnspan=2, column=1, sticky="W", padx=20, pady=20)
        # bottom_canvas.create_line(0, 2, 780, 2)

        bottom_canvas = tkinter.Canvas(bottom_full_canvas, bg="#BBE7EA")
        bottom_canvas.pack(side=tkinter.LEFT, fill=tkinter.Y)

        # drawing canvas containing search bar
        search_canvas = tkinter.Canvas(bottom_canvas, bg="#FC902E")
        search_canvas.pack(fill="x", padx=10, pady=5)
        self.auth_chbtn = tkinter.Checkbutton(search_canvas, text="Auteur", bg="#FC902E",
                                              variable=self.is_author_checked)
        self.auth_chbtn.grid(row=1, column=1, padx=5, pady=5)
        self.auth_spbox = tkinter.Spinbox(search_canvas, values=authors)
        self.auth_spbox.grid(row=1, column=2, padx=5, pady=5)
        self.price_chbtn = tkinter.Checkbutton(search_canvas, text="Prix", bg="#FC902E", variable=self.is_price_checked)
        self.price_chbtn.grid(row=1, column=3, padx=5, pady=5)
        self.price_spbox = tkinter.Spinbox(search_canvas, values=prices, width=10)
        self.price_spbox.grid(row=1, column=4, padx=5, pady=5)
        self.user_chbtn = tkinter.Checkbutton(search_canvas, text="Preteur", bg="#FC902E",
                                              variable=self.is_user_checked)
        self.user_chbtn.grid(row=1, column=5, padx=5, pady=5)
        self.pret_spbox = tkinter.Spinbox(search_canvas, values=users, width=10)
        self.pret_spbox.grid(row=1, column=6, padx=5, pady=5)
        self.classe_chbtn = tkinter.Checkbutton(search_canvas, text="Classe", bg="#FC902E",
                                                variable=self.is_classe_checked)
        self.classe_chbtn.grid(row=1, column=7, padx=5, pady=5)
        self.classe_spbox = tkinter.Spinbox(search_canvas, values=classes, width=10)
        self.classe_spbox.grid(row=1, column=8, padx=5, pady=5)
        self.dispo_chbtn = tkinter.Checkbutton(search_canvas, text="Dispo", bg="#FC902E",
                                               variable=self.is_dispo_checked)
        self.dispo_chbtn.grid(row=1, column=9, padx=5, pady=5)
        search_image_path = path.join(path_to_bundle, 'search_r.png')
        search_img = ImageTk.PhotoImage(file=search_image_path)
        self.search_label = tkinter.Label(search_canvas, image=search_img, bg="#FC902E")
        self.search_label.grid(row=1, column=10, padx=5, pady=5, sticky="news")
        self.search_label.bind("<Button-1>", func=self.search_books)

        # drawing canvas for result columns names
        columns_names_canvas = tkinter.Canvas(bottom_canvas, bg="#FC902E")
        columns_names_canvas.pack(fill="x", padx=10, pady=5)

        # Handling it with multiListbox
        columns_tuple = ('N°', 'NOM', 'AUTEUR', 'PRIX', 'CLASSE', 'DISPO', 'DATE DE PRET', 'UTILISATEUR')
        self.mlb = TkTreectrl.MultiListbox(columns_names_canvas, columns=columns_tuple, selectcmd=self.on_item_selected)
        ##        self.mlb.grid(column=1, row=1, columnspan=100)
        self.mlb.pack(fill=tkinter.BOTH, expand=1)
        self.mlb.focus_set()

        # adding scrollbar to the canvas containing results and linking it to every listbox
        scroll_canvas = tkinter.Canvas(bottom_full_canvas, bg="#bbaaaa")
        scroll_canvas.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.scrollbar = tkinter.Scrollbar(scroll_canvas)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.scrollbar.config(command=self.vscrolling)
        self.mlb.config(yscrollcommand=self.scrollbar.set)
        self.wind.mainloop()

    def on_item_selected(self, selected):

        print("Selected is : ", selected)
        selected_values = self.mlb.get(selected[0])
        print("values are : ", selected_values)
        self.update_screen(selected_values)

    def update_screen(self, values):
        values_to_set = values[0]
        reg_num = values_to_set[0]
        name = values_to_set[1]
        author = values_to_set[2]
        price = values_to_set[3]
        classe = values_to_set[4]
        stat = values_to_set[5]
        cur_user = values_to_set[7]
        if (stat == "Oui"):
            stat = self.BOOK_AVAILABLE
        else:
            stat = self.BOOK_LEND
        isbn = m_db.get_isbn(reg_num)

        # clear previous data
        self.clear_previous_data()

        # setting new values
        self.book_reg_num.insert(0, reg_num)
        self.book_name.insert(0, name)
        self.book_author.insert(0, author)
        self.book_price.insert(0, price)
        self.book_isbn.insert(0, isbn)
        self.user_number.insert(0, cur_user)

        self.classes_t_v.set(classe)
        self.status.set(stat)
        m_book.set_values(reg_num, name, author, price, isbn, classe, cur_user, stat)

    def clear_previous_data(self):
        self.book_reg_num.delete(0, tkinter.END)
        self.book_name.delete(0, tkinter.END)
        self.book_author.delete(0, tkinter.END)
        self.book_price.delete(0, tkinter.END)
        self.book_isbn.delete(0, tkinter.END)
        self.user_number.delete(0, tkinter.END)

    def vscrolling(self, *args):
        self.mlb.yview(*args)

    def create_book(self):
        print("create book")
        self.clear_previous_data()

    def update_list(list_type=None, value=None, action=None):

        my_switcher = {
            TYPE_AUTHOR: authors,
            TYPE_BOOK: saved_books,
            TYPE_USER: users,
            TYPE_PRICE: prices
        }
        working_list = my_switcher.get(list_type, None)
        if action == ACTION_ADD:
            working_list.append(value)
        if action == ACTION_REMOVE:
            working_list.remove(value)

    def save_book(self, book_exists=False):
        m_book = Book(self.book_reg_num.get(),
                      self.book_name.get(),
                      self.book_author.get(),
                      self.book_price.get(),
                      self.book_isbn.get(),
                      self.book_classe_spbox.get(),
                      self.user_number.get(),
                      self.status.get())
        print("m_book to save : ", m_book.get_reg_num())
        query_op_status = None
        if book_exists:
            query_op_status = m_db.update_book(  # update book in db
                reg_num=m_book.get_reg_num(),
                name=m_book.get_name(),
                author=m_book.get_author(),
                price=m_book.get_price(),
                isbn=m_book.get_isbn(),
                classe=m_book.get_classe(),
                status=m_book.get_status()
            )

        else:
            query_op_status = m_db.add_book_to_db(  # add book to db
                reg_num=m_book.get_reg_num(),
                name=m_book.get_name(),
                author=m_book.get_author(),
                price=m_book.get_price(),
                isbn=m_book.get_isbn(),
                classe=m_book.get_classe(),
                status=m_book.get_status()
            )
        ##        print("Query_op_status is : ", query_op_status)

        if self.status.get() == self.BOOK_LEND:  # if book is being lend
            user = m_db.search_user(self.user_number.get())  # checking if user already exists
            if len(user) == 0:  # if user doesn't exist yet
                self.show_add_user_dialog()  # add new user with his name

            m_db.update_book_user(self.book_reg_num.get(),  # add new book lent
                                  self.user_number.get())
            m_db.update_books_read(self.book_reg_num.get(),  # add book into books list user has read
                                   self.user_number.get())

        elif self.status.get() == self.BOOK_AVAILABLE:  # if book is being returned
            m_db.delete_entry_from_books_lend(reg_num=self.book_reg_num.get())  # delete it from books_lend

        # Showing a dialog to the user to confirm the success of operation
        print("query_stat, result_ok ", query_op_status, config.RESULT_OK)
        print("query_stat, result_error ", query_op_status, config.RESULT_ERROR)
        if (query_op_status == config.RESULT_OK):
            main_interface.auth_spbox.insert(len(authors), m_book.author)
            main_interface.price_spbox.insert(len(prices), m_book.price)

        self.show_operation_status(query_op_status, ['livre', 'mis à jour'])

    def show_operation_status(self, query_status, key_words=[]):
        """
            this method shows how operation has been terminated
            @key_words is list of 2 elements; the first one is the
            item we are working on : utilisateur, livre, auteur,....
            The second element is the type of operation that has been
            done ("supprimé", "mis à jour")
            @query_status is the result status of the operation
        """
        m_message = None
        m_title = None
        item = key_words[0]
        operation = key_words[1]
        if (query_status == config.RESULT_OK):
            m_message = item + " a été " + operation + " avec success."
            m_title = "Succes"
        elif (query_status == config.RESULT_ERROR):
            m_message = "Oups ! Cet élément n'a pas pu ëtre " + operation + ".\n Veuillez réessayer"
            m_title = "Operation non réussie"
        tkinter.messagebox.showinfo(title=m_title, message=m_message)

    def show_add_user_dialog(self,
                             user_mle=None):
        self.my_dialog = MyDialog(self.wind,
                                  first_label="Matricule :",
                                  first_entry=self.user_number.get(),
                                  second_label="Nom Prénoms :")

        self.wind.wait_window(self.my_dialog.top)

    ##        print("mle : ", self.my_dialog.user_mle)
    ##        print("name : ", self.my_dialog.user_name)

    def abort_book(self, confirm_abort):
        print("abort book")
        self.clear_previous_data()

    def leave_soft(self, confirm_save):
        print("Leave librairy")
        self.wind.destroy()

    def delete_book(self, confirm_save):
        reg_n = m_book.get_reg_num()
        operation_status = m_db.delete_entry_from_livre(reg_num=reg_n)
        self.show_operation_status(operation_status,
                                   key_words=["livre", "supprimé"])

        print("delete book")

    def search_books(self, hack):
        "This is the function for books searching. To be defined later"
        print("Searching for book")
        author, price, user_mle, classe, m_status = None, None, None, None, None

        if (self.is_author_checked.get() == 1):
            author = self.auth_spbox.get()
        if self.is_price_checked.get() == 1:
            price = self.price_spbox.get()
        if self.is_user_checked.get() == 1:
            user_mle = self.pret_spbox.get()
        if self.is_classe_checked.get() == 1:
            classe = self.classe_spbox.get()
        if self.is_dispo_checked.get() == 1:
            m_status = self.is_dispo_checked()

        query_result = m_db.search_book(author, price, user_mle, classe, m_status)
        self.display_result(query_result)

    ##        return query_result

    def empty_fields(self):
        self.mlb.delete(0, tkinter.END)

    def display_result(self, results):

        # emptying fields from all previous data before displaying new results

        self.empty_fields()

        for result in results:
            print(result)
            reg_num = result[0]
            isbn = result[1]
            author = result[2]
            name = result[3]
            price = result[4]
            classe = result[5]
            status = str(result[6])
            disp_stat = ''
            date_pret = ''
            cur_user = ''

            if status == self.BOOK_AVAILABLE:
                disp_stat = "Oui"
            else:
                disp_stat = "Non"
                # We must fetch lending date

                cur_user = m_db.get_current_user(reg_num)
                date_pret = m_db.get_lend_date(reg_num)  # we have a list object here
                print("date_pret is :", str(date_pret))
                # then a tuple object
                # which first element is a datetime object
                date_pret = date_pret[0][0]
                    #.strftime("%d-%m-%Y %H-%M-%S")

            entry = [reg_num, name, author, price, classe, disp_stat, date_pret, cur_user]
            # None values lead to error. So we will replace them by ''
            for i in range(0, len(entry)):
                if entry[i] == None:
                    entry[i] = ''
            print("our entry is : ", entry)
            self.mlb.insert(tkinter.END, *entry)

    def who_are_we(self):
        print("who are we ? ")
        my_message = tkinter.messagebox.Message(self.wind, title="BiblioPMB 1.0",
                                                message="""This software is developped by Lt SINGBO Israel.\
                                                        \nTel:+22997816156\
                                                        \ne-mail: sisra1993@yahoo.fr""")
        my_message.show()

        # tkinter.messagebox.showinfo(title="Info 2", message="This software is developped by Lt SINGBO Israel.\n Tel:+22997816156")

    ##  Creating tables and views

    def check_book_existence(self, reg_num=None):
        existence = False
        print("saved books : ", saved_books)
        # actually every item of the saved_books list is a tuple
        # so only the first element of this tuple is what we really need
        for i in saved_books:
            # print(str(reg_num), str(i[0]))
            if str(i) == str(reg_num):
                existence = True
                break
        return existence

    def confirm_save(self):
        book_exists = self.check_book_existence(m_book.get_reg_num())
        stat = self.status.get()
        if stat == None:
            stat = 2
        print("checked status is : " + stat + ".")
        m_title = "Sauvegarder"
        m_message = "Voulez-vous sauvegarder ce livre ? "
        if book_exists:
            m_title = "Mise à jour"
            m_message = "Ce numéro a déjà été attribué à un livre. Voulez-vous procéder à cette mise à jour ?"
        should_save = tkinter.messagebox.askokcancel(title=m_title, message=m_message)
        if should_save:
            self.save_book(book_exists)
        else:
            pass

    def confirm_delete(self):
        should_del = tkinter.messagebox.askyesno(title="Suppression de livre",
                                                 message="Etes-vous sûr de vouloir supprimer ce livre ?")
        if should_del:
            self.delete_book(True)

    ##    def confirm_update(self):
    ##        should_update = tkinter.messagebox.askyesno(title="Mise à jour", message="Voulez-vous enregistrer les modifications ?")
    ##        if should_update:
    ##            self.update_book()
    ##
    def cancel_without_saving(self):
        should_cancel = tkinter.messagebox.askyesno(title="Annuler l'édition",
                                                    message="Voulez-vous annuler vos modifications ?")
        if should_cancel:
            self.abort_book(True)

    def confirm_exit(self):
        should_exit = tkinter.messagebox.askyesno(title="Quitter", message="Voulez-vous quitter sans sauvegarder ?")
        if should_exit:
            self.leave_soft(self)


class MyDialog:
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
        top.title("Nouvel utilisateur")
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

        self.first_entry_f.pack(anchor='e', padx=10, pady=5)
        self.second_entry_f.pack(anchor='e', padx=10, pady=5)
        m_frame = tkinter.Frame(top)
        m_frame.pack(fill='x', padx=5, pady=10)

        self.ok_btn = tkinter.Button(m_frame, text="OK", width=10,
                                     command=lambda: self.ok_command(m_command))
        self.cancel_btn = tkinter.Button(m_frame, text="Cancel", width=10,
                                         command=self.cancel_command)

        self.ok_btn.pack(side='left', fill='y', padx=25)
        self.cancel_btn.pack(side='right', fill='y', padx=25)
        # top.mainloop()

    def ok_command(self, m_command):
        if m_command == None:
            self.user_mle = self.first_entry_f.get()
            self.user_name = self.second_entry_f.get()
            operation_status = m_db.add_user_to_db(self.user_mle, self.user_name)
            main_interface.show_operation_status(operation_status, ["utilisateur", "ajouté"])
            if operation_status == config.RESULT_OK:
                main_interface.pret_spbox.insert(len(users), str(self.user_mle))
                users.append(self.user_mle)
        else:
            return m_command()
        self.top.destroy()

    def cancel_command(self):
        self.top.destroy()


if __name__ == "__main__":

    # Setting path for bundled app
    path_to_bundle = path.abspath(path.dirname(__file__))

    # adding types for the update_list() method
    TYPE_AUTHOR = "author"
    TYPE_BOOK = "book"
    TYPE_USER = "user"
    TYPE_PRICE = "price"

    # adding actions for the update_list() method
    ACTION_ADD = "add"
    ACTION_REMOVE = "remove"

    m_book = Book()

    m_db = Mabd(host='localhost',  # connecting to db and creating inexistant tables
                user='root',
                passwd='')
    m_db.connect()
    m_db.create_tables_if_not_exist()

    saved_books = []  # Getting list of books user has saved
    for bk in m_db.get_saved_books_reg_num():
        saved_books.append(bk[0])
    users = []
    for user in m_db.get_users():
        users.append(user[0])
    authors = []
    for auth in m_db.get_authors():
        authors.append(auth[0])
    prices = []
    for pr in m_db.get_prices():
        prices.append(pr[0])
    classes = ["Tle", "1ere", "2nde", "3eme", "4eme", "5eme", "6eme"]
    print("users", users)
    print("authors", authors)
    print("prices", prices)
    print("saved books", saved_books)

    main_interface = Interface()

    main_interface.program_entry()
