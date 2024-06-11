from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from meetings.models import Meeting

class Command(BaseCommand):
    help = 'Create default user groups and assign permissions'

    def handle(self, *args, **kwargs):
        admin_group, created = Group.objects.get_or_create(name='Администраторы')
        organizer_group, created = Group.objects.get_or_create(name='Организаторы')
        moderator_group, created = Group.objects.get_or_create(name='Модераторы')
        participant_group, created = Group.objects.get_or_create(name='Участники')
        guest_group, created = Group.objects.get_or_create(name='Гости')

        content_type = ContentType.objects.get_for_model(Meeting)

        create_meeting_permission, created = Permission.objects.get_or_create(
            codename='can_create_meeting',
            name='Can create meeting',
            content_type=content_type,
        )
        edit_meeting_permission, created = Permission.objects.get_or_create(
            codename='can_edit_meeting',
            name='Can edit meeting',
            content_type=content_type,
        )
        delete_meeting_permission, created = Permission.objects.get_or_create(
            codename='can_delete_meeting',
            name='Can delete meeting',
            content_type=content_type,
        )

        admin_group.permissions.add(create_meeting_permission, edit_meeting_permission, delete_meeting_permission)
        organizer_group.permissions.add(create_meeting_permission, edit_meeting_permission)
        moderator_group.permissions.add(edit_meeting_permission)

        self.stdout.write(self.style.SUCCESS('Successfully created groups and assigned permissions'))
