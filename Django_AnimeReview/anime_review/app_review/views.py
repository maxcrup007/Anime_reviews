from django.shortcuts import render
from django.http import HttpResponse
from .serializers import ReviewSerializer
from .models import *


def HomePage(request):
	return render(request, 'review/home.html') #ไม่ใช่

def AboutPage(request):
	return render(request, 'review/about.html') #ไม่ใช่

def AnimePage(request):
	return render(request, 'review/review.html') #ไม่ใช่





    # Set หน้าบ้าน (React-Native ตรงหน้านี้เลยเสร็จแล้ว ส่งไป set path ที่ anime_review/urls.py )