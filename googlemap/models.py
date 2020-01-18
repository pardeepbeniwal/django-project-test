from django.contrib.gis.db import models


class GoogleMapModel(models.Model):
    url = models.URLField(max_length=255)
    location = models.PointField()

    def __str__(self):
        return self.url

    def save_data(self, data):
        success = True
        try:
            self.location = data.get('location')
            self.url = data.get('url')
            self.save()
        except:
            success = False
        return success
