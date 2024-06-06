from dj_rest_auth.serializers import LoginSerializer, TokenSerializer, UserDetailsSerializer, TokenModel
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

class CustomLoginSerializer(LoginSerializer):
    username = None #username은 더이상 받지 않음을 의미
    
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'name', 'nickname','gender', 'image', 'age_group', 'like_products')
        read_only_fields = ['id',]
        
    
class CustomTokenSerializer(TokenSerializer):
    user = CustomUserDetailsSerializer(read_only=True)
    class Meta:
        model = TokenModel
        fields = ['key', 'user', ]

class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(required = True)
    nickname = serializers.CharField(required=True)
    location = serializers.CharField(default='')
    gender = serializers.IntegerField(default = 0)
    age_group = serializers.IntegerField(default=0)
    image = serializers.ImageField(default='')
    
    
    def get_cleaned_data(self):
        return {
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'location': self.validated_data.get('location', ''),
            'name': self.validated_data.get('name', ''),
            'gender' : self.validated_data.get('gender',0),
            'age_group': self.validated_data.get('age_group', '0'),
            'image' : self.validated_data.get('image', '')
    }
        
    def save(self, request):
        user = super().save(request)
        user.nickname = self.data.get('nickname')
        user.name = self.data.get('name')
        user.gender = self.data.get('gender')
        user.age_group = self.data.get('age_group')
        user.image = self.data.get('image')
        user.location = self.data.get('location')
        user.save()
        return user



class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'nickname',
            'name',
            'gender',
            'location',
            'age_group'
        ]
    def update(self, instance, validated_data):
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class UserProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'image'
        ]

class UserLikeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =  get_user_model()