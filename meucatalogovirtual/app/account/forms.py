# -*- coding: utf-8 -*-
from models import UserProfile
from django.forms import ModelForm , EmailField
from django import forms
from django.contrib.auth.models import User


class FormRegistro(ModelForm):
    username = forms.CharField(min_length = 3, max_length = 30)
    class Meta:
        model=User
        order_by = ['username', 'email','password']
        fields = ('username','email','password')
    confirme_a_senha = forms.CharField( max_length=30, widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        self.base_fields['password'].help_text = ''
        self.base_fields['password'].widget = forms.PasswordInput()
        super(FormRegistro, self).__init__(*args, **kwargs)

    def clean_username(self):
        if User.objects.filter(
            username=self.cleaned_data['username'],
            ).count():
            raise forms.ValidationError('Já existe um usuário com esse username')

        return self.cleaned_data['username']


    def clean_confirme_a_senha(self):
        if self.cleaned_data['confirme_a_senha'] != self.data['password']:
            raise forms.ValidationError(u'Confirmação da senha não confere!')

        return self.cleaned_data['confirme_a_senha']

    def save(self, commit=True):
        usuario = super(FormRegistro, self).save(commit=False)

        usuario.set_password(self.cleaned_data['password'])

        if commit:
            usuario.save()

        return usuario