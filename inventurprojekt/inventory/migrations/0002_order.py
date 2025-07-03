from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('due_date', models.DateField()),
                ('product', models.ForeignKey(on_delete=models.deletion.CASCADE, to='inventory.item')),
            ],
        ),
    ]
