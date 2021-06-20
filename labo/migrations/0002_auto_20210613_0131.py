# Generated by Django 3.2 on 2021-06-12 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
