from django.urls import path, include
from . import views

apipatterns = [
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]

urlpatterns = [
    path('api/', include(apipatterns)),
]
