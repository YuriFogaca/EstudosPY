from django.forms import ModelForm
from aplicativoCRUD.models import Carros    

# Create the form class.
class CarrosForm(ModelForm):
    class Meta:
         model = Carros
         fields = ['Modelo', 'Marca', 'Ano']