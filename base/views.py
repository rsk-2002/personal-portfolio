from django.shortcuts import render
from .models import Project, Skill, Message
from .forms import MessageForm
from django.contrib import messages

# Create your views here.
def homePage(request):
    projects = Project.objects.filter(is_active=True)
    skills = Skill.objects.filter(is_active=True)

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was successfully sent.")
            return redirect('home')

    return render(request, 'base/home.html', {"projects":projects, "skills":skills})