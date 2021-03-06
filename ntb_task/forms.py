from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from ntb_task.models import Resource, User


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        fields = (
            'ip',
            'port',
            'type_resource',
        )


class ResourceFormAdmin(ModelForm):
    class Meta:
        model = Resource
        fields = (
            'ip',
            'port',
            'type_resource',
            'owner',
        )
