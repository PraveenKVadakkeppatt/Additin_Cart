
from django.urls import path
from api import views
from users import views as UserViews
from product import views as ProductViews
from cart import views as CartViews
from orders import views as OrderViews
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('register/',UserViews.RegisterView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path ('profile/',UserViews.ProfileView.as_view()),

    path('product/',ProductViews.ProductListView.as_view()),
    path('product/<int:pk>/',ProductViews.ProductDetailsView.as_view()),

    path('cart/',CartViews.CartList.as_view()),
    path('cart/add/',CartViews.AddToCartView.as_view()),
    path('cart/items/<int:item_id>/',CartViews.ManageCartItemView.as_view()),

    path('orders/place/',OrderViews.PlaceOrderViews.as_view()),
    path('orders/',OrderViews.MyOrderView.as_view()),
    path('orders/<int:pk>/', OrderViews.OrderDetailView.as_view()),

]

