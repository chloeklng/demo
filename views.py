from django.shortcuts import render
from django.http import HttpResponse
from .models import JD, CV
from .forms import DocumentForm

def home(request):
    return render(request, 'home.html')

def matching_candidate(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newfile = JD(file=request.FILES['file'])
            newfile.save()
            message = "Your matching is in progress!"
        else:
            message = "Form is not valid. Please check your inputs."
    else:
        form = DocumentForm()
        message = "Please upload a document."

    context = {'message': message, 'form': form}
    return render(request, 'matching_candidate.html', context)

def matching_job(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newfile = CV(file=request.FILES['file'])
            newfile.save()
            message = "Your matching is in progress!"
        else:
            message = "Form is not valid. Please check your inputs."
    else:
        form = DocumentForm()
        message = "Please upload a document."

    context = {'message': message, 'form': form}
    return render(request, 'matching_job.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')