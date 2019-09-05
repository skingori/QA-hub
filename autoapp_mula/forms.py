from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, help_text='Optional.',
                               widget=forms.TextInput(attrs={'class': "form-control"}))
    # first_name = forms.CharField(required=False, help_text='Optional.',
    #                              widget=forms.TextInput(attrs={'class': "form-control"}))
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.',
    #                             widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
                             widget=forms.EmailInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(required=False, help_text='Optional.', label="Password",
                                widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(required=False, help_text='Optional.', label="Confirm Password",
                                widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class LoginForm(forms.Form):
    username = forms.CharField(required=True, help_text='Optional.',
                               widget=forms.TextInput(attrs={'class': "form-control"}))

    password = forms.CharField(required=False, help_text='Optional.', label="Password",
                               widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'password')


class TestForm(forms.Form):
    qa_test_case = forms.CharField(max_length=150)
    section_id = forms.CharField(max_length=100)
    pre_conditions = forms.Textarea()
    steps = forms.Textarea()
    expected_result = forms.Textarea()
    big_data = forms.Textarea()


class SimulateForm(forms.Form):
    msisdn = forms.CharField(max_length=20)
    amount = forms.CharField(max_length=20)
    country = forms.CharField(max_length=20)
    currency = forms.CharField(max_length=20)
    timer = forms.CharField(max_length=20)
    experience = forms.CharField(max_length=100)
    payer_client = forms.CharField(max_length=20)


class SimulateJsonForm(forms.Form):
    json_data = forms.Textarea()


class SimulatePayment(forms.Form):
    amount = forms.CharField(max_length=6)
    account_number = forms.CharField(max_length=200)
    msisdn = forms.CharField(max_length=20)
    payerClient = forms.CharField(max_length=200)
    currency = forms.CharField(max_length=4)

