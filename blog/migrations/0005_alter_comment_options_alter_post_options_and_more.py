# Generated by Django 4.2.10 on 2024-02-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['create_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['create_on', 'author']},
        ),
        migrations.AddField(
            model_name='comment',
            name='challenge',
            field=models.SlugField(null=True),
        ),
    ]
