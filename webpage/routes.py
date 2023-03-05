from webpage import app
from flask import render_template, redirect, url_for, flash
from webpage import db
# from flask_login import login_user, logout_user, login_required
from webpage.forms import QueryForm
from webpage.query import find_doctors


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
        query_zipcode = form.zipcode.data
        query_distance = form.distance.data
        query_specialization = form.specialization.data
        query_years_experience = form.years_experience.data
        query_insurance = form.insurance.data
        query_lang = form.lang.data
        query_gender = form.gender.data

        print(query_zipcode)
        print(query_distance)
        print(query_specialization)
        print(query_years_experience)
        print(query_insurance)
        print(query_lang)
        print(query_gender)

        docs = find_doctors(query_zipcode, 
                            within_miles=query_distance, 
                            specialization=query_specialization, 
                            years_of_experience=query_years_experience, 
                            insurence=query_insurance,
                            language=query_lang,
                            gender=query_gender)
        
        print(docs)

        return render_template(url_for('home'))
        # return redirect(url_for('query_results', doctors = docs))
    
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('docquery.html', form=form)
