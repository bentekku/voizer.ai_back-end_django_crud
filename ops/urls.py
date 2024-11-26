from django.urls import path
from .views import Agent, Campaign, CampaignResults

urlpatterns = [
    path("agents/", Agent),
    path("campaigns/", Campaign),
    path("campaign-results/", CampaignResults),
]
