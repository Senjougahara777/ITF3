from django.shortcuts import render,redirect,reverse
from django.views import generic
from .forms import UtpForm
from .models import UTP
from accounts.models import User
# Create your views here.
def UtpView(request):
    template_name = 'table8/sectionA.html'
    page = "UTP"
    
    if request.method == 'POST':
        form = UtpForm(request.POST)
        if form.is_valid():
            # Create a BasicForm instance and associate it with the logged-in user
            basic_form = form.save(commit=False)  # Create an unsaved instance
            basic_form.user = request.user  # Set the user field
            basic_form.save()  # Save the instance with the user field set

            return redirect('table9:form-view')  # Redirect to a success page or any other desired URL
    else:
        form = UtpForm()

    return render(request, template_name, {'form': form, 'page': page})

def form_list(request):
    utp = UTP.objects.all()
    context = {
        "utp":utp
    }
    return render(request,"table8/formList.html",context)

def form_detail(request,pk):
    page = "utp"
    utp = UTP.objects.get(id = pk)
    context = {
        "utp":utp,
        "page":page
    }
    
    return render(request,"table8/formDetail.html",context)

def form_update(request,pk):
    page = "UTP(update)"
    user = User.objects.get(id = pk)
    utp = UTP.objects.get(id = pk)
    if request.method == 'POST':
        form = UtpForm(request.POST, request.FILES, instance=utp)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile',user_id = user.id )  # Redirect to the list view after successfully updating the CustomAbout object
    else:
        form = UtpForm(instance=utp)

    context = {'form':form,'page':page,'utp ':utp}
    return render(request,'table8/formUpdate.html',context)
