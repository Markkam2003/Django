from django.db import models


class DjangoClasses(models.Model):
    title = models.CharField(max_length=50)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=50)
    duration = models.FloatField(max_length=4)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.title)


math = DjangoClasses.objects.create(title="Math 101", courseNumber=1, instructorName="Dan", duration=35)

history = DjangoClasses.objects.create(title="History 101", courseNumber=2, instructorName="Been", duration=35)

english = DjangoClasses.objects.create(title="English 101", courseNumber=3, instructorName="Wilson", duration=35)

object.save(math, history, english)