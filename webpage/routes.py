from webpage import app
from flask import render_template, redirect, url_for, flash
from webpage import db
from webpage.forms import QueryForm, TextMessageForm
from flask import render_template, flash
from webpage.forms import QueryForm
from webpage.query import find_doctors, get_doc_by_id
from flask_googlemaps import Map, GoogleMaps, icons


@app.route('/')
@app.route('/home')
def home():
    map = Map(
        identifier="map",
        lat=43.0666775,
        lng=-89.4066381,
        zoom=12,
        style="height:800px;width:100%;margin:0;",
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 37.4419,
             'lng': -122.1419,
             'infobox': "<p>Hello World</p>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<p>Hello World from other place</p>"
          }
        ]
    )
    return render_template('home.html', map=map)

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