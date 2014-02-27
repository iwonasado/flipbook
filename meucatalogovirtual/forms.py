from django import forms
from django.utils.translation import ugettext_lazy as _
  
class ContactForm(forms.Form):
    content = forms.CharField(label=_("Mensagem"), widget=forms.Textarea(attrs={'title':_("Mensagem")}))
    name = forms.CharField(label=_("Nome"), required=False,widget=forms.TextInput(attrs={'title':_("Nome")}))
    email = forms.EmailField(label=_("Email"),widget=forms.TextInput(attrs={'title':_("Email")}))


    template = "contato/contact.html"
  