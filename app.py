from flask import Flask,render_template,request
app = Flask(__name__)

#1 Hello World!

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


#2 Static page navigation

@app.route('/launchpage')
def launch_page1():
    return render_template('index.html')

@app.route('/page1',methods=['POST'])
def launch_page2():
    return render_template('index1.html')


#3 URL parameter


@app.route('/user',methods=['GET'])
def print_user():
    data1=request.args.get('first_name')
    data2=request.args.get('last_name')
    return f"The name of the person is {data1,data2}"


#4 URL parameter


@app.route('/launchpage')
def launch_page():
    return render_template('index2.html')

@app.route('/userdata',methods=['POST'])
def input_data():
    data=request.form.get('input')
    return f"The data entered by the user is {data}"


#8

@app.route('/')
def login_page():
    return render_template('index3.html')
    
@app.route('/login',methods=['POST'])
def registration_page():
    name=request.form.get('username')
    password=request.form.get('password')
    return render_template('index4.html')

@app.route('/registration',methods=['POST'])
def confirmation():
    age=request.form.get('age')
    city=request.form.get('city')
    email=request.form.get('email')
    return f"The user has registered successfully with the details Age: {age}, City: {city} & EMAIL ID: {email}"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8001,debug=True)
