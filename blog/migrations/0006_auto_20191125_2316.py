# Generated by Django 2.2.6 on 2019-11-25 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_dislikes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['date_published']},
        ),
    ]
