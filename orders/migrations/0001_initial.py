# Generated by Django 4.2 on 2025-01-15 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                (
                    'table_number',
                    models.DecimalField(
                        decimal_places=0,
                        max_digits=100
                    )
                ),
                (
                    'items',
                    models.JSONField()
                ),
                (
                    'total_price',
                    models.DecimalField(decimal_places=2, max_digits=100000)
                ),
                (
                    'status',
                    models.CharField(
                        choices=[
                            ('PND', 'в ожидании'),
                            ('RED', 'готово'),
                            ('PDF', 'оплачено')
                        ],
                        default='PND',
                        max_length=3
                    )
                ),
            ],
        ),
    ]
