from django.db import models


class Comment(models.Model):
    comment_text = models.CharField(max_length=2000)
    article_uuid = models.CharField(max_length=20)

    def __str__(self):             
        return self.comment_text