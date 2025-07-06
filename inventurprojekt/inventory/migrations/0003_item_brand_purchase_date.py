from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='item',
            name='purchase_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
