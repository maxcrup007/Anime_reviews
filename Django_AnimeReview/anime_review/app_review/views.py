from django.shortcuts import render
from django.http import HttpResponse

def HomePage(request):
	return render(request, 'review/home.html')

def AboutPage(request):
	return render(request, 'review/about.html')

def AnimePage(request):
	return render(request, 'review/review.html')





    # Set หน้าบ้าน (React-Native ตรงหน้านี้เลยเสร็จแล้ว ส่งไป set path ที่ anime_review/urls.py )