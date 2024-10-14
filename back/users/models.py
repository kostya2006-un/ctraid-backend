from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import TelegramUserManager


class User(AbstractUser):
    email = models.EmailField(_("Email address"), blank=True, null=True)  # Email необязательный

    user_id = models.CharField(
        _("User ID"), max_length=255, unique=True, primary_key=True
    )

    USERNAME_FIELD = "user_id"  # Устанавливаем user_id как поле для авторизации
    REQUIRED_FIELDS = []  # Убираем обязательные поля
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='telegram_user_groups',  # Уникальное имя для обратной связи
        blank=True,
        verbose_name=_("groups")
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='telegram_user_permissions',  # Уникальное имя для обратной связи
        blank=True,
        verbose_name=_("user permissions")
    )
    objects = TelegramUserManager()  # Менеджер для работы с Telegram

    is_bot = models.BooleanField(_("Is bot"), default=False)
    date_joined = models.DateTimeField(_("Date joined"), auto_now_add=True)
    username = models.CharField(_("Username"), max_length=255, blank=True, null=True)

    # Оставляем поле password для совместимости с админкой
    password = models.CharField(_("password"), max_length=128, null=True, blank=True)

    def __str__(self) -> str:
        return self.username or str(self.user_id)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

