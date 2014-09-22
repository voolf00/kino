from django.forms import ModelForm
from film.models import Film, Film_comment, AboutCreatedUser

class FilmForm (ModelForm):
    class Meta():
        model = Film
        fields = {'film_name',  'film_jenres',  'film_sided_id', 'film_text', 'film_english_name'}

class Film_comment_Form(ModelForm):
    class Meta():

        model = Film_comment

class Film_About_created_Users_Form(ModelForm):
    class Meta():
        model = AboutCreatedUser
        fields = {'film_compozitor', 'film_actors', 'film_rejisser','film_operatior','film_scenarii', 'film_produsser', 'film_montaj'}
