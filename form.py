from flask_wtf import FlaskForm
from wtforms.validators import Length, NumberRange, URL, Optional, InputRequired
from wtforms import StringField, SelectField, BooleanField, TextAreaField, IntegerField

class addPet(FlaskForm):
    """Add pet form"""
    name = StringField(
        "Pet Name", validators = [InputRequired()]
    )

    species = SelectField(
        "Species", choices = [("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")]
    )

    photo_url = StringField(
        "Photo URL", validators = [Optional(), URL()]
    )

    age = IntegerField(
        "Age", validators = [Optional(), NumberRange(min = 0, max = 30)]
    )

    notes = TextAreaField(
        "Comments", validators = [Optional(), Length(min = 10)]
    )



class editPet(FlaskForm):
    """Edit pet Form"""
    photo_url = StringField(
        validators = [Optional(), URL()]
    )

    notes = TextAreaField(
        "Comments", validators = [Optional(), Length(min = 10)]
    )

    available = BooleanField("Available")
