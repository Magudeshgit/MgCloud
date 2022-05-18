from django.forms import ModelForm, widgets
from .models import FileUpload

class FileUpload(ModelForm):
	class Meta:
		model = FileUpload
		fields = ['file']