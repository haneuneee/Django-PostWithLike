# -*- coding: utf-8 -*-
from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)


class CommentForm(forms.Form):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'ng-model':'formdata.content'}), label='댓글달기')


FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)


class TestForm(forms.Form):
    name = forms.CharField(label_suffix=' ')
    name2 = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(input_formats=['%m/%d/%Y'])
    file = forms.FileField()
    birth_year = forms.DateField(widget=forms.SelectDateWidget())
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )
