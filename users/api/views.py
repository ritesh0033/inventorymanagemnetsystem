from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from users.models import Role,User
from .serializers import RoleSerializer,UserSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle

class RoleView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get(self, request):
        roles = self.get_queryset()
        serializer = self.get_serializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response({
                "message": "Role  Added Successfully"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class RoleRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]


class UserView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    queryset = User.objects.all() 
    serializer_class = UserSerializer

    def get (self,request):
        users = self.get_queryset()
        serializer = self.get_serializer(users,many = True )
        return  Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer = self.get_serializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"User Added Sucessfully"

            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class UserRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]    