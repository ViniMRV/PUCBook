# Generated by Django 4.0.5 on 2022-10-14 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PUCBook_Site', '0005_remove_usuario_aniversario_remove_usuario_curso_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CaixaComInformacoes',
        ),
        migrations.DeleteModel(
            name='Carona',
        ),
        migrations.DeleteModel(
            name='Grupo',
        ),
        migrations.DeleteModel(
            name='Mensagem',
        ),
    ]