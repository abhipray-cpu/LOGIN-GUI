import mysql.connector
from mysql.connector import errorcode
from mysql.connector import Error

import os
def insert_values(user_name, password):
    try:
        cnx = mysql.connector.connect(user='root', password=f"{os.environ(['Sql_Password'])}",
                                      host='localhost',
                                      database='tkinter_login')
        data_login = (user_name, password)
        query = "INSERT INTO login_details (user,password) VALUES (%s,%s)"
        cursor = cnx.cursor()
        cursor.execute(query, data_login)
        print("Abhi toe aur chlega")
        cnx.commit()
        print("Abhi bhi chl rha hai")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print("Insert operation failed tu toe lut gya re gotiya")


def fetch_values():
    try:
        cnx = mysql.connector.connect(user='root', password=f"{os.environ(['Sql_Password'])}",
                                      host='localhost',
                                      database='tkinter_login')
        query = "SELECT * from login_details"
        cursor = cnx.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        #print(result)
        return result  # this is a list of tuple therfore for each value extraced you can gain further access to other two values of tuple
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print("Insert operation failed tu toe lut gya re gotiya")


def fetch_single(user, password):
    try:
        cnx = mysql.connector.connect(user='root', password=f"{os.environ(['Sql_Password'])}",
                                      host='localhost',
                                      database='tkinter_login')
        data = (user,password)
        query = f"SELECT * FROM login_details WHERE user = %s AND password = %s"
        cursor = cnx.cursor()
        cursor.execute(query, data)
        result = cursor.fetchall()
        #print(result)
        return result

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()


def delete_funtion(user_delete,password):
    try:
        cnx = mysql.connector.connect(user='root', password=f"{os.environ(['Sql_Password'])}",
                                      host='localhost',
                                      database='tkinter_login')
        data = (user_delete,password)
        query = f'DELETE FROM login_details WHERE user = %s AND password = %s'
        cursor = cnx.cursor()
        cursor.execute(query, data)
        cnx.commit()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()


def update_function(old_user,old_password,user_name,new_password):
    # while performig this function do a validation ceck as well for the authenticity of user
    # perform a validation check first in here using the old password and user_name
    try:
        cnx = mysql.connector.connect(user='root', password=f"{os.environ(['Sql_Password'])}",
                                      host='localhost',
                                      database='tkinter_login')

        sql = "UPDATE login_details SET user = %s,password = %s WHERE user = %s AND password = %s"
        val = (user_name,new_password,old_user,old_password)
        mycursor = cnx.cursor()

        mycursor.execute(sql, val)
        cnx.commit()
        print("SQL updation successful!!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()

