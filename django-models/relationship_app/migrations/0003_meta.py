# Generated by Django 2.2.12 on 2024-08-20 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='relationship_app.Book')),
            ],
            bases=('relationship_app.book',),
        ),
    ]
