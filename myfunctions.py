from django.core.files.storage import FileSystemStorage
from django.shortcuts import *
from pymysql import *
from django.views.decorators.csrf import csrf_exempt
con=Connect (host='127.0.0.1',user='root',password='1234',database='login')
cr=con.cursor()
def one(request):
        return  render(request,'one.html')
def navbr(request):
        return  render(request,'navbr.html')
def login(request):
        return render(request,'login.html')

def course(request):
        s = "select * from admin"
        cr.execute(s)
        l = cr.fetchall()
        l1 = []
        for i in l:
                d = {'cname': i[0],'id':i[5], 'ctype': i[1], 'cduration': i[2], 'cdescription': i[3], 'cfee': i[4], 'img': i[6]}
                l1.append(d)

        return  render(request,'course.html',{'ar':l1})
def move(request):
        cid=request.GET.get('id')
        s = "select * from admin where cid={} ".format(cid)
        cr.execute(s)
        l = cr.fetchall()
        l1 = []
        for i in l:
                d = {'cname': i[0],'id':cid, 'ctype': i[1], 'cduration': i[2], 'cdescription': i[3], 'cfee': i[4] ,'img': i[6]}
                l1.append(d)
        return render(request, 'cart.html', {'ar': l1})
# def home(request):
#         return  render(request,'home.html')
def courses(request):
        return  render(request,'courses.html')
def cart(request):
        return  render(request,'cart.html')
@csrf_exempt
def home(request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        lucky= request.POST.get('lucky')
        s="select * from details"
        cr.execute(s)
        l=cr.fetchall()
        for i in l:
                if(i[1]==email):
                         return HttpResponse("email already exits")
        s="insert into details(name,email,password,address,lucky) values ('{}','{}','{}','{}','{}')".format(name,email,password,address,lucky)
        cr.execute(s)
        con.commit()
        return redirect(login)


@csrf_exempt
def courses(request):
        # name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # address = request.POST.get('address')
        s="select * from details"
        cr.execute(s)
        l=cr.fetchall()
        for i in l:
                if i[1]==email and i[2] ==password:
                        return redirect(course)

        else:
           return HttpResponse("email or password is wrong")

@csrf_exempt
def fpass(request):
        return  render(request,'fpass.html')

@csrf_exempt
def forget(request):
        email=request.POST.session('email')
        opass= request.POST.get('opass')
        npass= request.POST.get('npass')
        cpass= request.POST.get('cpass')
        s = "select * from details"
        cr.execute(s)
        l = cr.fetchall()
        if npass!=cpass:
                return HttpResponse("confirm passwword not match")
        else:
                s="update details set password='{}' where email='{}' and password='{}' ".format(npass,email,opass)
                cr.execute(s)
                con.commit()
                return redirect(login)
def forg(request):
        return render(request,'forget.html')
def fo(request):
        email=request.GET.get('email')
        lucky=request.GET.get('lucky')
        s="select * from details"
        cr.execute(s)
        l=cr.fetchall()
        for i in l:
                if i[1]==email and i[4]==lucky:
                        d={'password':i[2]}
                        return render(request,'msg.html',{'ar':d})
        return HttpResponse("Email ID or security answer not valid")
def ahome(request):
        s="select * from details"
        cr.execute(s)
        l=cr.fetchall()
        l1=[]
        for i in l:
                d={'name':i[0],'email':i[1],'password':i[2],'address':i[3]}
                l1.append(d)
        return render(request,'ahome.html',{'ar':l1})
def acourse(request):
        return render(request,'acourse.html')

@csrf_exempt
def dcourse(request):
       cname = request.POST.get('cname')
       ctype= request.POST.get('ctype')
       cduration= request.POST.get('cduration')
       cdescription = request.POST.get('cdescription')
       cfee = request.POST.get('cfee')
       myfile = request.FILES['myfile']
       sa = myfile.name
       a = 1
       if sa.endswith('jpg') or sa.endswith('jpeg') or sa.endswith('png'):
               fs = FileSystemStorage()
               a += 1
               filename = fs.save('course/' + str(a) + '.jpg', myfile)
               uploaded_url = fs.url(filename)
               s = "insert into admin(cname,ctype,cduration,cdescription,cfee,img) values ('{}','{}','{}','{}','{}','{}')".format(cname,ctype,cduration,cdescription,cfee, uploaded_url)

               cr.execute(s)
               con.commit()

               return HttpResponse("submitted")
       else:
               return HttpResponse("Wrong Image Type")


def imgexample(request):
        return render(request,'imgexample.html')
# @csrf_exempt
# def imge(request):
#         myfile=request.FILES['myfile']
#         s=myfile.name
#         a=1
#         print(myfile)
#         if s.endswith('jpg') or s.endswith('jpeg') or s.endswith('png'):
#                 fs=FileSystemStorage()
#                 a+=1
#                 filename=fs.save('course/'+str(a)+'.jpg',myfile)
#                 uploaded_url=fs.url(filename)
#                 s="insert into imgexample (img) values('{}')".format(uploaded_url)
#                 cr.execute(s)
#                 con.commit()
#                 return HttpResponse("Data Inserted")
#         else:
#                 return HttpResponse("Wrong Image Type")


def display(request):
        return render(request,display.html)
# def bcourse(request):
#         s = "select * from admin"
#         cr.execute(s)
#         l = cr.fetchall()
#         l1 = []
#         for i in l:
#             d = {'cname': i[0], 'ctype': i[1], 'cduration': i[2], 'cdescription': i[3],'cfee':i[4],'img':i[5]}
#             l1.append(d)
#         print(l1)
#
#         return render(request,'display.html', {'ar': l1})
