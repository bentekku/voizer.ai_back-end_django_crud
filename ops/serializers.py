from rest_framework import serializers
from .models import Agent, Campaign, CampaignResults


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = "__all__"


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = "__all__"


class CampaignResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignResults
        fields = "__all__"
