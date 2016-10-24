from django import forms
from .models import Contact, Member


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Name',
                    'required': True,
                    'class': 'form-control',
                    'id': 'name'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                    'required': True,
                    'class': 'form-control',
                    'id': 'name'
                }
            ),
            'message': forms.Textarea(attrs={
                'placeholder': 'What would you like to tell us?',
                'required': True,
                'class': 'form-control',
                'id': 'name'
            }
            )
        }
        labels = {
            'name': "Name",
            'email': 'Email',
            'message': 'Message',
        }
        error_messages = {
            'name': {
                'max_length': "The name is too long",
            },
            'email': {
                'max_length': "The email is too long",
            },
            'message': {
                'max_length': "The message is too long",
            }
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('name', 'email', 'knowledge', 'image', 'level', 'sex', 'message', 'bio', 'interest', 'display_image')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Name',
                    'required': True,
                    'class': 'form-control',
                    'id': 'name'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Why would you like to join us?',
                    'required': True,
                    'class': 'form-control',
                    'id': 'name'
                }
            ),

            'level': forms.Select(
                attrs={
                    'placeholder': 'Level',
                    'required': True,
                    'class': 'form-control',
                    'id': 'name'
                }
            ),
            'sex': forms.Select(
                attrs={
                    'placeholder': 'Sex',
                    'required': True,
                    'class': 'form-control',
                    'id': 'name'
                }
            ),
            'knowledge': forms.Select(
                attrs={
                    'placeholder': 'Level',
                    'required': True,
                    'class': 'form-control',
                    'id': 'name'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                    'required': True,
                    'class': 'form-control',
                    'id': 'name'
                }
            ),
            'bio': forms.Textarea(attrs={
                'placeholder': 'Tell us a little about yourself',
                'required': True,
                'class': 'form-control',
                'id': 'name'
            }
            ),
            'interest': forms.Select(
                attrs={
                    'placeholder': 'What interests you in Python?',
                    'required': True,
                    'class': 'form-control',
                    'id': 'name'
                }
            ),
        }
        labels = {
            'name': "Name",
            'email': 'Email',
            'message': 'Message',
            'knowledge': 'How well do you know Python?',
            'sex': 'Sex',
            'level': 'Level',
            'interest': 'Interest',
            'bio': 'Bio',

        }
        error_messages = {
            'name': {
                'max_length': "The name is too long",
            },
            'email': {
                'max_length': "The email is too long",
            },
            'message': {
                'max_length': "The message is too long",
            }
        }

