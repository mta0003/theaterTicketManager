# Generated by Django 2.1 on 2018-11-15 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('middleName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=400)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PriceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pricegroups', models.ManyToManyField(to='webapp.PriceGroup')),
                ('rows', models.ManyToManyField(to='webapp.Row')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('performances', models.ManyToManyField(to='webapp.Performance')),
            ],
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('sections', models.ManyToManyField(to='webapp.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('datePurchased', models.DateTimeField(verbose_name='Date Purchased')),
                ('door', models.BooleanField()),
                ('printed', models.BooleanField(default=False)),
                ('customer', models.ManyToManyField(to='webapp.Customer')),
                ('performance', models.ManyToManyField(to='webapp.Performance')),
                ('season', models.ManyToManyField(to='webapp.Season')),
                ('seat', models.ManyToManyField(to='webapp.Seat')),
                ('show', models.ManyToManyField(to='webapp.Show')),
            ],
        ),
        migrations.AddField(
            model_name='season',
            name='shows',
            field=models.ManyToManyField(to='webapp.Show'),
        ),
        migrations.AddField(
            model_name='row',
            name='seats',
            field=models.ManyToManyField(to='webapp.Seat'),
        ),
        migrations.AddField(
            model_name='performance',
            name='theater',
            field=models.ManyToManyField(to='webapp.Theater'),
        ),
    ]