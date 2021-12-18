# Generated by Django 2.2.19 on 2021-12-18 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        erialize=False,
                                        verbose_name='ID')),
                ('title', models.CharField(help_text='Дайте название группе',
                                           max_length=200,
                                           verbose_name='Заголовок')),
                ('slug', models.SlugField(
                    help_text='Укажите ключ адреса страницы группы',
                    unique=True,
                    verbose_name='Слаг')),
                ('description', models.TextField(
                    help_text='Опишите группу',
                    verbose_name='Описание группы')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True,
                                    null=True,
                                    upload_to='posts/'),
        ),
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='posts', to='posts.Group'),
        ),
    ]
