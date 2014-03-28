from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from models import Post
from models import UserProfile
from django.forms import Textarea


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True,     widget=forms.TextInput(attrs={'placeholder':'Email','class':'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'First Name','class':'form-control'}))
    last_name = forms.CharField(required=True,  widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control'}))
    username = forms.CharField(required=True,   widget=forms.widgets.TextInput(attrs={'placeholder': 'Username','class':'form-control'}))
    password1 = forms.CharField(required=True,  label='Password',  widget=forms.PasswordInput( attrs={'placeholder':'Password','class':'form-control'}))
    password2 = forms.CharField(required=True,  label='Password Again',  widget=forms.PasswordInput(attrs={'placeholder':'Password Confirmation','class':'form-control'}))

    def is_valid(self):
        form = super(RegistrationForm, self).is_valid()
        for f, error in self.errors.iteritems():
            self.fields[f].widget.attrs.update({"class":"error",'value':strip_tags(error)})

        return form

    class Meta:
        model = User
        fields=['email','first_name','last_name','username','password1','password2']



class AuthenticateForm(AuthenticationForm):

    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))

    def is_valid(self):
        form = super(AuthenticateForm, self).is_valid()
        for f, error in self.errors.iteritems():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form




class PostDonationForm(forms.ModelForm):

    class Meta:
        model = Post
        widgets={
            'post_header': Textarea(attrs={'rows':2,'cols':60}),
            'post_detail': Textarea(attrs={'rows':20,'cols':60}),
            'post_amount': Textarea(attrs={'rows':1,'cols':60}),
        }
        fields = ['post_type', 'post_donation_type', 'post_sector', 'post_amount', 'post_donation_method', 'post_header', 'post_detail']





from django_countries.data import COUNTRIES


class UserProfileUpdateForm(forms.ModelForm):


    first_name = forms.CharField(max_length=100, label="First Name")
    last_name = forms.CharField(max_length=100, label="Last Name")
    password = forms.CharField(widget=forms.PasswordInput(),help_text="this field is required to update")


    class Meta:
        model = UserProfile

        fields =['first_name','last_name','donor_donee_type', 'image', 'occupation', 'contact_no', 'street_no', 'street_address', 'city', 'country', 'description', 'website']

        widgets={
            'country':forms.Select(choices=sorted(COUNTRIES.items(),key=lambda country:country[1])),
            'password': forms.PasswordInput(),
        }












































