from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    author = models.ForeignKey("users.ServiceUser", on_delete=models.CASCADE,)
    branch = models.ForeignKey("branches.Branch", on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'post'
