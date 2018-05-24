from django.shortcuts import render, redirect
from project_hackathon.bloodmanager.models.main import BloodAmount
from django.db.models import Max
from project_hackathon.bloodmanager.models.common import Institution, Notification

from bloodmanager.forms import UserForm

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

    initial_data = {
        'name': request.user.name,
        'email': request.user.email,
        'comment': request.user.comment,
        'bloodtype': request.user.bloodtype,
        'institution': request.user.institution.name,
        'location': request.user.location,
        'date_of_birth': request.user.date_of_birth,
        'gender': request.user.gender
    }

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            return HttpResponseRedirect(reverse('my_profile'))

    else:
        form = UserForm(initial=initial_data)
    return render(request, "bloodmanager/my_profile.html", {
        'form': form,
    })


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

