#################################################################
# Module defining some classes and methods for my librairy      #
#                  database management                          #
# author : SINGBO Israel                                        #
#   e-mail: sisra1993@yahoo.fr                                  #
#   tel   : +22997816156                                        #
# date : 16/11/2019                                             #
#################################################################

# *-* encoding:utf-8 *-*
import mysql.connector

class Mabd:
    def __init__(self, host=None, user=None, passwd=None):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.mycursor = None
        self.mydb = None

    def connect(self):
        mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd)
        mycursor = mydb.cursor()
        #mycursor.execute("DROP DATABASE IF EXISTS books_db")
        mycursor.execute("CREATE DATABASE IF NOT EXISTS books_db")
        mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database='books_db')
        mycursor = mydb.cursor()
        self.mycursor = mycursor
        self.mydb = mydb

    def create_tables_if_not_exists(self):
        mycursor = self.mycursor
        try :
            
            # table Bibliotheque
            mycursor.execute("""CREATE TABLE IF NOT EXISTS BIBLIOTHEQUE(name VARCHAR(100) NOT NULL,
                             number_of_books INTEGER,
                             manager VARCHAR(100),
                             PRIMARY KEY (name) )""")
            # table livre
            mycursor.execute("""CREATE TABLE IF NOT EXISTS LIVRE (reg_num INTEGER NOT NULL,
                                isbn VARCHAR(13) NOT NULL,
                                author VARCHAR(100),
                                name VARCHAR(100),
                                price VARCHAR(100),
                                classe VARCHAR(15),
                                status VARCHAR(1) CHECK (status IN ('0','1')),
                                                        PRIMARY KEY(reg_num))""")
            # table user
            mycursor.execute("""CREATE TABLE IF NOT EXISTS USER(mle INTEGER,
                             name_surname VARCHAR(100),
                             PRIMARY KEY (mle))""")
            # table author
            mycursor.execute("""CREATE VIEW AUTHORS AS (SELECT isbn,
                             name, author FROM LIVRE)""")
            # table exemplaries
            mycursor.execute("""CREATE VIEW IF NOT EXISTS EXEMPLARIES AS (SELECT name,
                             COUNT(*) FROM LIVRE GROUP BY name)""")
            # table books_read
            mycursor.execute("""CREATE TABLE IF NOT EXISTS BOOKS_READ(
                             reg_num VARCHAR(13) NOT NULL,
                             reader_mle INTEGER,
                             FOREIGN KEY (isbn) REFERENCES LIVRE(isbn),
                             FOREIGN KEY (reader_mle) REFERENCES USER(mle)
                             )""")
            # table books_lent
            mycursor.execute("""CREATE TABLE IF NOT EXISTS BOOKS_LEND(
                             reg_num VARCHAR(13) NOT NULL,
                             user_mle INTEGER,
                             lend_date DATETIME,
                             FOREIGN KEY (reg_num) REFERENCES LIVRE(reg_num),
                             FOREIGN KEY (user_mle) REFERENCES USER(mle))""")
            ##    mycursor.execute("CREATE VIE"
            ##        mycursor.execute("SHOW DATABASES")
        except:
            print("An error occured, but we keep moving on")

    def add_book_to_db(self,
                    reg_num = None,
                    name = None,
                    author = None,
                    price = None,
                    isbn = None,
                    classe = None,
                    user_number = None,
                    status = None ) :
        query_insert_into_books = """INSERT INTO LIVRE(reg_num,
                                        isbn,
                                        author,
                                        name,
                                        price,
                                        classe,
                                        status)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        val = (reg_num, isbn, author, name, price, classe, status)
        self.mycursor.execute(query_insert_into_books, val)
        self.mydb.commit()
        print("book succesfully added")

    def delete_book(self, reg_num):
        query_delete_book = """DELETE FROM LIVRE WHERE reg_num = %s"""
        val = (reg_num,)
        self.mycursor.execute(query_delete_book, val)
        self.mydb.commit()

    def search_book(self,
                    book_author=None,
                    book_price=None,
                    book_user=None,
                    book_classe=None,
                    book_status=None):
        query_search_book_with_users = "SELECT * FROM LIVRE,BOOKS_LENT WHERE "
        query_search_book_simple = "SELECT * FROM LIVRE WHERE "
        query_search_book_without_criteria = "SELECT * FROM LIVRE"
        query_search_book = ""
        if book_user == None :
            query_search_book = query_search_book_simple
        else :
            query_search_book = query_search_book_with_users()

        criterias = []
        total_crit = {"author":book_author,
                     "price":book_price, "user_mle":book_user,
                     "classe":book_classe, "status":book_status}
        valid_criteres = {}
        criteres_tuple = total_crit.items()
        all_crit_none = True
        for key,value in criteres_tuple:
            if value is not None :
                all_crit_none = False
                valid_criteres[key] = value
                query_search_book += key +"=%s AND "

        if all_crit_none :
            query_search_book = query_search_book_without_criteria
        elif book_user == None :
            # Time to remove the last training "AND "
            query_search_book = query_search_book[:-4]
        else :            
            query_search_book += "LIVRE.isbn=BOOKS_LENT.isbn"
        print("query search is ",query_search_book)
        
        values = tuple(valid_criteres.values())
        self.mycursor.execute(query_search_book, values)
        myresult = self.mycursor.fetchall()
        for result in myresult:
            print(result)
        return myresult

    def search_user(self, mle=None):
        query_search_user = "SELECT * FROM USER WHERE mle = %s"
        value = (mle,)
        self.mycursor.execute(query_search_user, value)
        result = self.mycursor.fetchall()
        return result
                        

    def update_book_user(self, reg_num=None, user_mle=None):
        query = """INSERT INTO BOOKS_LENT (reg_num,
                    mle,
                    lend_date)
                    VALUES (%s, %s, NOW())"""
        values = (reg_num, user_mle,)
        self.cursor.execute()
        self.mydb.commit()

    def add_user_to_db(self, mle, name):
        query = """INSERT INTO USER
                    (
                        mle,
                        name_surname
                    ) VALUES
                    (
                        %s, %s
                    )"""
        values = (mle, name,)
        self.cursor.execute()
        self.mydb.commit()

    def delete_entry_from_table(self,
                                table_name=None,
                                entry_name=None,
                                entry_value=None):
        """
            Deletes any given entry from any given table when the
            'WHERE' condition is only one column
        """
        query = "DELETE FROM %s WHERE %s = %s"
        values = (table_name, entry_name, entry_value)
        self.cursor.execute(query, values)
        self.mydb.commit()
        
    def update_books_read(self,
                          reg_num=None,
                          reader_mle=None):
        query = """
                    INSERT INTO BOOKS_READ
                    (
                        reg_num,
                        reader_mle
                    )
                    VALUES (%s, %s)
                """
        values = (reg_num, reader_mle,)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def update_book(self,
                    reg_num = None,
                    name = None,
                    author = None,
                    price = None,
                    isbn = None,
                    classe = None,
                    user_number = None,
                    status = None):
        print("book updated")

        

