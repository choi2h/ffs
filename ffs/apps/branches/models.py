from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    description = models.TextField(blank=True)
    owner = models.ForeignKey('users.ServiceUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'branches'
        ordering = ('name',)
        db_table = 'branch'