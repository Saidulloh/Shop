from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from django.urls import reverse

# Create your models here.

class Category(MPTTModel):
    STATUS_CHOICES = (
        ('True', 'True'),
        ('False', 'False')
    )
    title = models.CharField(max_length = 50)
    parent = TreeForeignKey(
        'self', 
        on_delete = models.CASCADE,
        null = True,
        blank = True,
        related_name = 'children' 
    )
    image = models.ImageField(upload_to = 'category/')
    status = models.CharField(choices = STATUS_CHOICES, max_length = 10)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "категория"

    def get_absolute_url(self):
        return reverse("category_detail", kwargfs = {'slug':self.slug})

    class MPTTMeta:
        order_insertion_by = ['title']


class Product(models.Model):
    STATUS_CHOICES = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True, blank = True)
    image = models.ImageField(upload_to="product/")
    status = models.CharField(choices=STATUS_CHOICES, default=True, max_length=10)
    slug = models.SlugField(unique = True)
    description = RichTextUploadingField(verbose_name="описание")
    price = models.DecimalField(decimal_places=2, max_digits=10)
    brand = models.CharField(max_length = 100, null = True, blank = True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("product_detail", kwargs = {"slug":self.slug})

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src = "{}" height = "50px" >'.format(self.image.url))
        else:
            return ''
    
    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "товар"
        ordering = ['-id']


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'product_images/')

    def __str__(self):
        return f'{self.id}'

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src = "{}" height = "50px" >'.format(self.image.url))
        else:
            return ''

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Review(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    review = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')
    created = models.DateTimeField(auto_now_add=True)

    def __Str__(self):
        return f'Review by {self.name} on {self.product}'

    class Meta:
        ordering = ['created']