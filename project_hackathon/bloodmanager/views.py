from django.shortcuts import render
from project_hackathon.bloodmanager.models.main import BloodAmount

def index_admin(request):

    return render(request, "bloodmanager/supply_overview.html", {

    })

def user_overview(request):

    return render(request, "bloodmanager/user_overview.html", {

    })

def supply_overview(request):
    institution = request.user.institution.first()
    amounts = BloodAmount.objects.filter(institution=institution)
    return render(request, "bloodmanager/supply_overview.html", {
        'amounts': amounts
    })

def add_donator(request):

    return render(request, "bloodmanager/add_donator.html", {

    })

def index_user(request):

    return render(request, "bloodmanager/my_donations.html", {

    })

def my_profile(request):
    return render(request, "bloodmanager/my_profile.html", {

    })
    # return render(request, "bloodmanager/donation_overview.html", {

    # })
