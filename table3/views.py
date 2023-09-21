# Create your views here.
from django.shortcuts import render,reverse,redirect
from django.views import generic
from .models import TNA
from .forms import TnaForm
from accounts.models import User
# Create your views here.
def TnaView(request):
    template_name = 'table3/sectionA.html'
    page = "TNA"
    
    if request.method == 'POST':
        form = TnaForm(request.POST)
        if form.is_valid():
            # Create a BasicForm instance and associate it with the logged-in user
            basic_form = form.save(commit=False)  # Create an unsaved instance
            basic_form.user = request.user  # Set the user field
            basic_form.save()  # Save the instance with the user field set

            return redirect('table4:form-view')  # Redirect to a success page or any other desired URL
    else:
        form = TnaForm()

    return render(request, template_name, {'form': form, 'page': page})

def form_list(request):
    tna = TNA.objects.all()
    context = {
        "tna":tna
    }
    return render(request,"table3/formList.html",context)

def form_detail(request,pk):
    page = "tna form"
    tna = TNA.objects.get(id = pk)
    context = {
        "tna":tna,
        "page":page
    }
    return render(request,"table3/formDetail.html",context)


def form_update(request,pk):
    page = "TNA(update)"
    user = User.objects.get(id = pk)
    tna = TNA.objects.get(id = pk)
    if request.method == 'POST':
        form = TnaForm(request.POST, request.FILES, instance=tna)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile',user_id = user.id )  # Redirect to the list view after successfully updating the CustomAbout object
    else:
        form = TnaForm(instance=tna)

    context = {'form':form,'page':page,'tna ':tna}
    return render(request,'table3/formUpdate.html',context)
