
from django.shortcuts import render, redirect, get_object_or_404
from .models import About
from django.views import View
from .forms import AboutViewForm
# Create your views here.


def home_page(request):
    return render(request, 'home.html')


class AboutView(View):
    def get(self, request):
        about = About.objects.all()
        context = {
            'abouts': about
        }
        return render(request, 'about.html', context=context)


class AboutUpdateView(View):
    def get(self, request):
        about_instance = get_object_or_404(About, user=request.user)
        about_update_form = AboutViewForm(instance=about_instance)
        context = {
            'about_update_form': about_update_form
        }
        return render(request, 'about_update.html', context=context)

    def post(self, request):
        about_instance = get_object_or_404(About, user=request.user)
        update_form = AboutViewForm(request.POST, request.FILES, instance=about_instance)
        if update_form.is_valid():
            update_form.save()
            return redirect('home:about')
        else:
            context = {
                'about_update_form': update_form
            }
            return render(request, 'about_update.html', context=context)