from django.db.models import Avg, Min, Max, Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Ship
from .serializers import ShipSerializer
from .filters import ShipFilter


class ShipViewSet(viewsets.ModelViewSet):
    queryset = Ship.objects.all()[:100]
    serializer_class = ShipSerializer
    filter_class = ShipFilter
    filter_backends = [DjangoFilterBackend]

    @action(detail=False, methods=["get"])
    def mean_length(self, request):
        mean_length_ = Ship.objects.aggregate(mean_length=Avg("length"))
        return Response(mean_length_)

    @action(detail=False, methods=["get"])
    def min_length(self, request):
        min_length_ = Ship.objects.aggregate(min_length=Min("length"))
        return Response(min_length_)

    @action(detail=False, methods=["get"])
    def max_length(self, request):
        max_length_ = Ship.objects.aggregate(max_length=Max("length"))
        return Response(max_length_)

    @action(detail=False, methods=["get"])
    def total_count(self, request):
        total_count_ = Ship.objects.aggregate(total_count=Count("pk"))
        return Response(total_count_)
