from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return self.name

    def get_category(self):
        return f'{self.category}'
