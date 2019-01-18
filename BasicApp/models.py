from django.db import models


class Topic(models.Model):
    top_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ActiveRecord(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)
