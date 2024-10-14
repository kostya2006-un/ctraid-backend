from django.core.management import BaseCommand
from django.core.management.base import CommandParser

from typing import Tuple, Dict, Optional
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Creates an admin user non-interactively if it doesn't exist"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("--user-id", help="Admin's User ID", required=True)

        parser.add_argument("--password", help="Admin's Password", required=True)

    def handle(self, *args: Tuple, **options: Dict) -> Optional[str]:

        if User.objects.filter(user_id=options["user_id"]).exists():
            return

        User.objects.create_superuser(
            user_id=options["user_id"],
            first_name=options["user_id"],
            password=options["password"],
        )
