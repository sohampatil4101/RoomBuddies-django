from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.core.mail import send_mail
from django.conf import settings
import random



def home(request):
    items = list(Vacantroom.objects.all())
    so = random.sample(items, 4)

    abc = list(Vacanthouse.objects.all())
    ab = random.sample(abc, 4)

    xyz = list(Sellroom.objects.all())
    cd = random.sample(xyz, 4)
    context = {'username': request.session.get('username'), 'so': so, 'ab':ab, 'cd': cd }
    return render(request,'./app/home.html', context)


def done(request, obj1, obj2, obj3):
    ownername = obj1
    buyername = request.session.get('username')
    us = Register.objects.filter(username = request.session.get('username'))
    for i in us:
        gender = i.gender 
        qualification = i.qualification 
        email = i.email 
    rent = obj2
    address = obj3
    abc = Req(ownername = ownername, buyername = buyername, rent = rent, address = address, gender = gender, qualification = qualification, email = email)
    abc.save()
    context = {'username': request.session.get('username')}
    return render(request,'./app/done.html', context)

def login(request):
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username= username, password = password)
        request.session['username'] = username

        if (Register.objects.filter(username=username, password = password).exists()):
            context = {'username': request.session.get('username')}
            return redirect("/",context)
            context = {'successs':False}

        else:
            context= {'success':True, 'soham':"Please enter correct username or password!!!"}
            return render(request, './app/login.html', context)



    return render(request, './app/login.html', context)




def register(request):
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        gender = request.POST['gender']
        lastname = request.POST['lastname']
        qualification = request.POST['qualification']
        birthdate = request.POST['birthdate']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        filee = request.FILES.get('file')

        if ( len(username) and len(firstname) and len(lastname) and len(birthdate) and len(email) and len(phone) and len(password1) and len(password2)) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}

        elif (password1 != password2 ):
            context={'successs':True,'mssg':"Both passwords are not same!!"}

        elif (Register.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
    
        elif (Roommate.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
    
        
        elif ( Register.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}

        elif ( Roommate.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}



        else:
            ins = Register(username = username, gender = gender, firstname =firstname, lastname = lastname, email = email, birthdate = birthdate, phone = phone, file =filee)
            ins.save()
            context = {'success': True, 'mssg': "Account created Succcessfully"}
            try:
                send_mail(
                'Conguratulation!!!',
                'You have been successfully registered to our website',
                'settings.EMAIL_HOST_USER',
                [email], #here it can be also a list of emails
                fail_silently = False)
            except:
                pass
            return render(request,'./app/register.html', context)
            
    return render(request,'./app/register.html', context)

def about(request):
    context = {'username': request.session.get('username') }
    return render(request,'./app/about.html', context)


def contact(request):
    context = {'username': request.session.get('username')}
    return render(request,'./app/contact.html', context)
    
def roommate(request, obj1, obj2):
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        username = request.session.get('username')
        state = request.POST['state']
        city = request.POST['city']
        area = request.POST['area']
        room_mate_present = obj1
        room_mate_require = obj2
        rent = request.POST['rent']
        file = request.FILES.get('file')
        lastdate = request.POST['lastdate']
        address = state + " " + city + " " + area



        if ( len(username) and len(address) and len(rent) and len(lastdate)) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}

        else:
            ins = Vacantroom(username = username,address = address, state =state, city = city, area = area, room_mate_present = room_mate_present, room_mate_require = room_mate_require, rent =rent, file = file, lastdate = lastdate)
            ins.save()
            context = {'success': True, 'mssg':"Room added"}
            return redirect("/")
            
    return render(request,'./app/roommate.html', context)


def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return redirect('/')


def more(request, obj1, obj2, obj3):
    so = Vacantroom.objects.filter(username = obj1, address = obj2, rent = obj3 )
    ab = Vacanthouse.objects.filter(username = obj1, address = obj2, rent = obj3 )
    cd = Sellroom.objects.filter(username = obj1, address = obj2, sellprice = obj3 )
    context = {'so': so, 'ab': ab, 'cd': cd, 'username': request.session.get('username')}
    return render(request, './app/more.html', context)    


def vacanthouse(request):
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        username = request.session.get('username')
        state = request.POST['state']
        city = request.POST['city']
        area = request.POST['area']
        rent = request.POST['rent']
        file = request.FILES.get('file')
        lastdate = request.POST['lastdate']
        address = state +" "+ city +" "+ area

        if (len(address) and len(rent) and len(lastdate)) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}
        else:
            inss = Vacanthouse(username = username,address = address, state =state, city = city, area = area, rent =rent, file = file, lastdate = lastdate)
            inss.save()
            context = {'success': True, 'mssg': "Room Added successfully!!!"}
            return render(request,'./app/vacanthouse.html', context)
            
    return render(request,'./app/vacanthouse.html', context)





def sellroom(request):
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        username = request.session.get('username')
        state = request.POST['state']
        city = request.POST['city']
        area = request.POST['area']
        sellprice = request.POST['sellprice']
        file = request.FILES.get('file')
        lastdate = request.POST['lastdate']
        address = state +" "+ city +" "+ area

        if ( len(username) and len(address) and len(sellprice) and len(lastdate)) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}

        else:
            ins = Sellroom(username = username,address = address, state =state, city = city, area = area, sellprice =sellprice, file = file, lastdate = lastdate)
            ins.save()
            context = {'success': True, 'mssg': "Room added successfully!!!"}
            return render(request,'./app/sellroom.html', context)
            
    return render(request,'./app/sellroom.html', context)


def search(request):
    context = {'nopage': False}
    search = request.GET['search']
    so = Vacanthouse.objects.filter(area__icontains = search)
    ab = Vacantroom.objects.filter(area__icontains = search)
    cd = Sellroom.objects.filter(area__icontains = search)
    if(so or ab or cd):
        context = {'so': so, 'ab':ab, 'cd': cd}
        return render(request, './app/search.html', context)
    else:
        context = {'so': so, 'ab':ab, 'cd': cd, 'nopage': True}
        return render(request, './app/search.html', context)

    context = {'so': so, 'ab':ab, 'cd': cd}
    return render(request, './app/search.html', context)


def final(request):
    if request.method == "POST":
        room_mate_present = request.POST['room_mate_present']
        room_mate_require = request.POST['room_mate_require']
        context = {'i': int(room_mate_present), 'j': int(room_mate_require), 'p':range(0,int(room_mate_present)), 'q':range(0,int(room_mate_require))}
        return render(request,'./app/roommate.html', context)
    return render(request, './app/final.html')

def profile(request):
    so = Req.objects.filter(ownername = request.session.get('username'))
    context = {'so': so}
    return render(request, './app/profile.html', context)

def accept(request, obj1, obj2, obj3, obj4):
    try:
        send_mail(
        'Congratulations!!!',
        'sorry ur profile is rejected by volo mart due to some documents issued by you are incorrect...',
        'settings.EMAIL_HOST_USER',
        [obj4], #here it can be also a list of emails
        fail_silently = False)
    except:
        pass
    so = Req.objects.filter(buyername = obj1, address = obj2, rent = obj3)
    so.delete()
    return redirect('/profile')



def delete(request, obj1, obj2, obj3, obj4):
    try:
        send_mail(
        'Sorry!!!',
        'sorry ur profile is rejected by volo mart due to some documents issued by you are incorrect...',
        'settings.EMAIL_HOST_USER',
        [obj4], #here it can be also a list of emails
        fail_silently = False)
    except:
        pass
            
    so = Req.objects.filter(buyername = obj1, address = obj2, rent = obj3)
    so.delete()
    return redirect('/profile')