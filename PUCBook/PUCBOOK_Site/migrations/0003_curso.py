# Generated by Django 4.0.5 on 2022-10-10 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PUCBook_Site', '0002_caixacominformacoes_carona_grupo_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
    ]