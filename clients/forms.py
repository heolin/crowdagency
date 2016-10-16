from django.forms import ModelForm
from clients.models import Survey

class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = ['satisfaction_level', 'satisfaction_comment', 'experience']

    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control form-field'

        self.fields['satisfaction_level'].label = 'Oceń na skali od 1 do 5 jak bawiłeś się podczas rozrywki.'
        self.fields['satisfaction_comment'].label = 'Krótko uzasadnij dlaczego zdecydowałeś/aś się na wybór tej oceny?'
        self.fields['experience'].label = 'Jak często grasz w gry?'
