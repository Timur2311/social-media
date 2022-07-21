# Generated by Django 4.0.6 on 2022-07-21 03:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post_images/')),
                ('file', models.FileField(upload_to='post_files/')),
                ('content', models.TextField()),
                ('shares_count', models.PositiveIntegerField(default=0)),
                ('type', models.CharField(choices=[('Public', 'Public'), ('Only_me', 'Only_me'), ('Friends', 'Friends')], max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('visible_for_users', models.ManyToManyField(related_name='visible_profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
