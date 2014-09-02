from django.forms import ModelForm
from film.models import Film, Film_comment

class FilmForm (ModelForm):
    class Meta():
        model = Film
        fields = {'film_name', 'film_created_users', 'film_jenres',  'film_year', 'film_award', 'film_sided_id', 'film_text'}

class Film_comment_Form(ModelForm):
    class Meta():

        model = Film_comment
