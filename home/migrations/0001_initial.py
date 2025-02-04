# Generated by Django 5.0.4 on 2024-05-18 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default_img/user_img.png', null=True, upload_to='about/')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('title', models.TextField()),
            ],
            options={
                'db_table': 'about',
            },
        ),
    ]
