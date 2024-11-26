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
    def get_object(self, voice_id):
        try:
            return Agent.objects.get(voice_id=voice_id)
        except Agent.DoesNotExist:
            return Response(
                {"error": "Agent not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def get(self, request, pk):  # Here `pk` is the `voice_id`
        agent = self.get_object(pk)  # Use `voice_id` to get the agent
        serializer = AgentSerializer(agent)
        return Response(serializer.data)

    def put(self, request, pk):  # Here `pk` is the `voice_id`
        agent = self.get_object(pk)  # Query using `voice_id`
        serializer = AgentSerializer(agent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        agent = self.get_object(pk)
        serializer = AgentSerializer(agent, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):  # `pk` is still `voice_id`
        agent = self.get_object(pk)  # Delete using `voice_id`
        agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
