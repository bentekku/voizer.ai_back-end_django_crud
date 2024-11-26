from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # Status -> http response codes
from ..models import Agent  # Models -> data-base structure or Schema (express.js)
from ..serializers import AgentSerializer  # Serializer -> models => json


class AgentList(APIView):
    def get(self, request):
        agents = Agent.objects.all()
        serializer = AgentSerializer(agents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AgentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class AgentDetail(APIView):
    # instead of pk=pk, which takes in (id) and compares it with request's id; switched to voice_id, which is always unique to user
    def get(self, request, pk):
        try:
            agent = Agent.objects.get(voice_id=pk)
        except Agent.DoesNotExist:
            return Response(
                {"error": "Agent not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = AgentSerializer(agent)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            agent = Agent.objects.get(voice_id=pk)
        except Agent.DoesNotExist:
            return Response(
                {"error": "Agent not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = AgentSerializer(agent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            agent = Agent.object.get(voice_id=pk)
        except Agent.DoesNotExist:
            return Response(
                {"error": "Agent not found"}, status=status.HTTP_404_NOT_FOUND
            )
        agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
