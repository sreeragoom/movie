from django import forms
from .models import Movies


class MovieForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['title','description','year','poster','actors','links','category','slug','user']

        def clean_slug(self):
            slug = self.cleaned_data['slug']
            if not slug:
                raise forms.ValidationError("Slug cannot be empty.")
            if Movies.objects.filter(slug=slug).exists():
                raise forms.ValidationError("This slug is already in use. Please choose a different one.")
            return slug

