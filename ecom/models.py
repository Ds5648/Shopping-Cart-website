from django.db import models

# Create your models here.
class product (models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    product_desc=models.CharField(max_length=300)
    category=models.CharField(max_length=50,default=0)
    subcategory=models.CharField(max_length=50,default=0)
    price=models.FloatField(max_length=2000,default=10)
    pub_date=models.DateField()
    images=models.ImageField(upload_to="ecom/images",default="")


    def __str__ (self):
        return self.product_name