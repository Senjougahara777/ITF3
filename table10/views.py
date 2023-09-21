from django.shortcuts import render,redirect,reverse
from django.views import generic
from .forms import SectionForm
from .models import Section
from accounts.models import User

# Create your views here.
def SectionView(request):
    template_name = 'table10/sectionA.html'
    page = "Section"
    
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            # Create a BasicForm instance and associate it with the logged-in user
            basic_form = form.save(commit=False)  # Create an unsaved instance
            basic_form.user = request.user  # Set the user field
            basic_form.save()  # Save the instance with the user field set

            return redirect('table10:form-view')  # Redirect to a success page or any other desired URL
    else:
        form = SectionForm()

    return render(request, template_name, {'form': form, 'page': page})

def form_list(request):
    section = Section.objects.all()
    context = {
        "section":section
    }
    return render(request,"table10/formList.html",context)

def form_detail(request,pk):
    page = "section"
    section = Section.objects.get(id = pk)
    context = {
        "section":section,
        "page":page
    }
    
    return render(request,"table10/formDetail.html",context)

def form_update(request,pk):
    page = "Section(update)"
    user = User.objects.get(id = pk)
    section = Section.objects.get(id = pk)
    if request.method == 'POST':
        form = SectionForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile',user_id = user.id )  # Redirect to the list view after successfully updating the CustomAbout object
    else:
        form = SectionForm(instance=section)

    context = {'form':form,'page':page,'section ':section}
    return render(request,'table10/formUpdate.html',context)
