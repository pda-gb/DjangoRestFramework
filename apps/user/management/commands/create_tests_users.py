import json
import os
import random

from django.conf import settings
from django.core.management import BaseCommand, CommandError
from mimesis import Person

from apps.user.models import User

path_json = settings.BASE_DIR


# COUNT_ADMINISTRATORS = 2
# COUNT_MANAGERS = 3
# COUNT_DEVELOPERS = 10
# COUNT_USERS = COUNT_ADMINISTRATORS + COUNT_MANAGERS + COUNT_DEVELOPERS


def load_from_json(file_name):
    """
    :param file_name: имя необходимого json файла
    :return: выводит содержимое
    """
    with open(
            os.path.join(path_json, file_name + ".json"), "r", encoding="utf-8"
    ) as file_json:
        return json.load(file_json)


class Command(BaseCommand):
    def handle(self, *args, **options):
        person = Person('ru')
        for i in range(10):
            user_status = random.choice([1, 2, 3])
            # if  <= COUNT_ADMINISTRATORS:
            #     user_status = 1
            # if i >= (i - COUNT_ADMINISTRATORS):
            #     user_status = 2
            try:
                user = User(
                    username=person.username(template='U-d', ),
                    first_name=person.first_name(),
                    last_name=person.last_name(),
                    email=person.email(),
                    status=user_status
                )
            except IOError:
                raise CommandError(f'Error!!!')
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created '
                                                 f'{user.username}'))
