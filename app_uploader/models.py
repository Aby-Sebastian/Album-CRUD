from django.db import models
from django.utils.text import slugify
# Create your models here.

class Album(models.Model):
	image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
	slug = models.SlugField(default='', editable=False, max_length=50)
	alt = models.CharField(max_length=50)
	
	class Meta:
		ordering=["-id"]

	def __str__(self):
		return self.alt
		
	def save(self, *args,**kwargs):
		self.slug = slugify(self.alt, allow_unicode=True)
		super().save(*args, **kwargs)
