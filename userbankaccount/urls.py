from django.urls import URLPattern, path
from . import views



urlpatterns = [
    path('', views.UserExchangeAPIView, name='user_Exchange'),
    path("user-info/", views.UserInfoAPIView, name='user_Info'),
    # path('', views.Add_List_AccountAPIView.as_view(), name='add account'),
    # path('<int:id>', views.Account_DetailAPIView.as_view(), name='account details'),
]