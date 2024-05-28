from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import RedirectView


class CustomLogoutView(LoginRequiredMixin, RedirectView):
    """
    Custom logout view that logs the user out and redirects to a specific URL.
    """
    url = reverse_lazy('logout') 

    def get_redirect_url(self, *args, **kwargs):
        self.request.session.flush()  
        return super().get_redirect_url(*args, **kwargs)


def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')