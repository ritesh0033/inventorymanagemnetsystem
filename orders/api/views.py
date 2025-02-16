from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from orders.models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from rest_framework.pagination import PageNumberPagination

class OrderView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request):
        orders = self.get_queryset()  
        serializer = self.get_serializer(orders, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)  

    def post(self, request):
        serializer = self.get_serializer(data=request.data) 
        if serializer.is_valid():
            serializer.save() 
            return Response({
                "message": "Order added successfully"
            }, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)  

class OrderRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
