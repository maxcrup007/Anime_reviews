from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

def HomePage(request):
	return render(request, 'review/home.html')

def AboutPage(request):
	return render(request, 'review/about.html')

def AnimePage(request):
	return render(request, 'review/review.html')

def read_file(request):
    f = open('path/anime1.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()
    return render(request, "home.html", context)

def image(request):
    posx = Poster()
    variables = RequestContext(request,{
        'posx':posx
    })
    return render_to_response('home.html',variables)

def detail(request):
    comment = [
        { 'title' : 'Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season',
          'category' : 'advenger',
          'status' : 'finished',
          'detail' : '“นัตสึกิ สุบารุ” ฟื้นขึ้นมาในต่างโลก แถมชีวิตยังตกอยู่ในอันตรายทันทีเพราะโดนกลุ่มโจรเล่นงาน สุบารุได้รับความช่วยเหลือจากสาวผมเงินปริศนา'
                     'เพื่อทดแทนบุญคุณชายหนุ่มจึงช่วยเธอตามหาของที่เธอถูกขโมยไป ในขณะที่กำลังจะได้ของคืน ทั้งเขาและเธอกลับถูกฆ่าตาย '
                     'แต่สุบารุก็พบว่าเขาสามารถย้อนเวลากลับไปในช่วงก่อนเกิดเหตุได้ เขาจึงติดสินใจที่จะใช้พลังนี้เพื่อช่วยเหลือเด็กสาวผู้มีพระคุณออกจากชะตากรรมแห่งความตายให้ได้',
        },
        {'title': 'Kuma Kuma Kuma Bear',
         'category': 'love-comendy',
         'status': 'on-going',
         'detail': 'ยูนะ เกมเมอร์ฮิคิโคโมริ ที่ได้รับชุดหมีแรร์ หลังตอบคำถาม ทำให้เธอถูกพระเจ้า ส่งไปในโลกคู่ขนานแนวแฟนตาซี พร้อมชุดหมีที่ทำให้เธอแข็งแกร่ง '
                   'ยูน่าอายุสิบห้าปีชอบอยู่บ้านและเล่น VRMMO ที่เธอชื่นชอบเพื่อทำสิ่งอื่นรวมถึงการไปโรงเรียน '
                   'เมื่อการอัพเดทใหม่ที่แปลกประหลาดทำให้เธอมีชุดหมีที่ไม่เหมือนใครที่มีความสามารถอย่างล้นหลาม Yuna ถูกฉีกขาด'
                   'ชุดนั้นน่ารักเกินทน แต่น่าอายเกินกว่าที่จะสวมใส่ในเกม แต่ทันใดนั้นเธอก็พบว่าตัวเองถูกพาตัวไปสู่โลกของเกมเผชิญหน้ากับสัตว์ประหลาดและเวทมนตร์'
                   'ที่เป็นของจริงและชุดหมีกลายเป็นอาวุธที่ดีที่สุดที่เธอมี!',
         },
        {'title': 'Maou Gakuin no Futekigousha',
         'category': 'love-comendy',
         'status': 'finished',
         'detail': 'หลังจากตามกวาดล้างผู้คน ภูต รวมไปถึงเหล่าเทพเจ้ามายาวนานจนเริ่มรู้สึกเบื่อหน่ายกับสงครามอันไม่มีที่สิ้นสุด '
                   'จอมมารอานอสผู้โหดเหี้ยมก็วาดฝันถึงโลกที่มีแต่สันติสุขและตัดสินใจไปเกิดใหม่ ทว่าสิ่งที่รอเขาอยู่ในอีกสองพันปีให้หลังคือเหล่าผู้สืบทอด'
                   'สายเลือดที่อ่อนแอลงมากเพราะคุ้นชินกับสันติภาพ นอกจากนี้วิทยาการของเวทมนตร์ยังเสื่อมถอยลงจนถึงขีดสุดอานอสได้เข้าเรียนที่ ‘โรงเรียนจอมมาร’',
         },
    ]

    # context = { 'comment' : comment }
    #
    # return render(request, 'home.html', context)


    return  JsonResponse