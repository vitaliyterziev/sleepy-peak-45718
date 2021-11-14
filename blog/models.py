from django.db import models
from django.core import validators

class Entry(models.Model):
    entry_title = models.CharField(max_length=200)
    entry_content = models.TextField()
    pub_date = models.DateTimeField('date published')
    entry_img = models.ImageField(blank=True, validators=[validators.validate_image_file_extension])

    def __str__(self):
        return self.entry_title


class Comment(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.comment_text


class Membership(models.Model):
    email_address = models.CharField(max_length=200, validators=[validators.validate_email])

    def __str__(self):
        return self.email_address
