from django.contrib.admin.decorators import register
from django.shortcuts import render
from django.views import View

from .models import Profile

# Create your views here.
def index(request):
    return render(request, 'profile.html')

class IndexView(View):
    def get(self, request):
        name = "Jitti Sarai",
        birth = "2 Dec. 1996",
        age = "25",
        bachelor = "Computer Engineering",
        studied = "Uttaradit Rajabhat University",
        work = "ODDS",
        position = "Developer",
        return render(
            request,
            'index.html',
            {
                "name" : name,
                "birth" : birth,
                "age" : age,
                "bachelor" : bachelor,
                "studied" : studied,
                "work" : work,
                "position" : position,
            }
        )

    def post(self, request):
        print(request.POST)
        print(request.POST.get("email"))

        forms = SubscriberForm(request.POST)
        if forms.is_valid():
            print(forms.cleaned_data)
            print(forms.cleaned_data.get("email"))

            Profile = Profile.objects.get(id=1)
            name = "Jitti Sarai",
            return render(
                request,
                'index.html',
                {
                    "name" : name,
                    "Profile" : Profile,
                }
            ),
        return render(request, "index.html")