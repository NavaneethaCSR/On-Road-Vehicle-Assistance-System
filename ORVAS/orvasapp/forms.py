from django import forms
from django.forms import ModelForm
from.models import Request,Call,Reviews






class RequestForm(ModelForm):
        class Meta:
            model = Request
            fields = ('Name','Vehicle_Type','Vehicle_No','Problem')
            labels = {

                ' Vehicle name': 'Enter the Name',

                ' Vehicle Type': ' Enter the Vehicle Type',
                ' Vehicle No': 'Enter the Vehicle No',
                'Problem': 'Mention the problem',
            }
            widgets = {

                'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Enter your Name'}),
                'Vehicle_Type':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Vehicle Type'}),
                'Vehicle_No': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Vehicle No'}),
                'Problem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mention the problem'}),
            }



class CallForm(ModelForm):
        class Meta:
            model = Call
            fields = ('Mobile_no','SMS')
            labels = {

                ' Mobile no': 'Enter the Mobile no',

                ' SMS': ' Enter the message',

            }
            widgets = {

                'Mobile_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Enter the Mobile no'}),

                'SMS': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the message'}),
            }


class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ('Enter_Name', 'Write_review')
        labels = {

            ' Name': 'Enter the Name',

            ' Review': ' Enter the review',

        }
        widgets = {

            'Enter_Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Enter the Name'}),

            'Write_review': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the review'}),
        }

