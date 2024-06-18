# Generated by Django 5.0.3 on 2024-03-10 16:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0004_alter_book_updated_date_alter_borrow_updated_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='member',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]