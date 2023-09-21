from django.shortcuts import render,redirect,reverse
from django.views import generic
from .forms import FormBasicForm
from .models import BasicForm
from accounts.models import User
from accounts.decorators import HOT_required,AreaManager_required,CDN_required

# Create your views here.
def BasicFormView(request):
    template_name = 'table1/sectionA.html'
    page = "basic form"
    
    if request.method == 'POST':
        form = FormBasicForm(request.POST)
        if form.is_valid():
            # Create a BasicForm instance and associate it with the logged-in user
            basic_form = form.save(commit=False)  # Create an unsaved instance
            basic_form.user = request.user  # Set the user field
            basic_form.save()  # Save the instance with the user field set

            return redirect('table2:form-view')  # Redirect to a success page or any other desired URL
    else:
        form = FormBasicForm()

    return render(request, template_name, {'form': form, 'page': page})

def form_list(request):
    basic_forms = BasicForm.objects.all()
    context = {
        "basic_forms":basic_forms
    }
    return render(request,"table1/formList.html",context)

def form_detail(request,pk):
    page = "basic form"
    basic_forms = BasicForm.objects.get(id = pk)
    context = {
        "basic_forms":basic_forms,
        "page":page
    }
    
    return render(request,"table1/formDetail.html",context)


def form_update(request,pk):
    page = "basicform(update)"
    user = User.objects.get(id = pk)
    basic_forms = BasicForm.objects.get(id = pk)
    if request.method == 'POST':
        form = FormBasicForm(request.POST, request.FILES, instance=basic_forms)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile',user_id = user.id )  # Redirect to the list view after successfully updating the CustomAbout object
    else:
        form = FormBasicForm(instance=basic_forms)

    context = {'form':form,'page':page,'basic_forms ':basic_forms}
    return render(request,'table1/formUpdate.html',context)


