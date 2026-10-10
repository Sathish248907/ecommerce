from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import (UserRegistrationSerializer, UserLoginSerializer,
    UserProfileSerializer, UserUpdateSerializer, UserListSerializer)
from .permissions import IsAdminUser

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({'message':'Account created.','user':UserProfileSerializer(user).data,'tokens':{'access':str(refresh.access_token),'refresh':str(refresh)}}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({'message':'Login successful.','user':UserProfileSerializer(user).data,'tokens':{'access':str(refresh.access_token),'refresh':str(refresh)}})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_serializer_class(self):
        return UserUpdateSerializer if self.request.method in ['PUT','PATCH'] else UserProfileSerializer
    def get_object(self):
        return self.request.user
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = UserUpdateSerializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Profile updated.','user':UserProfileSerializer(instance).data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = [IsAdminUser]
    queryset = User.objects.filter(role='customer').order_by('-date_joined')

class UserDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = UserListSerializer
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
