# Generated by Django 3.2.9 on 2021-11-16 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Can set book as returned'),)},
        ),
    ]
