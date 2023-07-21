from django.db import models
from random import choices
from string import ascii_letters
from django.conf import settings

# Create your models here.
# model for links to be shortened

class Link(models.Model):
    original_link = models.URLField( )
    shortend_link = models.URLField(blank = True, null = True)
    
    def shortner(self):
        while True:
            random_string = ''.join(choices(ascii_letters,k=6))
            new_link = settings.HOST_URL + '/' + random_string
            
            # check if the new_link exists
            # if not break out of the loop
            if not Link.objects.filter(shortend_link = new_link).exists():
                break
            
        return new_link
            
    def save(self, *args, **kwargs):
        if not self.shortend_link:
            new_link = self.shortner()
            self.shortend_link = new_link
            return super().save(*args,**kwargs)
    

    