from django.shortcuts import render
from data.models import Data
from .forms import DataForm
from django.utils import timezone
from django.shortcuts import redirect
# Create your views here.

def post_data(request):
    comments = Data.objects.all().order_by('first_name')
    return render(request, 'data/post_data.html',{'comments':comments})

def delete_data(request):
    Data.objects.all().delete()
    return redirect('post_data')

def new_data(request):
    if request.method == "POST":
        form= DataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now()
            post.save()
            return redirect('post_data')
    else:
        form = DataForm()
    return render(request, 'data/post_new.html',{'form':form})
