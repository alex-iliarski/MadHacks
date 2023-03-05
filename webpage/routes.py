from webpage import app
from flask import render_template, redirect, url_for, flash
from webpage import db
from webpage.forms import QueryForm, TextMessageForm
from webpage.query import find_doctors, get_doc_by_id


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
        query_distance = int(form.distance.data)
        query_specialization = form.specialization.data
        query_years_experience = int(form.years_experience.data)
        query_insurance = form.insurance.data
        query_lang = form.lang.data
        query_gender = form.gender.data

        if query_insurance == None:
            query_insurance = ""
        if query_lang == None:
            query_lang = ""
        if query_gender == None:
            query_gender = ""

        docs = find_doctors(query_zipcode, 
                            within_miles=query_distance, 
                            specialization=query_specialization, 
                            years_of_experience=query_years_experience, 
                            insurence=query_insurance,
                            language=query_lang,
                            gender=query_gender)

        return query_results(docs)
    
    if form.errors != {}:  # If there are errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('docquery.html', form=form)

@app.route('/query_results')
def query_results(doctors):
    return render_template('query_results.html', doctors = doctors)

@app.route('/doctor/<doctor_id>')
def doctor(doctor_id):
    form = TextMessageForm()
    doc = get_doc_by_id(doctor_id)
    return render_template('doctor.html', form=form, doctor = doc)