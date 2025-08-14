from django.db import models

class ScheduledMessage(models.Model):
    message = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    send_time = models.TimeField()  # 24-hour format
    channels = models.JSONField()  # Stores a list like ["USD", "EUR"]
    sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.message[:50]}... at {self.send_time}"
