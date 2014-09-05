from django.forms import ModelForm
from film.models import Film, Film_comment, AboutCreatedUser

class FilmForm (ModelForm):
    class Meta():
        model = Film
        fields = {'film_name',  'film_jenres',  'film_year', 'film_award', 'film_sided_id', 'film_text'}

class Film_comment_Form(ModelForm):
    class Meta():

        model = Film_comment
