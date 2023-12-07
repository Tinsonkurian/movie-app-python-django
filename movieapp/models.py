from django.db import models

# Create your models here.

class Movies(models.Model):
    movie_name = models.CharField( max_length=50)
    movie_des = models.TextField()
    movie_year = models.CharField( max_length=4)
    movie_image = models.ImageField( upload_to='movies', height_field=None, width_field=None, max_length=None)

    def __str__(self) -> str:
        return self.movie_name