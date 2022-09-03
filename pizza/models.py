from django.db import models

# Create your models here.
SIZE = [  # choices = COUNTRIES
    ('Sm', 'Small'),
    ('Md', 'Medium'),
    ('Lg', 'Large'),
]

class Size(models.Model):

    title = models.CharField(max_length=100)
    size = models.CharField(max_length=3, choices=SIZE, default='Md')

    def __str__(self):
        return self.title # This is for good visual experimentation!
        
class Pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100) 
    size = models.ForeignKey(Size, on_delete=models.CASCADE) # This is for correlation to the Size class
    
    def __str__(self):
        return self.size, self.topping1, self.topping2
