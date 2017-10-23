from django.db import models

# Create your models here.
 
class OriginRecommandList(models.Model):
    user_id = models.IntegerField()
    books = models.TextField()

class BookIds(models.Model):
    book_id = models.IntegerField(default=0)
    book_name = models.TextField()
