from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email =forms.EmailField(
        label="",
         required=True,
         widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':
        'Email Adress *', 'required': 'required'}),)
    first_name = forms.CharField(label="",max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':
        'First Name *', 'required': 'required'}))
    last_name = forms.CharField(label="",max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':
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
        self.fields['username'].label=''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewe. Letters, digits and @/.+/-/_only.</small></span>'
        
        
        self.fields['password1'].required = True
        self.fields['password1'].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': 'Password *',
                    'required': 'required',
        })
        self.fields['password1'].label=''
        self.fields['password1'].help_text = '<ul class="form-text text-muted"><small><li>Your password can\'t be too similar to your other personal information.</li><li?Your password must contain at least  characters.</li><li>Your password can\'t be a commonlu used password.</li><li>Your password can\'t be entirely numeric</li></ul></span>'

        
        
        self.fields['password2'].required = True
        self.fields['password2'].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': 'Confirm Password',
                    'required': 'required',
        })
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password *'
        self.fields['password2'].label=''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification. </small></span>'
        

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'First Name', 'class':'form-control'}), label='')
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control'}), label='')
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Email', 'class':'form-control'}), label='')
    phone  = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Phone', 'class':'form-control'}), label='')
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Address', 'class':'form-control'}), label='')
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'City', 'class':'form-control'}), label='')
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'State', 'class':'form-control'}), label='')
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Zipcode', 'class':'form-control'}), label='')
  
    class Meta:
        model = Record
        exclude =('user',)