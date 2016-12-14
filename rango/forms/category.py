#coding: utf-8
from django import forms
from rango.models import CategoryModel


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Nome: ")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = CategoryModel
        fields = ('name',)
