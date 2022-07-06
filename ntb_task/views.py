from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from ntb_task.forms import CreationForm, ResourceForm
from ntb_task.models import Resource
from ntb_task.viewsmixins import IsAuthorMixin

User = get_user_model()


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy(
        "login")
    template_name = "signup.html"


class ResourceCreate(LoginRequiredMixin, CreateView):
    model = Resource
    template_name = 'resource_create.html'
    form_class = ResourceForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('index')


class ResourceView(LoginRequiredMixin, ListView):
    model = Resource
    template_name = 'resources_list.html'
    context_object_name = 'resources'

    def get_queryset(self):
        owner = get_object_or_404(User, id=self.request.user.id)
        queryset = Resource.objects.filter(owner=owner)
        return queryset


class ResourceEdit(IsAuthorMixin, LoginRequiredMixin, UpdateView):
    model = Resource
    template_name = 'resource_change.html'
    form_class = ResourceForm
    context_object_name = 'resource'

    def get_success_url(self):
        return reverse_lazy('index')


def index(request):
    return render(request, 'index.html')