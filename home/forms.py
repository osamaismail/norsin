from django import forms
from .models import ContactForm





class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name','email','message']
        # widgets = {
        # 'name':TextInput(attrs={'class': 'form-group form-control', 'placeholder':'Full Name'}),
        # 'message':Textarea(attrs={'class': 'form-group form-control', 'placeholder':'Message'})
        # }

        def __init__(self, *args, **kwargs):
            super(ContactFormForm, self).__init__(*args, **kwargs)

            self.fields['name'].widget.attrs.update({'class': 'form-group form-control', 'placeholder':'Full Name'})
            # self.fields['name'].widget.attrs.update({'placeholder':'Full Name'})
            # self.fields['name'].lable = 'Name'
            self.fields['name'].widget.attrs['class'] = 'form-group form-control'
            self.fields['email'].widget.attrs['placeholder']= 'Full Name'

            # self.fields['email'].lable = 'Email address'
            self.fields['email'].widget.attrs['placeholder']= 'Email Address'
            self.fields['email'].widget.attrs['class'] = 'form-group form-control'
            self.fields['email'].help_text = "We'll never share your email with anyone else."

            # self.fields['message'].lable = 'Message'
            self.fields['message'].widget.attrs['placeholder']= 'Message'
            self.fields['message'].widget.attrs['class'] = 'form-group form-control'
