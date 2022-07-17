from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create 1-1 relationship with existing user model
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg',upload_to='profile_pics')

#how we want our image to be displayed
	def __str__(self):
		return f'{self.user.username} Profile'

	#method that runs after model saved
	#
	def save(self):
		#run save of parent class using super()
		super().save()
#image of current instance
		img=Image.open(self.image.path)
		#resize img
		if img.height >300 or img.width>300:
			out_size=(300,300)
			img.thumbnail(out_size)
			#overwrite save
			img.save(self.image.path)

