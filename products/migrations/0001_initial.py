# Generated by Django 4.0.4 on 2022-07-01 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('brand_website', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('category_name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='categories')),
                ('category_code', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='ColorVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('color_name', models.CharField(max_length=100, null=True, unique=True, verbose_name='Color Name')),
            ],
            options={
                'verbose_name_plural': 'Color Variation',
            },
        ),
        migrations.CreateModel(
            name='Countreies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('name', models.CharField(max_length=255, null=True, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Country',
            },
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Product Attribute',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('product_name', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('meta', models.TextField(blank=True, max_length=500, null=True)),
                ('short_descriptions', models.CharField(blank=True, max_length=1200, null=True, verbose_name='Short DesColorVariationcription')),
                ('long_description', models.TextField(blank=True, null=True, verbose_name='Long Description')),
                ('alter_text', models.CharField(blank=True, max_length=400, null=True)),
                ('sku', models.CharField(max_length=20, null=True, unique=True, verbose_name='SKU')),
                ('feature_image', models.ImageField(null=True, upload_to='products')),
                ('sold_count', models.IntegerField(blank=True, null=True)),
                ('expire_rate', models.DateField(blank=True, null=True)),
                ('is_stock', models.BooleanField(default=True, verbose_name='Is Stock')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='products.brand')),
                ('category', models.ManyToManyField(related_name='Category_products', to='products.categories')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country', to='products.countreies')),
            ],
            options={
                'verbose_name_plural': 'Product',
            },
        ),
        migrations.CreateModel(
            name='SizeVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('size_name', models.CharField(max_length=100, null=True, unique=True, verbose_name='Size Name')),
            ],
            options={
                'verbose_name_plural': 'Size Variation',
            },
        ),
        migrations.CreateModel(
            name='WeightVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('weight_name', models.CharField(max_length=200, null=True, unique=True, verbose_name='Weight Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Variation_with_Price_variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('regular_price', models.FloatField(blank=True, null=True)),
                ('selling_price', models.FloatField(blank=True, null=True)),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.colorvariation', verbose_name='Product Color')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variant', to='products.products', verbose_name='Product')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.sizevariation', verbose_name='Product Size')),
                ('weight', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.weightvariation', verbose_name='Product Weight')),
            ],
            options={
                'verbose_name_plural': 'Product Variation',
            },
        ),
        migrations.CreateModel(
            name='Sub_Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('sub_category_name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='sub_categories')),
                ('description', models.TextField(blank=True, max_length=1500, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='products.categories')),
            ],
            options={
                'verbose_name_plural': 'Sub Category',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('slidername', models.CharField(blank=True, max_length=255, null=True)),
                ('slider_image', models.ImageField(blank=True, upload_to='slider_images')),
                ('url_link', models.CharField(blank=True, max_length=400, null=True, verbose_name='Slider URL Link')),
                ('position', models.PositiveIntegerField(null=True)),
                ('home_shown', models.BooleanField(default=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_slider', to='products.categories', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Sliders',
            },
        ),
        migrations.AddField(
            model_name='products',
            name='sub_category',
            field=models.ManyToManyField(related_name='Sub_category_products', to='products.sub_categories'),
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('star_count', models.IntegerField(null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.products')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.profile', verbose_name='Profile Name')),
            ],
            options={
                'verbose_name_plural': 'Product Review',
            },
        ),
        migrations.CreateModel(
            name='Product_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('image', models.ImageField(blank=True, upload_to='product_image_gallery')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='products.products')),
            ],
            options={
                'verbose_name_plural': 'Product Image',
            },
        ),
    ]
