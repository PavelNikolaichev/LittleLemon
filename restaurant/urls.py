from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import views

apipatterns = [
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]

urlpatterns = [
    path('api/', include(apipatterns)),
    path('api-token-auth/', obtain_auth_token),
]
