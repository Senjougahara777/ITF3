from django.shortcuts import render,reverse,redirect
from django.views import generic
from .models import BasicInfo
from .forms import BasicInfoForm
from accounts.models import User
# Create your views here.
def BasicInfoView(request):
    template_name = 'table2/sectionA.html'
    page = "basic info"
    
    if request.method == 'POST':
        form = BasicInfoForm(request.POST)
        if form.is_valid():
            # Create a BasicForm instance and associate it with the logged-in user
            basic_form = form.save(commit=False)  # Create an unsaved instance
            basic_form.user = request.user  # Set the user field
            basic_form.save()  # Save the instance with the user field set

            return redirect('table3:form-view')  # Redirect to a success page or any other desired URL
    else:
        form = BasicInfoForm()

    return render(request, template_name, {'form': form, 'page': page})




def form_list(request):
    basic_info = BasicInfo.objects.all()
    context = {
        "basic_info":basic_info
    }
    return render(request,"table2/formList.html",context)

def form_detail(request,pk):
    page = "basic info"
    basic_info = BasicInfo.objects.get(id = pk)
    context = {
        "basic_info":basic_info,
        "page":page
    }
    
    return render(request,"table2/formDetail.html",context)

def form_update(request,pk):
    page = "basicInfo(update)"
    user = User.objects.get(id = pk)
    basic_info = BasicInfo.objects.get(id = pk)
    if request.method == 'POST':
        form = BasicInfoForm(request.POST, request.FILES, instance=basic_info)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile',user_id = user.id )  # Redirect to the list view after successfully updating the CustomAbout object
    else:
        form = BasicInfoForm(instance=basic_info)

    context = {'form':form,'page':page,'basic_info ':basic_info}
    return render(request,'table2/formUpdate.html',context)
