from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Welcome Donovan!"}

@app.route('/about')
def about_user():
    information = request.args.get("information")
    email = request.args.get("email")
    return {"contact info": information, "email": email}




if __name__ == '__main__':
    app.run(debug=True, port=8000)
