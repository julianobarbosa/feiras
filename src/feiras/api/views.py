from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
)
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from core.models import Feira
from .pagination import FeiraPageNumberPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    FeiraCreateSerializer,
    FeiraDetailSerializer,
    FeiraListSerializer
)


class FeiraCreateAPIView(CreateAPIView):
    queryset = Feira.objects.all()
    serializer_class = FeiraCreateSerializer
    permission_classes = [
        IsAuthenticated
        ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FeiraDetailAPIView(RetrieveAPIView):
    queryset = Feira.objects.all()
    serializer_class = FeiraDetailSerializer
    lookup_field = 'id'


class FeiraDeleteAPIView(DestroyAPIView):
    queryset = Feira.objects.all()
    serializer_class = FeiraDetailSerializer
    lookup_field = 'id'
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
        ]


class FeiraListAPIView(ListAPIView):
    serializer_class = FeiraListSerializer
    pagination_class = FeiraPageNumberPagination
    filter_backends = [
        SearchFilter
        ]
    search_fields = [
        'nome_feira',
        'bairro',
        'regiao5',
        'coddist__cod_distrito',
        'coddist__des_distrito',
        ]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Feira.objects.all()
        if query := self.request.GET.get("q"):
            # queryset_list = queryset_list.filter(
            #     Q(coddist__des_distrito__icontains=query) |
            #     Q(regiao5__icontains=query) |
            #     Q(nome_feira__icontains=query) |
            #     Q(bairro__icontains=query)
            # ).distinct()
            queryset_list = queryset_list.filter(
                Q(nome_feira__icontains=query) |
                Q(bairro__icontains=query) |
                Q(regiao5__icontains=query) |
                Q(coddist__cod_distrito__icontains=query) |
                Q(coddist__des_distrito__icontains=query)
            ).distinct()
        return queryset_list


class FeiraUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Feira.objects.all()
    serializer_class = FeiraDetailSerializer
    lookup_field = 'id'
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
        ]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
