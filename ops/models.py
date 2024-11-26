from django.db import models


# INFO: models are just like schemas of mongoose from express.js

CAMPAIGN_TYPE_CHOICE = [("Inbound", "Inbound"), ("Outbound", "Outbound")]
STATUS_CHOICE = [
    ("Running", "Running"),
    ("Paused", "Paused"),
    ("Completed", "Completed"),
]


class Agent(models.Model):
    agent_name = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    voice_id = models.CharField(max_length=50, unique=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.agent_name


class Campaign(models.Model):
    campaign_name = models.CharField(max_length=100)
    campaign_type = models.CharField(
        max_length=35, choices=CAMPAIGN_TYPE_CHOICE, default="Inbound"
    )
    phone_number = models.CharField(max_length=12)
    status = models.CharField(max_length=35, choices=STATUS_CHOICE, default="Running")
    agent_name = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return self.campaign_name


class CampaignResults(models.Model):
    campaign_name = models.CharField(max_length=100)
    campaign_type = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    cost = models.FloatField()
    outcome = models.CharField(max_length=25)
    call_duration = models.FloatField()
    recording = models.URLField()
    summary = models.TextField()
    transcription = models.TextField()

    def __str__(self):
        return self.campaign_name
