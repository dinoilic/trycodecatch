from django.utils.translation import ugettext as _
from django import forms
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, HTML, Div, Submit
from project_hackathon.bloodmanager.models.main import Notification
from crispy_forms.helper import FormHelper
from django.urls import reverse_lazy


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.render_unmentioned_fields = False
        # default template
        self.helper.layout = Layout(
            Div(
                Div(
                    'name',
                    'email',
                    'telephone_number',
                    'comment',
                    css_class='col-sm-6'
                ),
                Div(
                    'location',
                    Field('date_of_birth'),
                    'gender',
                    'institution',
                    'bloodtype',
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


class NewUserForm(forms.Form):
    username = forms.CharField(
        label=_('Username'), max_length=100
    )

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification.")
    )

    def __init__(self, *args, **kwargs):

        super(NewUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.render_unmentioned_fields = False
        # default template
        self.helper.layout = Layout(
           'username',
           'password1',
           'password2'
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2


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
