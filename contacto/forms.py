from django import forms

class FormularioContacto(forms.Form):

    nombre = forms.CharField(label="Escribe tu nombre completo", required=True, widget=forms.TextInput(attrs={'placeholder':'Nombre...'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'em@il...'}))
    contenido = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Escribe tu mensaje...'}))