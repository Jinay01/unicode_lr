from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class MyAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")

        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email), password=password,)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    ROLE_CHOICES = [("Student", "Student"), ("Faculty",
                                             "Faculty"), ("Institute", "Institute")]

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=20)
    # l_name = models.CharField(max_length=20)
    # profile_image = models.ImageField(
    #     default="profile_images/default.png",
    #     upload_to="profile_images",
    #     blank=True,
    #     null=True,
    # )
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # verification
    is_institute = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    role = models.CharField(max_length=20, blank=False, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name

    USERNAME_FIELD = "email"

    objects = MyAccountManager()

    def save(self, *args, **kwargs):
        self.username = self.email
        super(Account, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


class Institute(Account):
    address = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.name


class Unreg_students(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100, null=True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class Students(Account):
#     # institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
#     department = models.CharField(
#         max_length=5, blank=False
#     )
#     pointer = models.DecimalField(
#         default=0.00, max_digits=5, decimal_places=2, blank=False, null=False
#     )
#     admission_year = models.CharField(max_length=2, blank=False)
#     unique_id = models.CharField(max_length=100, blank=False, null=False)


# class Faculty(Account):
