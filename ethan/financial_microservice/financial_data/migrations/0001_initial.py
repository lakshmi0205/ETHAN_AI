# Generated by Django 4.2.4 on 2024-04-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISIN', models.CharField(max_length=20)),
                ('Symbol', models.CharField(max_length=10)),
                ('Date', models.DateField()),
                ('Asset_Class', models.CharField(max_length=50)),
                ('Quantity', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Market_Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Cost_Price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
