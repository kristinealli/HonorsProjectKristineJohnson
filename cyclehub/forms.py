from django import forms
from .models import Item

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'category', 'photo', 'active', 'available', 'loan_terms']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'loan_terms': forms.Textarea(attrs={'class': 'form-control'}),
        }