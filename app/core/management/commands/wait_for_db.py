"""
Django command to wait for database to be available.
"""
import time

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django wait for database."""

    def handle(self, *args, **options) -> None:
        """Entry point for command."""
        self.stdout.write(self.style.WARNING("Wating for database ..."))
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write(
                    self.style.NOTICE(
                        "Database unavailable, waiting 1s ..."
                        )
                    )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
