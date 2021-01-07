from flask import Flask, render_template, request, make_response, session,redirect, url_for

app=Flask(__name__)
app.secret_key='any random string'

#when this function called we will see str function on the main page because the route is '/'
@app.route ('/')
def index0():
    str="""
<html>
    <body>
        <h1> My works on Flask to check other functions change the route like "  /1  " </h1>
    </body>
</html>

"""
    return str


###################################################

#it is calling helloworld.html file from templates
@app.route ('/1')
def index1():
    return render_template('helloworld.html')
###################################################

#static file also using js
@app.route ('/2')
def index2():
    return render_template('index.html')

###################################################
@app.route ('/3student')
def index3student():
    return render_template('student.html')

@app.route('/3result', methods=['POST','GET'])
def index3result():
    if request.method=='POST':
        result=request.form

        return render_template("result.html", result=result)

###################################################33
@app.route('/4')
def index4():
    return render_template('setcookie.html')

@app.route('/setcookie', methods=['POST','GET'])
def setcookie():
    if request.method =='POST':
        user=request.form['nm']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)
        return resp

@app.route('/getcookie')
def getcookie():
    name=request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'

###################################################

@app.route('/5',methods=['GET', 'POST'])
def index5():
    if 'username' in session:
        username= session['username']
        return ' Logged in as'+username+'<br> <b> <a href="/logout">click here to logout </a> </b>'
    return "You are not logged in <br> <a href='/login'> <b>click here to log in </b> </a>"

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        session['username']=request.form['username']
        return redirect(url_for(index5))
    return render_template('session.html')

@app.route('/logout',methods=['GET', 'POST'])
def logout():
    session.pop('username',None)
    return redirect(url_for(index5))


if __name__=='__main__':
    app.run(debug=True)