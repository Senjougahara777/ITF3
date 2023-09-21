# Create your views here.
from django.shortcuts import render,reverse,redirect
from django.views import generic
from .models import TTPD
from .forms import TtpdForm
from accounts.models import User
# Create your views here.
def TtpdView(request):
    template_name = 'table4/sectionA.html'
    page = "TTPD"
    
    if request.method == 'POST':
        form = TtpdForm(request.POST)
        if form.is_valid():
            # Create a BasicForm instance and associate it with the logged-in user
            basic_form = form.save(commit=False)  # Create an unsaved instance
            basic_form.user = request.user  # Set the user field
            basic_form.save()  # Save the instance with the user field set

            return redirect('table5:form-view')  # Redirect to a success page or any other desired URL
    else:
        form = TtpdForm()

    return render(request, template_name, {'form': form, 'page': page})

def form_list(request):
    ttpd = TTPD.objects.all()
    context = {
        "ttpd":ttpd
    }
    return render(request,"table4/formList.html",context)

def form_detail(request,pk):
    page = "ttpd"
    ttpd = TTPD.objects.get(id = pk)
    context = {
        "ttpd":ttpd,
        "page":page
    }
    
    return render(request,"table4/formDetail.html",context)

def form_update(request,pk):
    page = "TTPD(update)"
    user = User.objects.get(id = pk)
    ttpd = TTPD.objects.get(id = pk)
    if request.method == 'POST':
        form = TtpdForm(request.POST, request.FILES, instance=ttpd)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile',user_id = user.id )  # Redirect to the list view after successfully updating the CustomAbout object
    else:
        form = TtpdForm(instance=ttpd)

    context = {'form':form,'page':page,'ttpd ':ttpd}
    return render(request,'table4/formUpdate.html',context)
