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
import config

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
        print("database succesfully deleted")
        mycursor.execute("CREATE DATABASE IF NOT EXISTS books_db")
        print("database succesfully added")
        mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database='books_db')
        mycursor = mydb.cursor()
        self.mycursor = mycursor
        self.mydb = mydb

    def create_tables_if_not_exist(self):
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
            mycursor.execute("""CREATE VIEW AUTHORS AS SELECT reg_num,
                             author FROM LIVRE""")
            # table exemplaries
            mycursor.execute("""CREATE VIEW EXEMPLARIES AS (SELECT name,
                             COUNT(*) FROM LIVRE GROUP BY name)""")
            # table books_read
            mycursor.execute("""CREATE TABLE IF NOT EXISTS BOOKS_READ(
                             reg_num INTEGER NOT NULL,
                             reader_mle INTEGER,
                             FOREIGN KEY (reg_num) REFERENCES LIVRE(reg_num),
                             FOREIGN KEY (reader_mle) REFERENCES USER(mle)
                             )""")
            # table books_lend
            mycursor.execute("""CREATE TABLE IF NOT EXISTS BOOKS_LEND(
                             reg_num INTEGER NOT NULL,
                             user_mle INTEGER,
                             lend_date DATETIME,
                             FOREIGN KEY (reg_num) REFERENCES LIVRE(reg_num),
                             FOREIGN KEY (user_mle) REFERENCES USER(mle))""")
            return config.RESULT_OK
        except Exception as e:
            print("An error occured : ", str(e))
            return config.RESULT_ERROR

    def add_book_to_db(self,
                    reg_num = None,
                    name = None,
                    author = None,
                    price = None,
                    isbn = None,
                    classe = None,
                    user_number = None,
                    status = None ) :
        try:
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
            return config.RESULT_OK
        except Exception as e:
            print("An error occured : ", str(e))
            return config.RESULT_ERROR

    def update_book(self,
                        reg_num = None,
                        name = None,
                        author = None,
                        price = None,
                        isbn = None,
                        classe = None,
                        user_number = None,
                        status = None ) :
        try:
            query_insert_into_books = """
                                        UPDATE LIVRE SET
                                        isbn = %s,
                                        author = %s,
                                        name = %s,
                                        price = %s,
                                        classe = %s,
                                        status = %s
                                        WHERE reg_num = %s
                                        """
            val = (isbn, author, name, price, classe, status, reg_num)
            self.mycursor.execute(query_insert_into_books, val)
            self.mydb.commit()
            print("book succesfully updated\n", self.mycursor.rowcount, " record(s) affected")
            return config.RESULT_OK
        except Exception as e:
            print("An error occured : ", str(e))
            return config.RESULT_ERROR



    def delete_book(self, reg_num):
        try:
            query_delete_book = """DELETE FROM LIVRE WHERE reg_num = %s"""
            val = (reg_num,)
            self.mycursor.execute(query_delete_book, val)
            self.mydb.commit()
            return config.RESULT_OK
        except Exception as e:
            print("An error occured : ", str(e))
            return config.RESULT_ERROR


    def search_book(self,
                    book_author=None,
                    book_price=None,
                    book_user=None,
                    book_classe=None,
                    book_status=None):
        query_search_book_with_users = "SELECT * FROM LIVRE,BOOKS_LEND WHERE "
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
            query_search_book += "LIVRE.isbn=BOOKS_LEND.isbn"
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
        try:
            query = """INSERT INTO BOOKS_LEND (reg_num,
                        user_mle,
                        lend_date)
                        VALUES (%s, %s, NOW())"""
            values = (reg_num, user_mle,)
            self.mycursor.execute(query, values)
            self.mydb.commit()
            return config.RESULT_OK
        except Exception as e:
            print("An error occured : ", str(e))
            return config.RESULT_ERROR


    def add_user_to_db(self, mle, name):
        try :
            query = """INSERT INTO USER
                        (
                            mle,
                            name_surname
                        ) VALUES
                        (
                            %s, %s
                        )"""
            values = (mle, name,)
            self.mycursor.execute()
            self.mydb.commit()
            return config.RESULT_OK
        except Exception as e:
            print("An error occured : ", str(e))
            return config.RESULT_ERROR

    def delete_entry_from_table(self,
                                table_name=None,
                                entry_name=None,
                                entry_value=None):
        """
            Deletes any given entry from any given table when the
            'WHERE' condition is only one column
        """
        try:
            query = "DELETE FROM %s WHERE %s = %s"
            values = (table_name, entry_name, entry_value)
            self.mycursor.execute(query, values)
            self.mydb.commit()
            return config.RESULT_OK
        except Exception as e:
            print("An error occured : ", str(e))
            return config.RESULT_ERROR
        
        
    def update_books_read(self,
                          reg_num=None,
                          reader_mle=None):
        print("reg_num : ", reg_num,"\nreader_mle : ", reader_mle)
        try :
            query = """
                        INSERT INTO BOOKS_READ
                        (
                            reg_num,
                            reader_mle
                        )
                        VALUES (%s, %s)
                    """
            values = (reg_num, reader_mle,)
            self.mycursor.execute(query, values)
            self.mydb.commit()
            return config.RESULT_OK
        except Exception as e:
            print("An error occured : ", str(e))
            return config.RESULT_ERROR


    def get_saved_books_reg_num(self):
        query = """
                    SELECT reg_num FROM LIVRE
                """
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()
        return result
    
    def get_users(self):
        query = """
                    SELECT mle FROM USER
                """
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()
        return result
    
    def get_authors(self):
        query = """
                        SELECT DISTINCT author FROM AUTHORS
                    """
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()
        return result

    def get_prices(self):
        query = """
                    SELECT DISTINCT price FROM LIVRE
                """
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()
        return result

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

        

