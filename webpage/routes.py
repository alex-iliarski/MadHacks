from webpage import app
from flask import render_template, redirect, url_for, flash
from webpage import db
from flask_login import login_user, logout_user, login_required
from webpage.forms import QueryForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/docquery', methods=["GET", "POST"])
def docquery():
    form = QueryForm()

    
    if form.validate_on_submit():
        # # make query and redirect to results page
        # query_to_create = None
        # return redirect(url_for('query_results'))
        return redirect(url_for('docquery'))
    
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('docquery.html', form=form)

# <!-- {{ form.lang.label() }}
#                 {{ form.zipcode(<select class="form-select" aria-label="Default select example">
#                     <option selected>Open this select menu</option>
#                     <option value="1">One</option>
#                     <option value="2">Two</option>
#                     <option value="3">Three</option>
#                   </select>) }}
#                  -->
                
#                 <!-- {{ form.submit(class="btn btn-lg btn-primary btn-block") }} -->