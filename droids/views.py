from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Peca
from .serializers import PecaSerializer


class PecaList(APIView):
    def get(self, request, format=None):
        pecas = Peca.objects.all()
        serializer = PecaSerializer(pecas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PecaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PecaDetail(APIView):
    def get_object(self, pk):
        try:
            return Peca.objects.get(pk=pk)
        except Peca.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        peca = self.get_object(pk)
        serializer = PecaSerializer(peca)
        return Response(serializer.data)
