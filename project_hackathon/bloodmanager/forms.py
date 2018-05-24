from django.utils.translation import ugettext as _
from django import forms
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, HTML, Div


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


