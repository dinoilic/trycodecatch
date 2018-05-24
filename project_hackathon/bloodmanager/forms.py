from django.utils.translation import ugettext as _
from django import forms
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, HTML, Div, Submit
from project_hackathon.bloodmanager.models.common import Notification
from crispy_forms.helper import FormHelper
from django.urls import reverse_lazy


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.render_unmentioned_fields = False
        # default template
        default_layout = Layout(
            Div(
                Div(
                    'name',
                    'email',
                    'telephone_number',
                    'comment',
                    'bloodtype',
                    'institution',
                    css_class='col-sm-6'
                ),
                Div(
                    'location',
                    Field('date_of_birth'),
                    'gender',
                    css_class='col-sm-6'
                ),
                css_class='well the-fieldset row'
            ),
        )

    class Meta:
        model = get_user_model()
        fields = ['name', 'email', 'location',
                  'date_of_birth', 'gender', 'comment',
                  'bloodtype', 'institution', 'telephone_number']


class NotificationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NotificationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-personal-data-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse_lazy('send_notification_user')
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Notification
        fields = ['title', 'message', 'user']
