from django.db import models
from django.utils import timezone

class ScheduledMessage(models.Model):
    message = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    send_time = models.TimeField()  # 24-hour format
    channels = models.JSONField()  # Stores a list like ["USD", "EUR"]
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True, blank=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.message[:50]}... at {self.send_time}"

    @property
    def status(self):
        if self.sent:
            return "Completed"
        return "Pending"

    @property
    def channels_display(self):
        return ", ".join(self.channels) if self.channels else "No channels"
