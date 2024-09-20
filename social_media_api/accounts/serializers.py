from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token

class UserSerializer(serializer(serializers.ModelSerializer):
        class Meta:
            model = CustomUser
            fields = ['username', 'email', 'bio', 'profile_picture', 'followers', 'password']
            extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = get_user_model().objects.create_user(
                username=validated_data['username'],
                password=validated_data['password'],
                email=validated_data['email']
            )
            Token.objects.create(user=user)

class UserLoginSerializer(serializers.CharField():
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        user = get_user_model().obes.filter(username=username).first()

        if user is not None and user.check_password(password):
           token, created = Token.objects.get_or_create(user=user)
           return {
               "username": user.username,
               "token": token.key
          }
        raise serializer.ValidationError("Invalid credentials")

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class UserLoginView(ObtainAuthToken):
    serializer_class = UserLoginSerializer
