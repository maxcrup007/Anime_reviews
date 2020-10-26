from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


# class example(models.Model): 
#     data = models.JSONField(default={})



class poster(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='site_media')


class spoiler(models.Model):


    allow_us = models.BooleanField(default=False)
    spoiled = models.TextField(blank=True,null=True)


class Allboard(models.Model):

    allcategory = (	('Love-Comedy','Love-Comedy'),
					('Action','Action'),
					('Adventure','Adventure'),
					('Fantasy','Fantasy'),
                    ('Drama','Drama'),
                    ('Romance','Romance'))


    category = models.CharField(max_length=100, choices=allcategory, default='Love-Comedy')
    header = models.CharField(max_length=200)
    date = models.DateField(max_length=200)
    status_ongoing = models.BooleanField(default=True)
    favor = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    detail = models.TextField(blank=True,null=True)
    reviews = models.TextField(blank=True,null=True)



    def __str__(self):
    		return '{}-{}'.format(self.header,self.category)


class commentation(models.Model):

    comment = models.TextField(blank=True,null=True)
    favor = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    dropdown = models.TextField(blank=True,null=True)
    mute = models.BooleanField(default=True)






#[ how to use this ] นำ models ก้อนนี่ไป set localhost ที่ views ตาม React-Native 
# ที่เชื่อมต่อกับหน้าบ้าน ให้ดู หน้าบ้านผมที่เป็น ไฟล์ HTML เสร็จแล้วก็ไป set path ที่หน้า urls (ของผมจะชื่อตาม app คือ anime_review/urls.py)