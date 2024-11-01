from django.urls import include, path
from rest_framework import routers
from rest_framework.generics import ListCreateAPIView, ListAPIView

from api import views
from api.views import MyModelListView, MyModelListCreateView, MyModelDetailView

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('list/', MyModelListView.as_view(), name='list'),
    path('list-api/', MyModelListCreateView.as_view(), name='list-api'),
    path('mymodel/<int:pk>/', MyModelDetailView.as_view(), name='mymodel-detail'),
]
