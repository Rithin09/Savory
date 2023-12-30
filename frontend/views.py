from django.shortcuts import render,redirect
from delivery.models import catdb,productdb,bookingdb,Eventdb
from frontend.models import contactdb,registerdb,cartdb
from django.contrib import messages
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from Doorsteps import settings
from django.core.mail import send_mail

def homepg(req):
    data=catdb.objects.all()
    pr = productdb.objects.all()
    ev=Eventdb.objects.all()
    return render(req,"home.html",{'data':data, 'pr':pr, 'ev':ev})

def product(re):
    pr=productdb.objects.all()
    return render(re,"productpg.html",{'pr':pr})

def singledish(req,proid):
    data=productdb.objects.get(id=proid)
    return render(req,"singledish.html",{'data':data})

def dishcategory(req,cat_name):
    cat=productdb.objects.filter(CategoryName=cat_name)
    return render(req,"dishcat.html",{'cat':cat})

def about(re):
    ev = Eventdb.objects.all()
    return render(re,"about.html",{'ev':ev})

def contact(req):
    return render(req,"contact.html")
def service(re):
    return render(re,"servicepg.html")

def insertcontact(re):
    if re.method=="POST":
        a=re.POST.get('name')
        b=re.POST.get('email')
        c=re.POST.get('message')
        obj=contactdb(Name=a,Email=b,Message=c)
        obj.save()
        return redirect(homepg)

def registration(re):
    return render(re,"registerpg.html")

def registerdata(re):
    if re.method=="POST":
        a=re.POST.get('name')
        b=re.POST.get('email')
        c=re.POST.get('pswd')
        if registerdb.objects.filter(Email=b).exists():
            # Name is already taken, display an alert or handle it as needed
            alert_message = "Email Id exists. Please choose a different Email Id."
            return render(re, 'registerpg.html', {'alert_message': alert_message})
        else:
            obj=registerdb(Name=a,Email=b,Password=c)
            obj.save()
            return redirect(registration)

def userlogin(req):
    if req.method=="POST":
        un=req.POST.get('uname')
        psd=req.POST.get('upsd')
        if registerdb.objects.filter(Name=un,Password=psd).exists():
            req.session['Name']=un
            req.session['Password']=psd
            messages.success(req,"Login")
            return redirect(homepg)
        else:
            messages.warning(req,"No account found")
            return redirect(registration)
    return redirect(registration)

def logoutuser(req):
    del req.session['Name']
    del req.session['Password']
    return redirect(registration)




def insertcart(re):
    if re.method == "POST":
        a=re.POST.get('quantity')
        b=re.POST.get('dishname')
        c=re.POST.get('descp')
        d=re.POST.get('price')
        e=re.POST.get('totprice')
        f=re.POST.get('uname')
        obj=cartdb(Quantity=a,Dishname=b,Description=c,Price=d,TotalPrice=e,Username=f)
        obj.save()
        return redirect(cartpg)
def cartpg(re):
    if 'Name' not in re.session:
        # Redirect the user to the login page
        return redirect(userlogin)
    data=cartdb.objects.filter(Username=re.session['Name'])
    totalprice=0
    for s in data:
            totalprice=totalprice+s.TotalPrice
    return render(re,"cartpage.html",{'data':data,'totalprice':totalprice})

def deletedish(re,proid):
    pro=cartdb.objects.filter(id=proid)
    pro.delete()
    return redirect(cartpg)

def checkoutorder(re):
    data=cartdb.objects.filter(Username=re.session['Name'])
    totalprice=0
    for s in data:
            totalprice=totalprice+s.TotalPrice
    return render(re,"checkoutpage.html",{'data':data,'totalprice':totalprice})

def bookingevent(re):
    return render(re,"bookingpg.html")

def bookingdata(re):
    if re.method == "POST":
        a=re.POST.get('place')
        c=re.POST.get('event')
        d=re.POST.get('peoples')
        e=re.POST.get('mob')
        h=re.POST.get('name')
        f=re.POST.get('date')
        g=re.POST.get('mail')
        obj=bookingdb(Country=a,Events=c,Palace=d,Contact=e,Date=f,Email=g,Name=h)
        obj.save()
        messages.success(re,"Event Confirmed")
        subject = f"Booking Confirmed for your {obj.Events} Event"
        message = f"Hello {obj.Name},\n\nThank you for booking Savory Seasons for your dream event. This is a confirmation email!\n\nEvent Details:\nEvent Name: {obj.Events}\nEvent Date: {obj.Date}\n\nIf you have any further questions or require assistance, feel free to contact us.\n\nBest Regards,\nThe Savory Seasons Team"
        from_mail= settings.EMAIL_HOST_USER
        to_list= [obj.Email]
        send_mail(subject,message,from_mail,to_list,fail_silently=True)
        return redirect(homepg)
    
def confirmorder(re):
    data = cartdb.objects.filter(Username=re.session['Name'])
    totalprice = 0
    for s in data:
        totalprice = totalprice + s.TotalPrice
    return render(re,"paypage.html",{'data':data,'totalprice':totalprice})

def dish_search(request):
    query = request.GET.get('query')
    results = []

    if query:
        results = productdb.objects.filter(
            Q(ProductName__icontains=query) | Q(CategoryName__icontains=query)
        )

    return render(request, 'searchdish.html', {'query': query, 'results': results})

def eventspg(re):
    data=Eventdb.objects.all()
    return render(re,"eventspage.html",{'data':data})

def endpage(re):
    return render(re,"thanks.html")

def deletealldish(re):
    pro = cartdb.objects.filter(Username=re.session['Name'])
    pro.delete()
    return redirect(homepg)