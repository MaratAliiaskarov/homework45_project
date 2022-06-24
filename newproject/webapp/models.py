from django.db import models

# Create your models here.

STATUS_CHOICES = [("new", "New"), ("in_progress", "InProcess"), ("done", "Completed")]

class Article(models.Model):
    project = models.CharField(max_length=50, null=False, blank=False, verbose_name="Zagalovok")
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name="Author", default="Unknown")
    content = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created_date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date_changes")

    def __str__(self):
        return f"{self.id}. {self.project}. {self.author}. {self.status}"

    class Meta:
        db_table = "articles"
        verbose_name = "Statia"
        verbose_name_plural = "Statii"