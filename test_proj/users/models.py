from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kw):
        if not email:
            raise ValueError("'Email' field is requried")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **kw)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **kw):
        kw.setdefault('is_staff', True)
        kw.setdefault('is_superuser', True)

        if kw.get('is_staff') is False:
            raise ValueError('SuperUser must have "is_staff=True"')
        if kw.get('is_superuser') is False:
            raise ValueError('SuperUser must have "is_superuser=True"')
        
        return self.create_user(email, password, **kw)



class UserModel(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(unique=True, verbose_name='Електронна пошта',)
    phone = models.CharField(unique=True, null=True, blank=True, max_length=11, verbose_name='Номер телефону',)
    first_name = models.CharField(max_length=50,blank=True, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50,blank=True, verbose_name='Прізвище')
    birth_date = models.DateField(blank=True, null=True, verbose_name='Дата народження')
    user_image = models.ImageField(upload_to='user_image/', null=True, blank=True, verbose_name='Фото' )
    date_registration = models.DateTimeField(default=timezone.now(), verbose_name='Дата реєстрації')
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
    
    def __str__(self):
        return f'{self.first_name} - {self.email}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'