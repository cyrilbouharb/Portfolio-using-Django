from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    
    
    
    
    

#STEPS WHILE CREATING A MODEL:
# 1 CREATE A BLOG MODEL IN THIS CASE
# 2 ADD THE BLOG APP TO THE SETTINGS
# 3 CREATE A MIGRATION
# 4 MIGRATE
# 5 ADD TO THE ADMIN