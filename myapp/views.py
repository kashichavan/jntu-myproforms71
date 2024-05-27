from django.shortcuts import render

# Create your views here.
from .models import Student
from .forms import StudentForm

def uploadImage(request):
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
        else:
            print("hello")
        return render(request,'submit.html')    
    return render(request,'form.html')

def viewdata(request):
    data=Student.objects.all()
    data={'data':data}
    return render(request,'view.html',context=data)
