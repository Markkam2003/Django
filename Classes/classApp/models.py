from django.db import models


class DjangoClasses(models.Model):
    title = models.CharField(max_length=50)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=50)
    duration = models.FloatField(max_length=4)

    object = models.Manager()

    def __str__(self):
        return "{}".format(self.title)


math = DjangoClasses.object.create(title="Math 101", course_number=1, instructor_name="Dan", duration=35)

history = DjangoClasses.object.create(title="History 101", course_number=2, instructor_name="Been", duration=35)

english = DjangoClasses.object.create(title="English 101", course_number=3, instructor_name="Wilson", duration=35)

