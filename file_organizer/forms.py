from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField(required=True, allow_empty_file=False)