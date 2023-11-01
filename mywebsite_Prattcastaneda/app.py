from flask import Flask, render_template, url_for, request, redirect, session

import db


app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'MYSECRETKEY'

@app.route('/', methods = ['POST', 'GET'])
def index():
    return  render_template('index.html')

@app.route('/cyber', methods = ['POST', 'GET'])
def cyber():
    return render_template('cyberdesign.html')

@app.route('/contact', methods = ['POST', 'GET'])
def contact():
    return render_template('contactme.html')

@app.route('/posts', methods = ('POST', 'GET'))
def posts():
    if session.get('loggedin') is None:
        return render_template('login.html')
    posts = db.get_all_posts()
    return render_template('blog.html', posts=posts)

@app.route('/login', methods = ("POST", "GET"))
def login():
   
    if request.method == 'POST':
       
        username = request.form['username']
        password = request.form['password']
        user = db.check_user(username,password)
        print(user)
        if user is None:
            return render_template('login.html')
        else:
           
            session['username'] = username
            session['isadmin'] = user[4]
            session['loggedin'] = 1
            if user[4] == 1: 
                users = db.get_all_users()              
                return render_template('admin_users.html', users=users) #admin user
            else:
                return render_template('index.html') #regular user
    else: 
        if session.get('isadmin') ==1:
            users = db.get_all_users()              
            return render_template('admin_users.html', users=users)
        else:           
            return render_template('index.html') #regular user
        return render_template('login.html') 
        

@app.route('/logout')
def logout():
    session.clear()
    return render_template('login.html')

#add user
@app.route('/user_add', methods=('GET', 'POST'))
def user_add():
    if session.get('isadmin')!=1:
        session.clear()
        return render_template('login.html')
    else: 
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            admin = request.form['admin']
            
            error = None

            if not username:
                error = "Username is required."
            elif not email:
                error = "Email is required."
            elif not password:
                error = "Password is required."

            if error is None:
                result = db.user_add(username,email,password, admin)
                if result==True:
                    users = db.get_all_users()    
                    return render_template('admin_users.html', users=users,   errormsg="User created successfully!")
                else:
                    error ="Failed to add a new user"
                    return render_template('user_add.html',   errormsg=error)
        else:
            return render_template("user_add.html")

#add user
@app.route('/blog_add', methods=('GET', 'POST'))
def blog_add():
    if session.get('loggedin') is None:
        session.clear()
        return render_template('login.html')
    else: 
        if request.method == 'POST':
            blog_title = request.form['blog_title']
            blog_user = session.get('username')
            blog_content = request.form['blog_content']
            
            
            error = None

            if not blog_title:
                error = "blog title is required."
            elif not blog_content:
                error = "blog_content is required."
            

            if error is None:
                result = db.blog_add(blog_title,blog_user,blog_content)
                if result==True:
                    posts = db.get_all_posts()    
                    return render_template('blog.html', posts=posts,msg="Blog created successfully!")
                else:
                    error ="Failed to add a new blog"
                    return render_template('blog_add.html',   msg=error)
        else:
            return render_template("blog_add.html")

@app.route('/user_update/<int:id>', methods=('GET', 'POST'))
def user_update(id):
    if session.get('isadmin')!=1:
        session.clear()
        return render_template('login.html')
    else: 
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            admin = request.form['admin']
            
            error = None

            if not username:
                error = "Username is required."
            elif not email:
                error = "Email is required."
            elif not password:
                error = "Password is required."

            if error is None:
                result = db.update_user(username,email,password, admin,id)
                if result==True:
                    users = db.get_all_users()    
                    return render_template('admin_users.html', users=users,   msg="User updated successfully!")
                else:
                    error ="Failed to save a new user"                
        else:
            user = db.get_user(id)    
            return render_template('user_update.html', user=user)


@app.route('/edit_blog/', methods=('GET', 'POST'))
def edit_blog():
    if session.get('isadmin')!=1:
        session.clear()
        return render_template('edit_blog.html')
    else: 
        if request.method == 'POST':
            blog_title = request.form['blog_title']
            blog_content = request.form['blog_content']
            
            error = None

            if not blog_title:
                error = "Blog title is required."
            elif not blog_content:
                error = "Content is required."

            if error is None:
                result = db.edit_blog(blog_tite,blog_content)
                if result==True:
                    posts = db.get_all_posts(posts)    
                    return render_template('blog.html', posts=posts,msg="Blog edited successfully!")
                else:
                    error ="Failed to edit blog"                
        else:
            posts = db.get_all_posts(posts)    
            return render_template('blog.html', posts=posts)

@app.route('/delete_user/<int:id>', methods=('POST', 'GET'))
def delete_user(id):
    result=db.delete_user_by_id(id)
    if result==True:
        msg='Successfully deleted'
        users = db.get_all_users()    
    else:
        msg='Not deleted successfully'
    return render_template('admin_users.html',users=users, msg=msg)

@app.route('/delete_blog/<int:id>', methods=('POST', 'GET'))
def delete_blog(id):
    result=db.delete_blog_by_id(id)
    if result==True:
        msg='Successfully deleted'
        posts = db.get_all_posts()    
    else:
        msg='Not deleted successfully'
    return render_template('blog.html',posts=posts, msg=msg)

if __name__ == "__main__":
    app.run(debug=True,port=8080)