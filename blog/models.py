from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    
    
    def summary(self):
        return self.body[:100]
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    
    def __str__(self):
        return self.title
    
    
    

#STEPS WHILE CREATING A MODEL:
# 1 CREATE A BLOG MODEL IN THIS CASE
# 2 ADD THE BLOG APP TO THE SETTINGS
# 3 CREATE A MIGRATION
# 4 MIGRATE
# 5 ADD TO THE ADMIN