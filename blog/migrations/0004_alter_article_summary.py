# Generated by Django 5.2 on 2025-07-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_article_summary"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="summary",
            field=models.TextField(),
        ),
    ]
