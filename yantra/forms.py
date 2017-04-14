from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()
