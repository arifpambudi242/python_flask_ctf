from flask import Flask, render_template, request, jsonify, render_template_string
from db_handler import DBHandler
app = Flask(__name__)

db = DBHandler()


@app.route("/")
def index():
  return render_template("index.html")

# register
@app.route("/register")
def register():
  return render_template("register.html")

# login
@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/hello", methods=["GET"])
def hello():
  name = request.args.get("name")
  return render_template_string("Hello, {}".format(name))

@app.route("/act_register", methods=["POST"])
def act_register():
  username = request.form["username"]
  password = request.form["password"]
  if db.get_user(username):
    return jsonify({"success": False, "message": "User {} already exists".format(username)})
  db.insert_user(username, password)
  return jsonify({"success": True, "message": "User {} registered successfully".format(username)})

@app.route("/act_login", methods=["POST"])
def act_login():
  username = request.form["username"]
  passwd = request.form["password"]
#   make it vulnerable to sql injection
  db.connect()
  sql_text = "SELECT * FROM users WHERE username = '{0}' AND password = '{1}'".format(username, passwd)
  db.cursor.execute(sql_text)
  print(sql_text)
  datas = db.cursor.fetchall()
  db.close()
  if datas:
    # redirect to welcome page
    # penjelasan cara inject sql ke halaman ini in bahasa
    """
    # menggunakan '='
    # username: admin'='
    # password: password
    # maka sql_text akan menjadi
    SELECT * FROM users WHERE username = 'admin'=' AND password = 'password'
    # menggunakan 'OR'

    # username: admin' OR '1'='1
    # password: password
    # maka sql_text akan menjadi
    SELECT * FROM users WHERE username = 'admin' OR '1'='1' AND password = 'password'

    # menggunakan 'OR' dan '--'
    # username: admin' OR '1'='1' --
    # password: password
    # maka sql_text akan menjadi
    SELECT * FROM users WHERE username = 'admin' OR '1'='1' --' AND password = 'password'
    # penjelasan
    -- adalah komentar di sql, maka sql_text akan menjadi
    SELECT * FROM users WHERE username = 'admin' OR '1'='1'
    
    """
    return jsonify({"success": True, 'message': "User {} logged in successfully".format(username)})
  return jsonify({"success": False, 'message': "Username or password is incorrect"})

# welcome page
@app.route("/welcome")
def welcome():
  return render_template("welcome.html")

# make route vulnerable to xss attack
@app.route("/search/<username>")
def search(username):
  return "Search result for {}".format(username)

if __name__ == "__main__":
  app.run(debug=True)
