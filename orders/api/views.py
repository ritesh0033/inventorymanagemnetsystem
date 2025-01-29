from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from orders.models import Order
from .serializers import OrderSerializer

class OrderView(GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request):
        orders = self.get_queryset()  # Fetch the queryset
        serializer = self.get_serializer(orders, many=True)  # Pass the queryset, not the model class
        return Response(serializer.data, status=status.HTTP_200_OK)  # Use 200 OK for GET requests

    def post(self, request):
        serializer = self.get_serializer(data=request.data)  # Deserialize the incoming data
        if serializer.is_valid():
            serializer.save()  # Save the new order to the database
            return Response({
                "message": "Order added successfully"
            }, status=status.HTTP_201_CREATED)  # Status 201 for resource creation
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Handle validation errors

class OrderRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
