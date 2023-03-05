from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    SelectField,
    SelectMultipleField,
)
from wtforms.validators import (
    Length,
    EqualTo,
    Email,
    DataRequired,
    ValidationError,
    Regexp,
)


def clean(str):
    return str.replace("_", " ").title()


class QueryForm(FlaskForm):
    def validate_zipcode(self, zipcode):
        if len(zipcode.data) != 5:
            raise ValidationError("Zipcode must be 5 digits long.")
        if not zipcode.data.isdigit():
            raise ValidationError("Zipcode must be numeric.")

    specializations = [
        "CARDIOLOGIST",
        "DENTIST",
        "DERMATOLOGIST",
        "ENDOCRINOLOGIST",
        "GASTROENTEROLOGIST",
        "GENERAL_PRACTITIONER",
        "GYNECOLOGIST",
        "HEMATOLOGIST",
        "INFECTIOUS_DISEASES_SPECIALIST",
        "NEPHROLOGIST",
        "NEUROLOGIST",
        "NEUROSURGEON",
        "OBSTETRICIAN",
        "ONCOLOGIST",
        "OPHTHALMOLOGIST",
        "ORTHOPEDIST",
        "OTORHINOLARYNGOLOGIST",
        "PEDIATRICIAN",
        "PHYSIATRIST",
        "PSYCHIATRIST",
        "RADIOLOGIST",
        "RHEUMATOLOGIST",
        "SURGEON",
        "UROLOGIST",
    ]

    insurances = [
        "",
        "ALINA_HEALTH",
        "ALLIANZ",
        "ASANATOARE",
        "BLUE_CROSS_BLUE_SHIELD",
        "CIGNA",
        "CIGNA",
        "MEDICARE",
        "MEDICAID",
        "MUTUAL_OF_OMAHA",
        "UNITED_HEALTHCARE",
        "KAISER_PERMANENTE",
        "ANTHEM",
        "HUMANA",
    ]
    langs = ["", "ENGLISH", "FRENCH", "GERMAN", "ITALIAN", "SPANISH"]
    genders = ["", "NO_PREFERENCE", "MALE", "FEMALE", "NON_BINARY"]

    specializations_choices = [
        (specialization, clean(specialization)) for specialization in specializations
    ]
    insurances_choices = [(insurance, clean(insurance)) for insurance in insurances]
    langs_choices = [(lang, clean(lang)) for lang in langs]
    genders_choices = [(gender, clean(gender)) for gender in genders]

    zipcode = StringField(
        label="Zipcode:", validators=[Length(min=5, max=5), DataRequired()]
    )
    distance = StringField(label="Within Miles:", validators=[Length(max=3)])
    specialization = SelectMultipleField(
        label="Specialization:", choices=specializations_choices, validators=[]
    )
    years_experience = StringField(
        label="Minimum Years of Experience:", validators=[Length(max=2)]
    )
    insurance = SelectField(
        label="Insurance:", choices=insurances_choices, validators=[]
    )
    lang = SelectField(
        label="Preferred Language: ", choices=langs_choices, validators=[]
    )
    gender = SelectField(
        label="Preferred Gender: ", choices=genders_choices, validators=[]
    )

    submit = SubmitField(label="Search For Doctors")


# class EmailMessageForm(FlaskForm):
#     name = StringField(label='Name:', validators=[DataRequired()])
#     email = StringField(label='Email:', validators=[Email(), DataRequired()])
#     subject = StringField(label='Subject:', validators=[DataRequired()])
#     message = StringField(label='Message:', validators=[DataRequired()])
#     submit = SubmitField(label='Send Message')


class TextMessageForm(FlaskForm):
    name = StringField(label="Your Name:", validators=[DataRequired(), Length(min=3)])
    phone = StringField(
        label="Your Phone Number:",
        validators=[
            Length(min=9, max=15),
            DataRequired(),
            Regexp(
                r"^(1\s?)?(\d{3}|\(\d{3}\))[\s\-]?\d{3}[\s\-]?\d{4}$",
                message="That phone number is invalid!",
            ),
        ],
    )
    message = StringField(label="Message:", validators=[Length(min=20), DataRequired()])
    submit = SubmitField(label="Send Message")
