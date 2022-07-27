from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FileUpload(models.Model):
	foreignKey = models.ForeignKey(User, related_name="Key", on_delete=models.CASCADE,  null=True)
	file = models.FileField(null=True, upload_to='UserFiles')
	def __str__(self):
		return self.file.name