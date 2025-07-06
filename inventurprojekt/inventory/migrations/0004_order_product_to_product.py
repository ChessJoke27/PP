from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_product'),
        ('inventory', '0003_item_brand_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=models.CASCADE, to='inventory.product'),
        ),
    ]
