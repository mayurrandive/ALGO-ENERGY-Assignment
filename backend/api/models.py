from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = models.Manager()


    def __str__(self):
        return self.first_name
    
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

class Expenses(models.Model):
    date = models.DateField(auto_now_add=True)
    # food = array of numbers
    food = ArrayField(models.DecimalField(max_digits=10, decimal_places=2), default=list)
    transport = ArrayField(models.DecimalField(max_digits=10, decimal_places=2), default=list)
    entertainment = ArrayField(models.DecimalField(max_digits=10, decimal_places=2), default=list)
    others = ArrayField(models.DecimalField(max_digits=10, decimal_places=2), default=list)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # function whihc returns the total of each category
    def total_food(self):
        return sum(self.food)
    
    def total_transport(self):
        return sum(self.transport)
    
    def total_entertainment(self):
        return sum(self.entertainment)
    
    def total_others(self):
        return sum(self.others)

    def __str__(self):
        return f"{self.user.email} expenses"
