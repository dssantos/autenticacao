from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.categoria


class Produto(models.Model):
    produto = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "produto"
        verbose_name_plural = "produtos"

    def __str__(self):
        return self.produto
