from django.shortcuts import redirect

from ntb_task.forms import ResourceFormAdmin


def is_admin(user):
    return any((
        user.role == 'admin',
        user.is_staff,
        user.is_superuser
    ))


class IsAuthorMixin:
    def dispatch(self, request, *args, **kwargs):
        if is_admin(request.user):
            return super().dispatch(request, *args, **kwargs)
        if request.user != self.get_object().owner:
            return redirect("index")
        return super().dispatch(request, *args, **kwargs)


class IsAdminMixin:
    def get_form(self, form_class=None):
        if is_admin(self.request.user):
            return ResourceFormAdmin
        return self.form_class
