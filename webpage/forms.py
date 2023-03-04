from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

class QueryForm(FlaskForm):
    
    def validate_zipcode(self, zipcode):
        if len(zipcode.data) != 5:
            raise ValidationError('Zipcode must be 5 digits long.')
        if not zipcode.data.isdigit():
            raise ValidationError('Zipcode must be numeric.')
    
    zipcode = StringField(label='Zipcode:', validators=[Length(min=5, max=5), DataRequired()])
    specialization = SelectMultipleField(label='Specialization:', choices=[('gen_prac', 'General Practitioner'), ('obgyn', 'OBGYN'), ('optomologist', 'Optomologist')], validators=[])
    years_experience = StringField(label='Minimum Years of Experience:', validators=[Length(max=2)])
    insurance = SelectMultipleField(label='Insurance:', choices=[('aetna', 'Aetna'), ('blue_cross', 'Blue Cross'), ('cigna', 'Cigna'), ('humana', 'Humana'), ('medicare', 'Medicare'), ('medicaid', 'Medicaid'), ('united_healthcare', 'United Healthcare'), ('alina', 'Alina Health')], validators=[])
    lang = SelectField(label="Preferred Language: ", choices=[('english', 'English'), ('spanish', 'Spanish')], validators=[])
    gender = SelectMultipleField(label="Preffered Gender: ", choices=[('nopref', 'No Preference'), ('male', 'Male'), ('female', 'Female'), ('other', 'Other')], validators=[])
    
    submit = SubmitField(label='Search For Doctors')

