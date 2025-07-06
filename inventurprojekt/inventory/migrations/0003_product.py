from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('purchase_link', models.URLField(blank=True)),
                ('is_apple', models.BooleanField(default=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='product_photos/')),
            ],
        ),
    ]
