from django.db import models

# Create your models here.

class category(models.Model):
    designation = models.CharField(verbose_name='Category designation',max_length=20)
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.designation

class plantes(models.Model):
    name = models.CharField(verbose_name='Plantes', max_length=50)
    image = models.ImageField(verbose_name='Image', upload_to='images/plantes%Y/%m/%d',blank=True,null=True)
    description = models.TextField(verbose_name='Description')
    medecinal_benifit = models.TextField(verbose_name='Medecinal benefit')
    use = models.TextField(verbose_name='How use')
    culture = models.TextField(verbose_name='Culture')
    source = models. URLField(verbose_name='Source')

    def __str__(self):
        return self.name
    
