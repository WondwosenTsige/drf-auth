from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SportSerializer
from .models import Sport
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class SportList(ListCreateAPIView):
    #permission_classes = (IsOwnerOrReadOnly,)
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


class SportDetail(RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsOwnerOrReadOnly,)
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

