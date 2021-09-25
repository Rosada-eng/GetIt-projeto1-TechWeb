from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.name}"

class Note(models.Model):
    title   = models.CharField(max_length=60)
    content = models.TextField()
    tag     = models.ForeignKey(Tag, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}. {self.title}"