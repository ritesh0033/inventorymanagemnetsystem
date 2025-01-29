from  rest_framework.generics import GenericAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from suppliers.models import Supplier
from .serializers import SupplierSerializer


class SupplierView(GenericAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def get(self,request):
        suppliers = self.get_queryset()
        serializer = self.get_serializer(suppliers,many = True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def post(self,request):
        serializer = self.get_serializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Supplier addes Sucessfully"

            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class SupplierRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView) :
    queryset = Supplier.objects.all()
    serializer_class =   SupplierSerializer 