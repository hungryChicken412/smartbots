from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from .utils import get_random_code
from django.template.defaultfilters import slugify
import binascii
import os
# Create your models here.
from uuid import uuid4





class faq(models.Model):
	question = models.CharField(max_length=200, default="")
	ans = models.TextField(max_length=200, default="")

	def __str__(self):
		return f"{self.question}"

class chatlog(models.Model):
	userIP = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add = True)
	ended = models.DateTimeField(auto_now_add = False)
	messages = models.IntegerField(default=0)
	cost = models.FloatField(default=0)

class ChatbotProfile(models.Model):
	def generateToken():
		return str(uuid4())

	faqs = models.ManyToManyField(faq)
	context = models.TextField(max_length=10000)
	greeting = models.TextField(max_length=1000, default="Hi there! How Can I Help You!")
	owner = models.ForeignKey(User, related_name="Connected_User", on_delete=models.DO_NOTHING)
	logs = models.ManyToManyField(chatlog)

	token = models.CharField(max_length=100, default=generateToken)
			
	def __str__(self):
		return f"{self.owner.username}'s Chatbot--{self.token}"


class Profile(models.Model):

	## BASE ##

	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	
	email = models.EmailField(max_length=200)
	avatar = models.ImageField(default='chicken.jpg', upload_to='avatars/')
	info = models.TextField(max_length=200, default='N\A')
	username = models.CharField(max_length=200, default='#user')

	updated = models.DateTimeField(auto_now = True)
	created = models.DateTimeField(auto_now_add = True)

	## END_BASE ##

	## ACTIVITY / STATS ##

	credits = models.FloatField(default=100)
	bots = models.ManyToManyField(ChatbotProfile)
	

	## END_ACTIVITY / END_STATS ##

	@property
	def user__username(self):
		return self.user.username
		
	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return f"{self.user.username}--{self.created}"



	

	
	
	
	





