from django.db import models


class DjangoClasses(models.Model):
    title = models.CharField(max_length=50)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=50)
    duration = models.FloatField(max_length=4)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.title)

