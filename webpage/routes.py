from webpage import app
from flask import render_template, redirect, url_for, flash, request
from webpage.forms import QueryForm, TextMessageForm
from webpage.query import find_doctors, get_doc_by_id
from webpage.dist import get_lat_long
from webpage.query import find_doctors, get_doc_by_id, get_all_docs
from flask_googlemaps import Map, GoogleMaps, icons
from webpage.twillio import message_doc, contact_us
from random import randint


def make_all_markers():
    ret = []
    all_doctors = get_all_docs()
    for doctor in all_doctors:
        plus_or_minus = lambda: 1 if randint(0, 1) == 0 else -1
        rand_offset = randint(0, 100) / 100000 * plus_or_minus()
        loc_dict = get_lat_long(doctor["address"]["street"]+" "+doctor["address"]["city"]+" "+doctor["address"]["state"]+" "+doctor["address"]["zip"])
        ret.append({
            'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
            'lat': loc_dict["lat"]+rand_offset,
            'lng': loc_dict["lng"]+rand_offset,
            'infobox': f"""
            <div>
            <b style=\"color:black; text-align: center; \">{doctor['first_name']} {doctor['last_name']}</b> <br>
            <img src=\"{doctor['avatar_url']}\" style=\"float:left; height: 100px; width 50px;\"> <br>
            <a href="{url_for('doctor', doctor_id=doctor["_id"])}" style=\"float:left;\">More Info</a>
            </div>
            """
        })
    return ret

def make_specific_markers(doctors):
    ret = []
    for doctor in doctors:
        plus_or_minus = lambda: 1 if randint(0, 1) == 0 else -1
        rand_offset = randint(0, 100) / 100000 * plus_or_minus()
        loc_dict = get_lat_long(doctor["address"]["street"]+" "+doctor["address"]["city"]+" "+doctor["address"]["state"]+" "+doctor["address"]["zip"])
        ret.append({
            'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
            'lat': loc_dict["lat"]+rand_offset,
            'lng': loc_dict["lng"]+rand_offset,
            'infobox': f""" 
            <div>
            <b style=\"color:black; text-align: center; \">{doctor['first_name']} {doctor['last_name']}</b> <br>
            <img src=\"{doctor['avatar_url']}\" style=\"float:left; height: 100px; width 50px;\"> <br>
            <a href="{url_for('doctor', doctor_id=doctor["_id"])}" style=\"float:left;\">More Info</a>
            </div>
            """
        })
    return ret


@app.route("/")
@app.route("/home")
def home():
    map = Map(
        identifier="map",
        lat=43.0666775,
        lng=-89.4066381,
        zoom=12,
        style="height:800px;width:100%;margin:0;",
        center_on_user_location=True,
        markers=make_all_markers()
    )
    return render_template("home.html", map=map)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    form = TextMessageForm()
    if request.method == "POST":
        if form.validate_on_submit():
            phone_number = form.phone.data
            name = form.name.data
            message = (
                "Message from "
                + name
                + " at "
                + phone_number
                + ": "
                + form.message.data
            )

            contact_us(message)
            flash(
                "Message sucessfully sent to developers, they should be getting back to you shortly!",
                category="success",
            )
            return redirect(url_for("contact"))
        flash(
            "Message not sent, There was an error in your phone number",
            category="danger",
        )
        return redirect(url_for("contact"))

    else:
        return render_template("contact.html", form=form)


@app.route("/docquery", methods=["GET", "POST"])
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

        if query_insurance == None:
            query_insurance = ""
        if query_lang == None:
            query_lang = ""
        if query_gender == None:
            query_gender = ""

        if query_distance == "":
            query_distance = 50
        else:
            query_distance = int(query_distance)

        if query_years_experience == "":
            query_years_experience = 0
        else:
            query_years_experience = int(query_years_experience)

        docs = find_doctors(
            query_zipcode,
            within_miles=query_distance,
            specialization=query_specialization,
            years_of_experience=query_years_experience,
            insurence=query_insurance,
            language=query_lang,
            gender=query_gender,
        )

        return query_results(docs, query_zipcode)

    if form.errors != {}:  # If there are errors from the validations
        for err_msg in form.errors.values():
            flash(
                f"There was an error with creating a user: {err_msg}", category="danger"
            )

    return render_template("docquery.html", form=form)


@app.route("/query_results")
def query_results(doctors, query_zipcode):
    lat_long = get_lat_long(query_zipcode)
    map = Map(
        identifier="query_map",
        lat=lat_long["lat"],
        lng=lat_long["lng"],
        zoom=12,
        style="height:800px;width:100%;margin:0;",
        markers=make_specific_markers(doctors)
    )
    return render_template("query_results.html", doctors=doctors, map=map)


@app.route("/doctor/<doctor_id>", methods=["GET", "POST"])
def doctor(doctor_id):
    form = TextMessageForm()
    doc = get_doc_by_id(doctor_id)
    if request.method == "POST":
        if form.validate_on_submit():
            phone_number = form.phone.data
            name = form.name.data
            message = (
                "Message from "
                + name
                + " at "
                + phone_number
                + ": "
                + form.message.data
            )

            message_doc(doc, message)
            flash(
                "Message sucessfully sent to the doctor, they should be getting back to you shortly!",
                category="success",
            )
            return redirect(url_for("doctor", doctor_id=doctor_id))
        flash(
            "Message not sent, There was an error in your phone number",
            category="danger",
        )
        return redirect(url_for("doctor", doctor_id=doctor_id))

    else:
        return render_template("doctor.html", form=form, doctor=doc)
