from django.shortcuts import render, redirect
from project_hackathon.bloodmanager.models.main import BloodAmount
from django.db.models import Max
from project_hackathon.bloodmanager.models.common import Institution, Notification


def index_admin(request):

    return render(request, "bloodmanager/supply_overview.html", {

    })

def user_overview(request):

    return render(request, "bloodmanager/user_overview.html", {

    })

def supply_overview(request):
    institution = request.user.institution.first()
    amounts = BloodAmount.objects.filter(institution=institution).order_by('amount')
    max_amount = BloodAmount.objects.filter(institution=institution).aggregate(Max('amount'))['amount__max']

    for amount in amounts:
        amount.perc_amount = amount.amount / max_amount * 100

    return render(request, "bloodmanager/supply_overview.html", {
        'amounts': amounts,
        'max_amount': max_amount,
        'institution': institution
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


def send_notification(request, pk, blood_type):
    if request.method == 'GET':
        institution = Institution.objects.get(pk=pk)
        title = 'Alartmantno - fali krvne grupe {}'.format(blood_type)
        message = "Fali na krvi. Molim vas da donirate"
        institution_users = institution.user_set.all()

        for institution_user in institution_users:
            Notification.objects.create(
                title=title,
                message=message,
                user=institution_user
            )

    return redirect('supply_overview')
