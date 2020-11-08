from flask import Flask, render_template, request, redirect, session
import sys
import os
from utils import *
from utils import add_user_to_db
#sys.path.append("..")


app = Flask(__name__, template_folder = '../html_src/')

#Home Page which is currently for signup
@app.route('/', methods = ['GET', 'POST'])
def default():
    return render_template('sign_up.html')

#Processing the sign up request
@app.route('/SignUp', methods = ['GET', 'POST'])
def new_user():
    try:
        if request.method == 'POST':
            #Get the details of the user
            user_id = request.form['UserID']
            password = request.form['Password']

            print ("User ID and password : {} and {}".format(user_id, password))
            ret_val = add_user_to_db.add_user_to_db(user_id, password)

            if ret_val == True:
                #return render_template('sign_up.html')
                return "User Added Successfully"

            else:
                #return render_template('failed.html')
                return "Failed to add user"
    except:
        return "Internal Server Error"


if __name__ == "__main__":

    app.run(debug = True)
