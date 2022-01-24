from django.db import migrations
from django.db.migrations import operations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(app,schema_editor):
        user = CustomUser(name = 'nikhil',
        email = 'test@gmail.com',
        phone = '1234567890',
        gender= 'male',
        is_staff = True,
        is_superuser = True,
        )
        user.set_password('test123')
        user.save()

    dependencies = []

    operations= [
        migrations.RunPython(seed_data),
    ]