from django.forms import ModelForm
from models import FlipBook

class FlipBookForm(ModelForm):
	class Meta:
		model = FlipBook
		exclude = ('slug')