from rest_framework import generics
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
# Create your views here.


class CartList(generics.ListCreateAPIView):
    """
    API view for listing and creating carts.
    """
    queryset = Cart.objects.first()
    serializer_class = CartSerializer
    pagination_class = None

    def get_queryset(self):
        """
        Return the cart associated with the current user.
        """
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Create a cart for the current user.
        """
        user = self.request.user
        cart = Cart.objects.create(user=user)

class CartDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a cart.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_object(self):
        """
        Return the cart associated with the current user.
        """
        return Cart.objects.get(user=self.request.user)



class CartItemList(generics.ListCreateAPIView):
    """
    API view for listing and creating cart items.
    """
    serializer_class = CartItemSerializer

    def get_queryset(self):
        """
        Return the cart items associated with the current user's cart.
        """
        user = self.request.user
        cart = Cart.objects.get(user_id=user.id)
        return CartItem.objects.filter(cart_id=cart.id) 
    
    def perform_create(self, serializer):
        """
        Create a cart item associated with the current user's cart.
        """
        user = self.request.user
        cart = Cart.objects.get(user_id=user.id)
        serializer.save(cart=cart)


class CartItemDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a cart item.
    """
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        cart = Cart.objects.get(user_id=user.id)
        return CartItem.objects.filter(cart_id=cart.id)