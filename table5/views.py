from django.shortcuts import render,redirect,reverse
from django.views import generic
from .forms import StpForm
from .models import STP
from accounts.models import User

# Create your views here.
def StpView(request):
    template_name = 'table5/sectionA.html'
    page = "STP"
    
    if request.method == 'POST':
        form = StpForm(request.POST)
        if form.is_valid():
            # Create a BasicForm instance and associate it with the logged-in user
            basic_form = form.save(commit=False)  # Create an unsaved instance
            basic_form.user = request.user  # Set the user field
            basic_form.save()  # Save the instance with the user field set

            return redirect('table6:form-view')  # Redirect to a success page or any other desired URL
    else:
        form = StpForm()

    return render(request, template_name, {'form': form, 'page': page})

def form_list(request):
    stp = STP.objects.all()
    context = {
        "stp":stp
    }
    return render(request,"table5/formList.html",context)

def form_detail(request,pk):
    page = "stp"
    stp = STP.objects.get(id = pk)
    context = {
        "stp":stp,
        "page":page
    }
    
    return render(request,"table1/formDetail.html",context)

def form_update(request,pk):
    page = "STP(update)"
    user = User.objects.get(id = pk)
    stp = STP.objects.get(id = pk)
    if request.method == 'POST':
        form = StpForm(request.POST, request.FILES, instance=stp)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile',user_id = user.id )  # Redirect to the list view after successfully updating the CustomAbout object
    else:
        form = StpForm(instance=stp)

    context = {'form':form,'page':page,'stp ':stp}
    return render(request,'table5/formUpdate.html',context)
