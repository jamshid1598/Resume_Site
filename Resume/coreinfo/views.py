from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.


from .models import (
    UserInfo,
)
from .forms import  (
    UserInfoForm,
    UserInfoModelForm,
    UserInfoFormSet,
)


def home(request, *args, **kwargs):
    object_list = UserInfo.objects.all()
    return render(
        request=request,
        template_name='coreinfo/index.html',
        context={'object_list' : object_list}
    )

print(datetime.now())

def update(request, id=None):
    obj  = UserInfo.objects.get(id=id)
    form = UserInfoModelForm(instance=obj)
    if request.method == 'POST':
        form = UserInfoModelForm(request.POST, request.FILES, instance=obj) # binding data to the form
        if form.is_valid():
            form.save()
            form = UserInfoModelForm()
            return redirect('Home:main-home')
        form = UserInfoModelForm(instance=obj)
    return render(
        request       = request, 
        template_name = 'coreinfo/update-cv.html', 
        context       = { 'form': form }
    )

def create_multiple_cv(request, *args, **kwargs):
    formset = UserInfoFormSet()
    obj= UserInfo.objects.get(id=1)
    print(type(obj))
    if request.method == "POST":
        formset = UserInfoFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return get_success_url()
    return render(
        request=request,template_name='coreinfo/update-cv.html', context={'formsets' : formset}
    )