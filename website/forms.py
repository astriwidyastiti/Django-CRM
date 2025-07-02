from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
from django.core.validators import RegexValidator

class SignUpForm(UserCreationForm):
    email =forms.EmailField(
        label="Email",
         required=True,
         widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':
        'Email Adress *', 'required': 'required'}),)
    first_name = forms.CharField(label="First Name",max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':
        'First Name *', 'required': 'required'}))
    last_name = forms.CharField(label="Last Name",max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':
        'Last Name *', 'required': 'required'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].required = True
        self.fields['username'].widget.attrs.update({
                     'class': 'form-control',
                    'placeholder': 'Username *',
                    'required': 'required',
        })
        self.fields['username'].label='Username'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewe. Letters, digits and @/.+/-/_only.</small></span>'
        
        
        self.fields['password1'].required = True
        self.fields['password1'].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': 'Password *',
                    'required': 'required',
        })
        self.fields['password1'].label='Password'
        self.fields['password1'].help_text = '<ul class="form-text text-muted"><small><li>Your password can\'t be too similar to your other personal information.</li><li?Your password must contain at least  characters.</li><li>Your password can\'t be a commonlu used password.</li><li>Your password can\'t be entirely numeric</li></ul></span>'

        
        
        self.fields['password2'].required = True
        self.fields['password2'].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': 'Confirm Password',
                    'required': 'required',
        })
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password *'
        self.fields['password2'].label='Confirm Password'
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification. </small></span>'
        

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name*',
            'class': 'form-control',
            'required': 'required'
        }),
        label='First Name'
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name*',
            'class': 'form-control',
            'required': 'required'
        }),
        label='Last Name'
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email*',
            'class': 'form-control',
            'required': 'required'
        }),
        label='Email'
    )
    phone = forms.CharField(
        required=True,
        validators=[RegexValidator(regex=r'^\d{10,13}$', message="Enter a valid phone number (10–13 digits).")],
        widget=forms.TextInput(attrs={
            'placeholder': 'Phone*',
            'class': 'form-control',
            'pattern': r'\d{10,13}',
            'inputmode': 'numeric',
            'required': 'required'
        }),
        label='Phone'
    )
    address = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Address*',
            'class': 'form-control',
            'required': 'required'
        }),
        label='Address'
    )
    country = forms.ChoiceField(
        choices=[('Indonesia', 'Indonesia')],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Country'
    )
    state = forms.CharField(
          
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'state'  
        }),
        label='State'
    )
    city = forms.CharField(
         
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'city'  
        }),
        label='City'
    )
    zipcode = forms.CharField(
        required=True,
        validators=[RegexValidator(regex=r'^\d{5}$', message="Zipcode must be 5 digits.")],
        widget=forms.TextInput(attrs={
            'placeholder': 'Zipcode*',
            'class': 'form-control',
            'maxlength': '5',
            'pattern': r'\d{5}',
            'inputmode': 'numeric',
            'required': 'required'
        }),
        label='Zipcode'
    )
    class Meta:
        model = Record
        exclude = ('user',)