from django import forms
from . import models

class Create_article(forms.ModelForm):
    class Meta:
       model = models.Article
       fields = [
           "title", "slug", "body", "photo"
       ]