from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import CampaignResults
from ..serializers import CampaignResultsSerializer


class CampaignResultsList(APIView):
    def get(self, request):
        results = CampaignResults.objects.all()
        serializer = CampaignResultsSerializer(results, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CampaignResultsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CampaignResultsDetail(APIView):
    def get(self, request, pk):
        try:
            result = CampaignResults.objects.get(pk=pk)
        except CampaignResults.DoesNotExist:
            return Response(
                {"error": "Campaign Result not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = CampaignResultsSerializer(result)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            result = CampaignResults.objects.get(pk=pk)
        except CampaignResults.DoesNotExist:
            return Response(
                {"error": "Campaign Result not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = CampaignResultsSerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            result = CampaignResults.objects.get(pk=pk)
        except CampaignResults.DoesNotExist:
            return Response(
                {"error": "Campaign Result not found"}, status=status.HTTP_404_NOT_FOUND
            )
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)