# Generated by Django 4.2.1 on 2023-05-14 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_alter_topic_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='blog_header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
