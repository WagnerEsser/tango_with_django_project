# coding: utf-8
from django import forms
from rango.models import PageModel


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Título: ", required=True)
    url = forms.CharField(max_length=200, help_text="URL: ", required=True,
                          widget=forms.TextInput(attrs={'placeholder': 'http:// ...'}))
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = PageModel
        exclude = ('category',)

    # def clean_url(self):
    #     url = self.cleaned_data.get('url')
    #     if not url.startswith('http://') or not url.startswith('https://'):
    #         print("deu tiuti")
    #         raise forms.ValidationError("Informe uma URL válida.")
    #     else:
    #         return url