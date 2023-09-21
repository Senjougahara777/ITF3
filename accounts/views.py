from django.shortcuts import render
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView
from django.contrib import messages
from .models import User
from .forms import SignupForm,LoginForm
from table1.models import BasicForm
from table2.models import BasicInfo
from table3.models import TNA
from table6.models import DTPA
from table4.models import TTPD
from table5.models import STP
from table7.models import STP2
from table8.models import UTP
from table9.models import NDTP
from table10.models import Section
 
from .decorators import HOT_required,AreaManager_required,CDN_required
# Create your views here.
def registerPage(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('accounts:profile',user_id = request.user.id)
        else:
            return redirect('accounts:error')

    return render(request, 'accounts/pages-register.html', {'form': form})

class view404(TemplateView):
    template_name = "accounts/pages-error-404.html"


def logout_user(request):
    logout(request)
    return redirect('accounts:login')

def loginPage(request):
    form = LoginForm()
    if request.user.is_authenticated:
        return redirect('accounts:profile',user_id = request.user.id)

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            user_id = user.id
            return redirect('accounts:profile',user_id = user_id)
        else:
            messages.error(request, 'Username OR password does not exit')

    return render(request, 'accounts/pages-login.html', context={'form': form})

def landingPageView(request,pk):
    page = "landing"
    user = User.objects.get(id=pk)
    basic_forms = user.basicform.all()
    dtpa = DTPA.objects.get(user = request.user)
    context = {
        'basic_forms':basic_forms,
        'user':user,
        'dtpa':dtpa,
        'page':page,
    }
    return render(request,'pages-blank.html',context)

def StatisticsView(request,pk):
    page = "Statistics"
    user = User.objects.get(id=pk)
    dtpa = DTPA.objects.get(user = request.user)
    context = {
        'user':user,
        'dtpa':dtpa,
        'page':page,
    }
    return render(request,'accounts/statistics.html',context)


def ProfileView(request,user_id):
    page = "profile"
    user = User.objects.get(id=user_id)
    basic_forms = user.basicform.all()
    basic_info = user.basicinfo.all()
    tna = user.tna.all()
    ttpd = user.ttpd.all()
    stp = user.stp.all()
    stp2 = user.stp2.all()
    ndtp =user.ndtp.all()
    dtpa = user.dtpa.all()
    section = user.section.all()
    utp = user.utp.all()

    context = {
        'page':page,
        'user':user,
        'basic_forms':basic_forms,
        'basic_info':basic_info,
        'tna':tna,
        'ttpd':ttpd,
        'stp':stp,
        'stp2':stp2,
        'dtpa':dtpa,
        'ndtp':ndtp,
        'dtpa':dtpa,
        'section':section,
        'utp':utp
    }
    return render(request,"accounts/profile.html",context)

@AreaManager_required
def Area_manager_profile_view(request):
    page = "Area Manager"
    user = User.objects.all()
    basic_forms = BasicForm.objects.all()
    basic_info = BasicInfo.objects.all()
    tna = TNA.objects.all()
    ttpd = TTPD.objects.all()
    stp = STP.objects.all()
    stp2 = STP2.objects.all()
    ndtp =NDTP.objects.all()
    dtpa = DTPA.objects.all()
    section = Section.objects.all()
    utp = UTP.objects.all()

    context = {
        'page':page,
        'user':user,
        'basic_forms':basic_forms,
        'basic_info':basic_info,
        'tna':tna,
        'ttpd':ttpd,
        'stp':stp,
        'stp2':stp2,
        'dtpa':dtpa,
        'ndtp':ndtp,
        'dtpa':dtpa,
        'section':section,
        'utp':utp
    }
    return render(request,'accounts/area_manager.html',context)

@CDN_required
def CDN_profile_view(request):
    page = "CPD"
    user = User.objects.all()
    basic_forms = BasicForm.objects.all()
    basic_info = BasicInfo.objects.all()
    tna = TNA.objects.all()
    ttpd = TTPD.objects.all()
    stp = STP.objects.all()
    stp2 = STP2.objects.all()
    ndtp =NDTP.objects.all()
    dtpa = DTPA.objects.all()
    section = Section.objects.all()
    utp = UTP.objects.all()

    context = {
        'page':page,
        'user':user,
        'basic_forms':basic_forms,
        'basic_info':basic_info,
        'tna':tna,
        'ttpd':ttpd,
        'stp':stp,
        'stp2':stp2,
        'dtpa':dtpa,
        'ndtp':ndtp,
        'dtpa':dtpa,
        'section':section,
        'utp':utp
    }
    return render(request,'accounts/CDN.html',context)

@HOT_required
def HOT_profile_view(request):
    page = "HOT"
    user = User.objects.all()
    basic_forms = BasicForm.objects.all()
    basic_info = BasicInfo.objects.all()
    tna = TNA.objects.all()
    ttpd = TTPD.objects.all()
    stp = STP.objects.all()
    stp2 = STP2.objects.all()
    ndtp =NDTP.objects.all()
    dtpa = DTPA.objects.all()
    section = Section.objects.all()
    utp = UTP.objects.all()

    context = {
        'page':page,
        'user':user,
        'basic_forms':basic_forms,
        'basic_info':basic_info,
        'tna':tna,
        'ttpd':ttpd,
        'stp':stp,
        'stp2':stp2,
        'dtpa':dtpa,
        'ndtp':ndtp,
        'dtpa':dtpa,
        'section':section,
        'utp':utp
    }
    return render(request,'accounts/HOT.html',context)


class HelpView(TemplateView):
    template_name = "accounts/help.html"

class ContactView(TemplateView):
    template_name = "accounts/contacts.html"

def verification(request):
    return render(request,'accounts/verification',{})