# Generated by Django 5.1.2 on 2024-10-31 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_caption_alter_post_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='posts_images/', verbose_name='Imagen'),
        ),
    ]
