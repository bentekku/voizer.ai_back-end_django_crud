from django.urls import path
from .views.agent_views import AgentList, AgentDetail
from .views.campaign_views import CampaignList, CampaignDetail
from .views.campaign_results_views import CampaignResultsList, CampaignResultsDetail

urlpatterns = [
    # Agent URLs
    path("agents/", AgentList.as_view(), name="agent-list"),
    path("agents/<str:pk>/", AgentDetail.as_view(), name="agent-detail"),
    # Campaign URLs
    path("campaigns/", CampaignList.as_view(), name="campaign-list"),
    path("campaigns/<str:pk>/", CampaignDetail.as_view(), name="campaign-detail"),
    # CampaignResults URLs
    path(
        "campaign-results/", CampaignResultsList.as_view(), name="campaign-results-list"
    ),
    path(
        "campaign-results/<str:pk>/",
        CampaignResultsDetail.as_view(),
        name="campaign-results-detail",
    ),
]
