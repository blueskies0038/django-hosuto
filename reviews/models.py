from django.db import models
from core import models as core_models

class Review(core_models.TimeStampedModel):
    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.PositiveIntegerField()
    cleanliness = models.PositiveIntegerField()
    value = models.PositiveIntegerField()
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", related_name="reviews", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):
        average = (self.accuracy + self.communication + self.cleanliness + self.value)/4
        return round(average, 2)
    rating_average.short_description = "Avg."
