from flask import Flask, render_template, request, redirect, session

#Home Page
@app.route('/Signup', methods = ['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        #Get the details of the user
        user_id = request.form['UserID']
        password = request.form['Password']

        ret_val = add_user_to_db(user_id, password)

        