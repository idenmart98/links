from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LinkForm
from .models import Links
from .utils import gen_link

# Create your views here.


def cut_link(request):
    form = LinkForm
    link = False
    if request.method == 'POST':
        if not Links.objects.filter(old_link=request.POST['link']):
            Links.objects.create(
                old_link=request.POST['link'],
                new_link=gen_link())
    if Links.objects.filter(old_link=request.POST.get('link', False)):
        link = Links.objects.get(old_link=request.POST.get('link', False))
    return render(request, 'index.html', context={'link': link, 'form': form})


def all_link(request):
    links = Links.objects.all().order_by('-id')
    return render(request, 'index.html', context={'links': links})


def redirect_old(request, link_id):
    old_url = Links.objects.get(id=link_id).old_link
    return HttpResponseRedirect(old_url)