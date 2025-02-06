from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=255,unique=True, verbose_name="Названиe")
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name="URL")
    isvisible = models.BooleanField(default=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering=('id',)

    def __str__(self):
        return self.name

class Products(models.Model):

    name = models.CharField(max_length=255, verbose_name="Названиe")
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name="URL")
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, verbose_name="Цена")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name="Изображение")
    discount = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, verbose_name="Скидка")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    isvisible = models.BooleanField(default=True)

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} Количество: {self.quantity}'

    def display_id(self)-> str:
        return f'{self.id:03}'

    def sell_pryce(self):
        if self.discount:
            return round(self.price-self.price*self.discount/100,2)
        return self.price



