from django import forms 
from .models import Post , CustomProfile,User
from django.contrib.auth.forms import UserCreationForm

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','image']

class CustomProfileform(forms.ModelForm):
    class Meta:
        model = CustomProfile
        fields = ['phone_number','address']

class CustomUsercreationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model = User
        fields= ['email','password1','password2','first_name','last_name']

    def clean_email(self):
        email=self.cleaned_data['email'].lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'this email is already registered'
            )
        return email

class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
