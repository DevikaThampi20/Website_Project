from django import forms
class RegistrationForm(forms.Form):
    username=forms.CharField(max_length=50)
    firstname=forms.CharField(max_length=50)
    lastname=forms.CharField(max_length=60)
    password = forms.CharField(max_length=50)
    confirm_password = forms.CharField(max_length=60)
    gender=forms.CharField(max_length=4)
    date=forms.IntegerField
    city=forms.CharField(max_length=50)
    state=forms.CharField(max_length=50)
    country=forms.CharField(max_length=50)
    pin=forms.IntegerField
    upload_image=forms.ImageField()