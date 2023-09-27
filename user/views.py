from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import csv

# Create your views here.
def index(request):
    # login start
    if request.method=="POST":
        email = request.POST.get("email")
        passwd = request.POST.get("passwd")
        x = signup.objects.all().filter(email=email, password=passwd).count()
        y = signup_reporter.objects.all().filter(email=email, password=passwd).count()
        if x==1 or y==1:
            request.session['userid']=email
            return HttpResponse("<script>alert('Login Successfully');location.href='/profile/'</script>")
        else:
            return HttpResponse("<script>alert('Your Email or Password is incorrect !!');location.href='/index/'</script>")
    # Login End
    
    categorys = category.objects.all().filter().order_by('-id')
    headline = mynews.objects.all().order_by('-id')
    latest = mynews.objects.all().order_by('-id')[0:8]
    pmmodi = mynews.objects.all().filter(newscategory=4)[0:4]
    cricket = mynews.objects.all().filter(newscategory=6)[0:4]
    phone = mynews.objects.all().filter(newscategory=3)[0:4]
    science = mynews.objects.all().filter(newscategory=1)[0:4]
    mydict = {"categorys":categorys, "headline":headline, "pmmodi":pmmodi, "cricket":cricket, "phone":phone, "science":science, "latest":latest}
    return render(request, 'user/index.html', context=mydict)

####################################################

def about(request):
    categorys = category.objects.all().filter().order_by('-id')
    return render(request, 'user/about.html', {"categorys":categorys})

####################################################

def viewnews(request):
    categorys = category.objects.all().filter().order_by('-id')
    cid = request.GET.get('news')
    snews = mynews.objects.all().order_by('-id')
    cat = category.objects.all()
    if cid is not None:
        snews = mynews.objects.all().filter(newscategory=cid).order_by('-id')
    return render(request, 'user/viewnews.html', {"snews":snews, "cat":cat, "categorys":categorys})


####################################################

def contact(request):
    categorys = category.objects.all().filter().order_by('-id')
    if request.method=="POST":
        a = request.POST.get("name")
        b = request.POST.get("number")
        c = request.POST.get("email")
        d = request.POST.get("message")
        contactus(Name=a, Number=b, Email=c, Message=d).save()
        return HttpResponse("<script>alert('Message Send Successfully'); location.href='/index/'</script>")
    return render(request, 'user/contact.html', {"categorys":categorys})


############################################################################

def feedback(request):
    categorys = category.objects.all().filter().order_by('-id')
    if request.method=="POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        feedbackus(name=name, image=image, email=email, feedback=feedback).save()
        return HttpResponse("<script>alert('Feedback Send Successfully'); location.href='/feedback/'</script>")
    feed = feedbackus.objects.all().order_by('-id')
    return render(request, 'user/feedback.html', {"feed":feed, "categorys":categorys})

############################################################################

def logout(request):
    if request.session.get('userid'):
        del request.session['userid']
        return HttpResponse("<script>alert('You are signed out..'); location.href='/index/'</script>")
    else:
        return HttpResponse("<script>alert('You are allready signed out.. Please Sign In First..'); location.href='/index/'</script>")
      


##################################################################

def register(request):
    categorys = category.objects.all().filter().order_by('-id')
    if request.method=="POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        password = request.POST.get("password")
        image = request.FILES.get("image")
        email = request.POST.get("email")
        address = request.POST.get("address")

        num = signup.objects.all().filter(email=email).count()                # Checking Email in User Register Table
        num2 = signup_reporter.objects.all().filter(email=email).count()      # Checking Email In Reporter Register Table

        if num==0 and num2==0:
            signup(name=name, number=number, password=password, image=image, email=email, address=address).save()
            return HttpResponse("<script>alert('Registered Successfully'); location.href='/index/'</script>")
        else:
            return HttpResponse("<script>alert('Email is Allready Registered'); location.href='/index/'</script>")
    return render(request, 'user/register.html', {"categorys":categorys})

##################################################################


def profile(request):
    categorys = category.objects.all().filter().order_by('-id')
    user = request.session.get('userid')
    delete = request.GET.get('del')
    data=""
    if user:
        data = signup.objects.all().filter(email=user)             # user table
        data2 = signup_reporter.objects.all().filter(email=user)    # Admin table 
        
        # User Profile Page
        if data:
            if request.method=="POST":
                name = request.POST.get('name')
                image = request.FILES.get('image')
                number = request.POST.get('number')
                password = request.POST.get('password')
                address = request.POST.get('address')
                signup(name=name, number=number, password=password, image=image, email=user, address=address).save()
                return HttpResponse("<script>alert('Profile Update Successfully'); location.href='/profile/'</script>")
            return render(request, 'user/profile.html', {"prodata":data, "categorys":categorys})
        
        # Admin Profile Page
        elif data2:
            if request.method=="POST":
                a = request.POST.get('newsreport')
                b = request.POST.get('newscate')
                c = request.FILES.get('image')
                d = request.POST.get('newstitle')
                e = request.POST.get('newsdec')
                mynews(newsreporter=a, newscategory=b, newsimage=c, newstitle=d, newsdec=e).save()
                return HttpResponse("<script>alert('News Created Successfully'); location.href='/profile/'</script>")
            if delete is not None:
                mynews.objects.all().filter(id=delete).delete()
                return HttpResponse("<script>alert('Deleted');location.href='/profile/'</script>")
            
            newss = mynews.objects.all().filter(newsreporter=user).order_by('-id')
            return render(request, 'user/reporter_profile.html', {"prodata2":data2, "d":newss, "categorys":categorys})
    else:
        return HttpResponse("<script>alert('You have to login first');location.href='/index/'</script>")



##################################################################

def blog(request):
    categorys = category.objects.all().filter().order_by('-id')
    if request.method=="POST":
        a = request.POST.get("name")
        b = request.POST.get("email")
        c = request.FILES.get("image")
        d = request.POST.get("data")
        ourblog(Name=a, Email=b, Image=c, Data=d).save()
        return HttpResponse("<script>alert('Blog Created Successfully'); location.href='/blog/'</script>")
    blogdata = ourblog.objects.all().order_by('-id')
    return render(request, 'user/blog.html', {"blogdata":blogdata, "categorys":categorys})

##################################################################

def shownews(request):
    categorys = category.objects.all().filter().order_by('-id')
    cid = request.GET.get('news')
    if cid:
        title = category.objects.all().filter(id=cid)
        snews = mynews.objects.all().filter(newscategory=cid).order_by('-id')
        return render(request, 'user/shownews.html', {"snews":snews, "categorys":categorys, "title":title})
    else:
        return HttpResponse("<script>alert('Oops! Something Went Wrong'); location.href='/index/'</script>")

##################################################################

def detailnews(request):
    categorys = category.objects.all().filter().order_by('-id')
    cid = request.GET.get('news')
    if cid:
        snews = mynews.objects.all().filter(id=cid)
        return render(request, 'user/detailnews.html', {"snews":snews, "categorys":categorys})
    else:
        return HttpResponse("<script>alert('Oops! Something Went Wrong... You cant visit this page'); location.href='/index/'</script>")
    
##################################################################