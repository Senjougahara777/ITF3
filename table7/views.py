from django.shortcuts import render,redirect,reverse
from django.views import generic
from .forms import Stp2Form
from .models import STP2
from accounts.models import User

# Create your views here.
def Stp2View(request):
    template_name = 'table6/sectionA.html'
    page = "STP2"
    
    if request.method == 'POST':
        form = Stp2Form(request.POST)
        if form.is_valid():
            # Create a BasicForm instance and associate it with the logged-in user
            basic_form = form.save(commit=False)  # Create an unsaved instance
            basic_form.user = request.user  # Set the user field
            basic_form.save()  # Save the instance with the user field set

            return redirect('table7:form-view')  # Redirect to a success page or any other desired URL
    else:
        form = Stp2Form()

    return render(request, template_name, {'form': form, 'page': page})

def form_list(request):
    stp2 = STP2.objects.all()
    context = {
        "stp2":stp2
    }
    return render(request,"table7/formList.html",context)

def form_detail(request,pk):
    page = "stp2"
    stp2 = STP2.objects.get(id = pk)
    context = {
        "stp2":stp2,
        "page":page
    }
    
    return render(request,"table7/formDetail.html",context)

def form_update(request,pk):
    page = "STP2(update)"
    user = User.objects.get(id = pk)
    stp2 = STP2.objects.get(id = pk)
    if request.method == 'POST':
        form = Stp2Form(request.POST, request.FILES, instance=stp2)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile',user_id = user.id )  # Redirect to the list view after successfully updating the CustomAbout object
    else:
        form = Stp2Form(instance=stp2)

    context = {'form':form,'page':page,'stp2 ':stp2}
    return render(request,'table7/formUpdate.html',context)
