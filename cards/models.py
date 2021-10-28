from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.username


class Flashcards(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.CharField(max_length=100)
    start_date = models.CharField(max_length=60)
    end_date = models.CharField(max_length=50,blank=True)
    time = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Flashcards'

    def __str__(self):
        return self.title
