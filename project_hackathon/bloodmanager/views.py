from django.shortcuts import render, redirect
from project_hackathon.bloodmanager.models.main import BloodAmount
from django.db.models import Max
from project_hackathon.bloodmanager.models.common import Institution, Notification
from django.contrib.auth import get_user_model
from bloodmanager.forms import UserForm, NotificationForm
from project_hackathon.bloodmanager.models.main import Donation

from bloodmanager.forms import UserForm, NewUserForm


def index_admin(request):

    return render(request, "bloodmanager/supply_overview.html", {

    })

def user_home(request):
    notifications = Notification.objects.filter(
        user=request.user
    )
    return render(request, "bloodmanager/user_home.html", {
        'notifications': notifications
    })

def user_overview(request):
    all_users = get_user_model().objects.all()
    return render(request, "bloodmanager/user_overview.html", {
        'users': all_users,
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
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        form2 = UserForm(request.POST)
        if form.is_valid() and form2.is_valid():
            data = form.cleaned_data
            data2 = form2.cleaned_data

            # obj = get_user_model().objects.create(
            #     username=data['username'],
            #     password=data['password1'],
            # )
            # import pdb; pdb.set_trace()
            # obj.email=data['email'],
            # obj.telephone_number=data['telephone_number'],
            # obj.date_of_birth=data['date_of_birth'],
            # obj.gender=data['gender'],
            # obj.comment=data['comment'],
            # obj.bloodtype=data['bloodtype'],
            # obj.location=data['location'],
            # obj.institution=data['institution']
            # obj.save()
            # import pdb; pdb.set_trace()
            # return HttpResponseRedirect(reverse('supply_overview'))

    else:
        form = NewUserForm()
        form2 = UserForm()

    return render(request, "bloodmanager/add_donator.html", {
        'form': form,
        'form2': form2
    })

def index_user(request):
    user = request.user
    donations = Donation.objects.filter(user=user.id)
    institutions = []
    for donation in donations:
        institutions.append(donation.institution)
    return render(request, "bloodmanager/my_donations.html", {
        'user': user,
        'donations': donations,
        'institutions': institutions
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


def new_donation(request):
    return render(request, "bloodmanager/new_donation.html", {

    })


def send_notification(request, pk, blood_type):
    if request.method == 'GET':
        institution = Institution.objects.get(pk=pk)
        title = 'Alartmantno - fali krvne grupe {}'.format(blood_type)
        message = "Fali nam krvi. Molim vas da donirate"
        institution_users = institution.user_set.all()

        for institution_user in institution_users:
            Notification.objects.create(
                title=title,
                message=message,
                user=institution_user
            )

    return redirect('supply_overview')


def send_notification_user(request):
    initial_data = {
        'title': '',
        'message': '',
        'user': None,
    }

    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Notification.objects.create(
                title=data['title'],
                message=data['message'],
                user=data['user'],
            )

            return redirect('send_notification_user')
    else:
        form = NotificationForm(initial=initial_data)


    return render(request, "bloodmanager/send_notification_user.html", {
        'form': form,
    })
