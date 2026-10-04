from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('category', models.CharField(choices=[('sell', 'Продам'), ('buy', 'Куплю'), ('service', 'Услуги'), ('lost', 'Потеряно и найдено')], default='sell', max_length=10, verbose_name='Раздел')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена, ₽')),
                ('contact', models.CharField(max_length=60, verbose_name='Контакт')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
            ],
            options={
                'verbose_name': 'объявление',
                'verbose_name_plural': 'объявления',
                'ordering': ['-created'],
            },
        ),
    ]
