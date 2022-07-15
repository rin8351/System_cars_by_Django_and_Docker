from django.db import models
from django.urls import reverse

class parts(models.Model):
    type = models.CharField(max_length = 100)
    price = models.IntegerField()
    model_p = models.CharField(max_length = 100)
    count_p = models.IntegerField()
    params = models.CharField(max_length = 100)

    def __str__(self):
        return self.model_p

    def get_absolute_url(self):
        return reverse('parts')

class cars(models.Model):
    name = models.CharField(max_length=100)
    parts = models.ManyToManyField(parts, related_name='carss')
    margin = models.IntegerField()
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cars')

    def save(self, *args, **kwargs):
        part_list = car_part.objects.filter(car=self)
        parts_list2 = parts.objects.filter(id__in=part_list.values('part'))
        price = 0
        for part in parts_list2:
            price += part.price * part.count_p
        self.price = price * (1 + self.margin / 100)
        super().save(*args, **kwargs)


class car_part(models.Model):
    car = models.ForeignKey(cars, on_delete=models.CASCADE)
    part = models.ForeignKey(parts, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{} {}".format(self.car.__str__(), self.part.__str__())