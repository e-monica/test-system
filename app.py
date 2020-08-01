from flask import Flask, escape, request, render_template
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def index():
	name = 'hello'
	return render_template('home.html', name=name)

#if __name__ == '__main__':
	#app.run(port=8000, debug=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form.get("email")
		password = request.form.get("password")
		doLogin(email, password)
		return render_template('home.html')
	else:
		return render_template('login.html')

def doLogin():
	if email == "elgawlymonica@gmail.com" and password == "password":
		return True
	else:
		return False