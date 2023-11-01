import sqlite3

def create_table():
    database = sqlite3.connect("mydb.db")
    cursor = database.cursor()
    query= """CREATE TABLE users(id INT PRIMARY KEY,
    username TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT NOT NULL,
    isadmin INTEGER,
    createdat TEXT DEFAULT CURRENT_TIMESTAMP)"""
    cursor.execute(query)
    database.commit()

def insert_records(data):
    database = sqlite3.connect("mydb.db")
    cursor = database.cursor()
    query = """INSERT INTO users (id, username, email, password, isadmin) VALUES(?, ?, ?,?, ?)"""
    cursor.executemany(query, data)
    database.commit()

def insert_record(data):
 query = """INSERT INTO users (id, username, email, password, isadmin) VALUES(?, ?, ?,?, ?)"""
 cursor.execute(query, data)
 database.commit()

def get_all_users():
    users=[]
    try:
        conn = sqlite3.connect('mydb.db')
        cursor = conn.cursor()
        query = """SELECT * FROM users """
        cursor.execute(query)
        users = cursor.fetchall()
        return users
    except sqlite3.Error as err:
        print('Database Error', err)       
    finally:
        if conn != None:
            conn.close()
    return users
def get_all_posts():
    blogs=[]
    try:
        conn = sqlite3.connect('mydb.db')
        cursor = conn.cursor()
        query = """SELECT * FROM blogs """
        cursor.execute(query)
        blogs = cursor.fetchall()
        return blogs
    except sqlite3.Error as err:
        print('Database Error', err)       
    finally:
        if conn != None:
            conn.close()
    return blogs
def delete_user_by_id(id):                                                                                                           
    success=True
    try:
        conn = sqlite3.connect('mydb.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE id = ?;", (id,))
        conn.commit()        
    except sqlite3.Error as err:
        print('Database Error', err)
        success=False
    finally:
        if conn != None:
            conn.close()
    return success
def delete_blog_by_id(id):                                                                                                           
    success=True
    try:
        conn = sqlite3.connect('mydb.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM blogs WHERE id = ?;", (id,))
        conn.commit()        
    except sqlite3.Error as err:
        print('Database Error', err)
        success=False
    finally:
        if conn != None:
            conn.close()
    return success

def check_user(username,password):
    user=None
    try:
        conn = sqlite3.connect('mydb.db')
        cur = conn.cursor()
        cur.execute("Select * FROM users WHERE username=? AND password=?", (username,password,)),
        user = cur.fetchone()
    except sqlite3.Error as err:
        print('Database error', err)
    finally: 
        if conn != None:
            conn.close()
    return user

def user_add(user,email,password, isadmin):                                                                                                           
    success=True
    try:
        conn = sqlite3.connect('mydb.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, email, password,isadmin) VALUES (?,?,?,?)", (user,email,password,isadmin))
        conn.commit()        
    except sqlite3.Error as err:
        print('Database Error', err)
        success=False
    finally:
        if conn != None:
            conn.close()
    return success

def blog_add(blog_title,blog_user,blog_content):                                                                                                           
    success=True
    try:
        conn = sqlite3.connect('mydb.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO blogs (blog_title, blog_user, blog_content) VALUES (?,?,?)", (blog_title,blog_user,blog_content))
        conn.commit()        
    except sqlite3.Error as err:
        print('Database Error', err)
        success=False
    finally:
        if conn != None:
            conn.close()
    return success


def update_user(username,email,password, isadmin,id):
    success=True
    try:
        conn = sqlite3.connect('mydb.db')
        cur = conn.cursor()       
        cur.execute('''UPDATE users SET username =?, email=?, password=?, isadmin=? WHERE id=?''', (username,email,password,isadmin,id,))
        conn.commit()        
    except sqlite3.Error as err:
        print('save_user error', err)
        success=False
    finally:
        if conn != None:
            conn.close()
    return success
def get_user(id):
    user=None
    try:
        conn = sqlite3.connect('mydb.db')
        cur = conn.cursor()
        cur.execute("Select * FROM users WHERE id=?", (id,))
        user = cur.fetchone()      
    except sqlite3.Error as err:
        print('Database Error', err)        
    finally:
        if conn != None:
            conn.close()
    return user
 
def edit_blog(blog_title,blog_content):
    success=True
    try:
        conn = sqlite3.connect('mydb.db')
        cur = conn.cursor()       
        cur.execute('''UPDATE blogs SET blog_title =?, blog_content=? WHERE id=?''', (blog_title,blog_content))
        conn.commit()        
    except sqlite3.Error as err:
        print('edit_blog error', err)
        success=False
    finally:
        if conn != None:
            conn.close()
    return success
def get_posts(posts):
    user=None
    try:
        conn = sqlite3.connect('mydb.db')
        cur = conn.cursor()
        cur.execute("Select * FROM blogs WHERE id=?", (posts,))
        user = cur.fetchone()      
    except sqlite3.Error as err:
        print('Database Error', err)        
    finally:
        if conn != None:
            conn.close()
    return posts
 