from django.shortcuts import render,redirect,reverse
from django.views import generic
from .forms import NdtpForm
from .models import NDTP
from accounts.models import User

# Create your views here.
def NdtpView(request):
    template_name = 'table9/sectionA.html'
    page = "NDTP"
    
    if request.method == 'POST':
        form = NdtpForm(request.POST)
        if form.is_valid():
            # Create a BasicForm instance and associate it with the logged-in user
            basic_form = form.save(commit=False)  # Create an unsaved instance
            basic_form.user = request.user  # Set the user field
            basic_form.save()  # Save the instance with the user field set

            return redirect('table10:form-view')  # Redirect to a success page or any other desired URL
    else:
        form = NdtpForm()

    return render(request, template_name, {'form': form, 'page': page})

def form_list(request):
    ndtp = NDTP.objects.all()
    context = {
        "ndtp":ndtp
    }
    return render(request,"table9/formList.html",context)

def form_detail(request,pk):
    page = "ndtp"
    ndtp = NDTP.objects.get(id = pk)
    context = {
        "ndtp":ndtp,
        "page":page
    }
    
    return render(request,"table9/formDetail.html",context)

def form_update(request,pk):
    page = "NDTP(update)"
    user = User.objects.get(id = pk)
    ndtp = NDTP.objects.get(id = pk)
    if request.method == 'POST':
        form = NdtpForm(request.POST, request.FILES, instance=ndtp)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile',user_id = user.id )  # Redirect to the list view after successfully updating the CustomAbout object
    else:
        form = NdtpForm(instance=ndtp)

    context = {'form':form,'page':page,'ndtp ':ndtp}
    return render(request,'table9/formUpdate.html',context)
