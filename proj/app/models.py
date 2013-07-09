from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

 
class Profile(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(unique=True, max_length=255)
	description = models.CharField(max_length=255)
	interests = models.TextField()
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
 
	class Meta:
		ordering = ['-created']
 
	def __unicode__(self):
		return u'%s' % self.title
 
	def get_absolute_url(self):
 		return reverse('app.views.profile', args=[self.slug])

class Event(models.Model):
	title = models.CharField(max_length=255)
	interests = models.TextField()
	description = models.CharField(max_length=255)
	when = models.DateTimeField(auto_now_add=True)
 
	class Meta:
		ordering = ['-when']
 
	def __unicode__(self):
		return u'%s' % self.title



