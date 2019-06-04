from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.title

class Subcategory(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre")
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "subcategoria"
        verbose_name_plural = "subcategorias"
        ordering = ['-created']

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre")
    subcategory = models.ForeignKey('Subcategory', on_delete=models.SET_NULL, null=True)
    price = models.CharField(max_length=50, verbose_name="Precio")
    image = models.ImageField(verbose_name="Imagen", upload_to="products")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ['-created']

    def __str__(self):
        return self.title 