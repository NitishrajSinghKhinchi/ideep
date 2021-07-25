from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """ This is model manager for customized user model which uses mobile_no as default username field. """

    use_in_migrations = True

    def _create_user(self,mobile_no, email, password, **extra_fields):
        """ This method creates and saves new user through mobile_no, email and password. """
        if not mobile_no:
        	raise ValueError('The mobile no. must be set in')
        if not email:
            raise ValueError("Email is required!")
        email = self.normalize_email(email)
        mobile_no = self.normalize_email(mobile_no)
        user = self.model(mobile_no=mobile_no,email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,mobile_no, email, password=None, **extra_fields):
        """ This method creates and saves regular users using mobile_no, email and password. """

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(mobile_no,email, password, **extra_fields)

    def create_superuser(self,mobile_no,email,password, **extra_fields):
        """ This method creates and saves superuser using mobile_no, email and password. """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(mobile_no,email,password, **extra_fields)