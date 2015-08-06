from django import forms


class HelloWorldForm(forms.Form):
    name = forms.CharField(required=True, label="Say Hello")
    awesome = forms.BooleanField(label="Are they awesome?")

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.lower().startswith('b'):
            raise forms.ValidationError("Wait a second, your name doesn't start with B!")
        return name
