# from django.contrib.auth.models import Group, User
# from rest_framework import permissions, viewsets
import django_filters
from rest_framework import permissions, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
#
# from api.serializers import UserSerializer, GroupSerializer
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all().order_by('name')
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#  def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             # snippet["name"] = serializer.validated_data["name"]
#             # snippet["age"] = serializer.validated_data["age"]
#             # snippet.save()
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# pagination, filtering and ordering
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import MyModel
from .serializers import MyModelSerializer


class MyModelPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class MyModelFilter(django_filters.FilterSet):
    # Use __icontains for case-insensitive search on the 'name' field
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = MyModel
        fields = ['name']


class MyModelListView(ListAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    pagination_class = MyModelPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        'name': ['icontains']
    }
    # filterset_class = MyModelFilter
    ordering_fields = ['name', 'id']
    ordering = ['name']


# setting permissions for only authenticated users
class MyModelListCreateView(ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# view that list all objects, it allows only the owner to update and delete it
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user



class MyModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
