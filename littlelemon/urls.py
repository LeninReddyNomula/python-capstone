from django.urls import path,include
from rest_framework.routers import DefaultRouter,SimpleRouter
from . import views

# router = SimpleRouter()
# router.register(r'users', views.UserView,basename='user')


router = DefaultRouter()
router.register(r'users', views.UserView,basename='user')
router.register(r'booking',views.BookingViewSet,basename='booking')



urlpatterns = [

   # path('user/',views.UserView.as_view({'get':'list','post':'create'}) ),
    path('',include(router.urls)),
    path('items/',views.MenuItemView.as_view({'get':'list'})),
    path('items/<int:pk>', views.SingleMenuItem.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('users/<int:pk>/set_password/', views.UserViewSet.as_view({'post': 'set_password'}), name='set_password'),
    
]

