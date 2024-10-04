from django import forms 
from cars.models import Car

    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car 
        fields = "__all__"
#para fazer validações usamos a seguinte sintaxd a baixo
#O django so consegue entender que uma função é uma função de validação se tiver o clean_ primeiro
    def clean_value(self):
        value = self.cleaned_data.get("value")#pega o dado ja limpo
        if value < 20000:
            self.add_error("value","Valor minimo para cadastrar um carro tem que ser maior ou igual a 20 mil")
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get("factory_year")
        if factory_year < 1975:
            self.add_error('factory_year',"Não é possivel adicionar carros lançados antes de 1975, Digite um valor valido")
