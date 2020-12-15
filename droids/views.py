from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, authentication, permissions

from .models import Peca, Anunciante, Demanda
from .serializers import PecaSerializer, AnuncianteSerializer, DemandaSerializer


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


class PecaViewSet(viewsets.ModelViewSet):
    """ Lista todas as Pecas. """
    queryset = Peca.objects.all()
    serializer_class = PecaSerializer

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class AnuncianteViewSet(viewsets.ModelViewSet):
    """ Lista todos os Anunciantes. """
    queryset = Anunciante.objects.all()
    serializer_class = AnuncianteSerializer

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class DemandaViewSet(viewsets.ModelViewSet):
    """ Lista todos as Demandas do respectivo Usuário. """
    queryset = Demanda.objects.all()
    serializer_class = DemandaSerializer

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """Retrieve the Demand for the authenticated user"""
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        """ Create a new Demand """
        serializer.save(user=self.request.user)
