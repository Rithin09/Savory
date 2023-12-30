from django.shortcuts import render, redirect
from delivery.models import catdb, productdb,Eventdb,bookingdb
from frontend.models import contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages


# Create your views here.
def indexpage(re):
    return render(re, "index.html")


def category(re):
    return render(re, "addcategory.html")


def insert(re):
    if re.method == "POST":
        a = re.POST.get('cname')
        b = re.POST.get('cdescp')
        c = re.FILES['cimg']
        obj = catdb(CategoryName=a, Description=b, Image=c)
        obj.save()
        messages.success(re,"Category saved")
        return redirect(category)


def catdisplay(re):
    data = catdb.objects.all()
    return render(re, "categorydisplay.html", {'data': data})


def editcat(re, dataid):
    edit = catdb.objects.get(id=dataid)
    return render(re, "editcategory.html", {'edit': edit})


def updatecat(re, dataid):
    if re.method == "POST":
        a = re.POST.get('cname')
        b = re.POST.get('cdescp')
        try:
            img = re.FILES['cimg']
            fs = FileSystemStorage()
            fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = catdb.objects.get(id=dataid).Image
        catdb.objects.filter(id=dataid).update(CategoryName=a, Description=b, Image=file)
        messages.success(re,"Category Updated")
        return redirect(catdisplay)


def deletecat(req, dataid):
    data = catdb.objects.filter(id=dataid)
    data.delete()
    messages.warning(req,"Data deleted")
    return redirect(catdisplay)


def dish(r):
    cat = catdb.objects.all()
    return render(r, "addproduct.html", {'cat': cat})


def productdata(req):
    if req.method == "POST":
        a = req.POST.get('cname')
        b = req.POST.get('pname')
        c = req.POST.get('pdescp')
        d = req.POST.get('price')
        e = req.FILES['pimg']
        obj = productdb(CategoryName=a, ProductName=b, Description=c, Price=d, ProductImage=e)
        obj.save()
        messages.success(req,"Product saved")
        return redirect(dish)


def prodisplay(re):
    data = productdb.objects.all()
    return render(re, "displayproduct.html", {'data': data})


def editprod(re, dataid):
    data = productdb.objects.get(id=dataid)
    cat = catdb.objects.all()
    return render(re, "editproduct.html", {'data': data, 'cat': cat})


def update(re, dataid):
    if re.method == "POST":
        a = re.POST.get('cname')
        b = re.POST.get('pname')
        c = re.POST.get('pdescp')
        d = re.POST.get('price')
        try:
            img = re.FILES['pimg']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).ProductImage
        productdb.objects.filter(id=dataid).update(CategoryName=a, ProductName=b, Description=c, Price=d,ProductImage=file)
        messages.success(re,"Product Updated")                      
        return redirect(prodisplay)


def delete(re, dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    messages.warning(re,"Data deleted")
    return redirect(prodisplay)


def loginpage(re):
    return render(re, "loginpage.html")


def logindetails(re):
    if re.method == "POST":
        un = re.POST.get('user_name')
        psd = re.POST.get('pass_word')
        if User.objects.filter(username__contains=un).exists():
            main = authenticate(username=un, password=psd)
            if main is not None:
                login(re, main)
                re.session['username'] = un
                re.session['password'] = psd
                return redirect(indexpage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)


def logoutpage(req):
    del req.session['username']
    del req.session['password']
    return redirect(loginpage)


def displaycontact(re):
    data = contactdb.objects.all()
    return render(re, "displaycontact.html", {'data': data})


def deletecontact(re, dataid):
    cont = contactdb.objects.filter(id=dataid)
    cont.delete()
    return redirect(displaycontact)

def addeventpg(re):
    return render(re, "addevents.html")


def insertevents(re):
    if re.method=="POST":
        a=re.POST.get('ename')
        b=re.FILES['eimg']
        c=re.FILES['eimg1']
        d=re.FILES['eimg2']
        e=re.FILES['eimg3']
        f=re.FILES['eimg4']
        g=re.FILES['eimg5']
        h=re.FILES['eimg6']
        obj=Eventdb(Eventname=a,image=b,image1=c,image2=d,image3=e,image4=f,image5=g,image6=h)
        obj.save()
        return redirect(addeventpg)
def displayevent(re):
    data=Eventdb.objects.all()
    return render(re,"eventdisplay.html",{'data':data})

def editpg(re,dataid):
    edit=Eventdb.objects.get(id=dataid)
    return render(re,"editevents.html",{'edit':edit})

def updateevent(re,dataid):
    if re.method=="POST":
        a=re.POST.get('ename')
        try:
            img = re.FILES['eimg']
            fs=FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Eventdb.objects.get(id=dataid).image
        try:
            img1 = re.FILES['eimg1']
            fs=FileSystemStorage()
            file1 = fs.save(img1.name, img1)
        except MultiValueDictKeyError:
            file1 = Eventdb.objects.get(id=dataid).image1
        try:
            img2 = re.FILES['eimg2']
            fs=FileSystemStorage()
            file2 = fs.save(img2.name, img2)
        except MultiValueDictKeyError:
            file2 = Eventdb.objects.get(id=dataid).image2
        try:
            img3 = re.FILES['eimg3']
            fs=FileSystemStorage()
            file3 = fs.save(img3.name, img3)
        except MultiValueDictKeyError:
            file3 = Eventdb.objects.get(id=dataid).image3
        try:
            img4 = re.FILES['eimg4']
            fs=FileSystemStorage()
            file4 = fs.save(img4.name, img4)
        except MultiValueDictKeyError:
            file4 = Eventdb.objects.get(id=dataid).image4
        try:
            img5 = re.FILES['eimg5']
            fs=FileSystemStorage()
            file5 = fs.save(img5.name, img5)
        except MultiValueDictKeyError:
            file5 = Eventdb.objects.get(id=dataid).image5
        try:
            img6 = re.FILES['eimg6']
            fs=FileSystemStorage()
            file6 = fs.save(img6.name, img6)
        except MultiValueDictKeyError:
            file6 = Eventdb.objects.get(id=dataid).image6
        Eventdb.objects.filter(id=dataid).update(Eventname=a,
        image=file, image1=file1, image2=file2, image3=file3, image4=file4,
        image5=file5, image6=file6)
        return redirect(displayevent)

def displaybookingpg(re):
    data=bookingdb.objects.all()
    return render(re,"displaybooking.html",{'data':data})


def bookingdelete(re, dataid):
    data = bookingdb.objects.filter(id=dataid)
    data.delete()
    messages.warning(re,"Data deleted")
    return redirect(displaybookingpg)
