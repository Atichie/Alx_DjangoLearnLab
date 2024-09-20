from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer
from .models import CustomUser
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get or create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors)

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(id=token.user_id)
        return Response({'token': token.key, 'user_id': user.id})

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_to_folllow = get_object_or_404(CustomUser, pk=kwargs['pk'])
        if user_to_follow != request.user:
            request.user.following.add(user_to_follow)
            return Response({"detail": f"Ypu are now following {user_to_follow.username}"})
        return Response({"detail": "You cannot follow yourself."}, status=400)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_to_unfollow = get_object_or_404(CustomUser, pkkwargs['pk'])
        if user_to_unfollow in request.user.following.all():
            request.user.following.remove(user_to_unfollow)
            return Response({"detail": "You are not following this user."}, status=400)

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
