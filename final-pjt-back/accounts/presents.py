from django.contrib.auth.models import BaseUserManager

# username을 필수값으로 쓰지 않는 CustomUserManager를 재정의
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수입니다.')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )

        # 비밀번호는 해싱하여 저장
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)
