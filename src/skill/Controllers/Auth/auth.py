from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import logout
from django.shortcuts import render
from django.shortcuts import redirect
from ...forms.auth.forms import AuthForm
from django.contrib.auth import authenticate


class MyRegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "auth/registration.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    form = AuthForm
    return render(request, 'auth/login.html', {'form': form})


def enter(request):
    authenticate(email=request.POST.get('email'), password=request.POST.get('password'))
    return redirect('/')