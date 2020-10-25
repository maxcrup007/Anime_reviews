from django.db import models


# class example(models.Model): 
#     data = models.JSONField(default={})



class poster(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='site_media')



class borader(models.Model):

    allcategory = (('love-comendy','love-comendy'),
					('advenger','advenger'),
					('action','action'),
					('fantasy"','fantasy'),
                    ('drama"','drama'),
                    ('romance"','romance'),
                    )

      title = models.CharField(max_length=200)
      status_ongoing = models.BooleanField(default=True)
      category = models.SmallIntegerField(max_length=200, choices=allcategory, default='love-comendy')
      detail = models.TextField(blank=True,null=True)


class spoiler(models.Model):


    allow_us = models.BooleanField(default=False)
    spoiled = models.TextField(blank=True,null=True)






#[ how to use this ] นำ models ก้อนนี่ไป set localhost ที่ views ตาม React-Native 
# ที่เชื่อมต่อกับหน้าบ้าน ให้ดู หน้าบ้านผมที่เป็น ไฟล์ HTML เสร็จแล้วก็ไป set path ที่หน้า urls (ของผมจะชื่อตาม app คือ anime_review/urls.py)