from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Company
from .serializers import CompanySerializer
from users.permissions import IsAdminUser, IsAdminOrReadOnly


class CompanyListCreateView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer

    def get_permissions(self):
        return [IsAdminUser()] if self.request.method == 'POST' else [permissions.IsAuthenticated()]

    def get_queryset(self):
        qs = Company.objects.all()
        return qs if self.request.user.role == 'admin' else qs.filter(is_active=True)


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response({'message': 'Brand deactivated.'}, status=status.HTTP_200_OK)
