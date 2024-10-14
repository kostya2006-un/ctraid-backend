from django.contrib.auth.base_user import BaseUserManager


class TelegramUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, user_id: str, password=None, **kwargs):
        if not user_id:
            raise ValueError("The given user_id must be set")

        user = self.model(user_id=user_id, **kwargs)

        # Если пароль задан, устанавливаем его
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)
        return user

    def create_user(self, user_id: str, password=None, **kwargs):
        kwargs.setdefault("is_staff", False)
        kwargs.setdefault("is_superuser", False)
        return self._create_user(user_id, password, **kwargs)

    def create_superuser(self, user_id: str, password="admin", **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return self._create_user(user_id, password, **kwargs)

