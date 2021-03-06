from flask import Flask, render_template, request, redirect, session
import sys
import os
from utils import *
from utils import dynamodb_utils, get_summary


app = Flask(__name__, template_folder = 'html_src/')

app.secret_key = os.urandom(12).hex()

@app.route('/', methods = ['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        #Get the details of the user
        user_id = request.form['UserID']
        password = request.form['Password']

        
        ret_val = dynamodb_utils.verify_login(user_id, password)

        #User does not exist
        if ret_val == 0:
            return render_template('login_failed.html', reason = "User does not exist. Try again.")

        #password is wrong
        elif ret_val == 1:
            return render_template('login_failed.html', reason = "Password was wrong. Try again.")

        #Login successful, go to home page
        else:
            session['username'] = user_id
            return redirect("/Home")

    else:
        return render_template('login.html')

#Processing the sign up request
@app.route('/SignUp', methods = ['GET', 'POST'])
def new_user():
    try:
        if request.method == 'POST':
            #Get the details of the user
            user_id = request.form['UserID']
            password = request.form['Password']

            # print ("User ID and password : {} and {}".format(user_id, password))
            ret_val = dynamodb_utils.add_user_to_db(user_id, password)

            #Successful Sign Up template to be rendered
            if ret_val == 2:
               
                return render_template('signup_success.html')

            #Failure in signing up template to be rendered

            else:

                if ret_val == 0:
                    reason = "Username or password cannot be blank"

                else:
                    reason = "User already exists"
                
                return render_template('failed.html', reason = reason)

        else:
                return render_template('signup.html')
                

    except:
        return "Internal Server Error"




@app.route('/Home', methods = ['GET', 'POST'])
def render_home():

    if request.method == 'POST':

        user_id = session['username']

        url = request.form['URL']

        dynamodb_utils.add_bookmark(user_id, url)

    return render_template('home.html')

@app.route('/Bookmarks', methods = ['GET', 'POST'])
def display_bookmarks():
    #Get user

    user_id = session['username']

    summaries = dynamodb_utils.get_summaries(user_id)

    arr = list()

    for item in summaries:
        tup = (item["url"], item["title"], item["summary"])
        arr.insert(0, tup)

    return render_template('show_bookmarks.html', details = arr)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)
