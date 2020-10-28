from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django_resized import ResizedImageField

class MyModel(models.Model):
    ...
    image1 = ResizedImageField(size=[500, 300], upload_to='whatever')
    image2 = ResizedImageField(size=[100, 100], crop=['top', 'left'], upload_to='whatever')
    image3 = ResizedImageField(size=[100, 100], crop=['middle', 'center'], upload_to='whatever')
    image4 = ResizedImageField(size=[500, 300], quality=75, upload_to='whatever')
    image5 = ResizedImageField(size=[500, 300], upload_to='whatever', force_format='PNG')




# class example(models.Model): 
#     data = models.JSONField(default={})



class poster(models.Model):
    name = models.CharField(max_length=255)
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


class Comment(models.Model):
    poster = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text








#[ how to use this ] นำ models ก้อนนี่ไป set localhost ที่ views ตาม React-Native 
# ที่เชื่อมต่อกับหน้าบ้าน ให้ดู หน้าบ้านผมที่เป็น ไฟล์ HTML เสร็จแล้วก็ไป set path ที่หน้า urls (ของผมจะชื่อตาม app คือ anime_review/urls.py)