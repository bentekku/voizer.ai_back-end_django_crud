from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Campaign
from ..serializers import CampaignSerializer


class CampaignList(APIView):
    def get(self, request):
        campaigns = Campaign.objects.all()
        serializer = CampaignSerializer(campaigns, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CampaignDetail(APIView):
    def get(self, request, pk):
        try:
            campaign = Campaign.objects.get(pk=pk)
        except Campaign.DoesNotExist:
            return Response(
                {"error": "Campaign not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = CampaignSerializer(campaign)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            campaign = Campaign.objects.get(pk=pk)
        except Campaign.DoesNotExist:
            return Response(
                {"error": "Campaign not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = CampaignSerializer(campaign, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            campaign = Campaign.objects.get(pk=pk)
        except Campaign.DoesNotExist:
            return Response(
                {"error": "Campaign not found"}, status=status.HTTP_404_NOT_FOUND
            )
        campaign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
