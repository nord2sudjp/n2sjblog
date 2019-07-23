from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField()
    #create_date = models.DateTimeField(default=timezone.datetime.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def summary(self):
        return self.text[:100]

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField()
    # create_date = models.DateTimeField(default=timezone.datetime.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment =True
        self.save()

    def __str__(self):
        return self.text

