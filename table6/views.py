from django.shortcuts import render,redirect,reverse
from django.views import generic
from .forms import DtpaForm
from .models import DTPA
from accounts.models import User

# Create your views here.
def DtpaView(request):
    template_name = 'table6/sectionA.html'
    page = "DTPA"
    
    if request.method == 'POST':
        form = DtpaForm(request.POST)
        if form.is_valid():
            # Create a BasicForm instance and associate it with the logged-in user
            basic_form = form.save(commit=False)  # Create an unsaved instance
            basic_form.user = request.user  # Set the user field
            basic_form.save()  # Save the instance with the user field set

            return redirect('table7:form-view')  # Redirect to a success page or any other desired URL
    else:
        form = DtpaForm()

    return render(request, template_name, {'form': form, 'page': page})

def form_list(request):
    dtpa = DTPA.objects.all()
    context = {
        "dtpa":dtpa
    }
    return render(request,"table6/formList.html",context)

def form_detail(request,pk):
    page = "dtpa"
    dtpa = DTPA.objects.get(id = pk)
    context = {
        "dtpa":dtpa,
        "page":page
    }
    
    return render(request,"table6/formDetail.html",context)


def form_update(request,pk):
    page = "DTPA(update)"
    user = User.objects.get(id = pk)
    dtpa = DTPA.objects.first()
    if request.method == 'POST':
        form = DtpaForm(request.POST, request.FILES, instance=dtpa)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile',user_id = user.id )  # Redirect to the list view after successfully updating the CustomAbout object
    else:
        form = DtpaForm(instance=dtpa)

    context = {'form':form,'page':page,'dtpa ':dtpa}
    return render(request,'table6/formUpdate.html',context)

def dtpa_update(request,pk):
    page = "DTPA(update)"
    user = User.objects.get(id = pk)
    dtpa = DTPA.objects.first()
    if request.method == 'POST':
        form = DtpaForm(request.POST, request.FILES, instance=dtpa)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile',user_id = user.id )  # Redirect to the list view after successfully updating the CustomAbout object
    else:
        form = DtpaForm(instance=dtpa)

    context = {'form':form,'page':page,'dtpa ':dtpa}
    return render(request,'table6/formUpdate.html',context)
