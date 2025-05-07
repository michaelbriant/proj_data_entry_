from django import forms
from .models import Pengguna, Content

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

class PenggunaForm(forms.ModelForm):
    state = forms.ChoiceField(choices=STATES)

    class Meta:
        model = Pengguna
        exclude = ['tanggal_join',]

class ContentForm(forms.ModelForm):
    article = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Tulis artikel di sini...', 'rows': 4}),
        label="Artikel",
        required=True
    )

    class Meta:
        model = Content
        fields = ['author', 'set_view', 'article']
