from django.shortcuts import render


# Create your views here.
def Agent(request):
    # name = models.CharField(max_length=100)
    return render(request, "base.html", context={"page_data": "Agent Page"})


def Campaign(request):
    # name = models.CharField(max_length=100)
    return render(request, "base.html", context={"page_data": "Campaign Page"})


def CampaignResults(request):
    # name = models.CharField(max_length=100)
    return render(request, "base.html", context={"page_data": "Campaign Results Page"})
