from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_text
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from ...tokens import account_activation_token
from ...forms.auth.forms import AuthForm
from ...forms.auth.forms import NewPassForm
from django.contrib.auth import login, authenticate, logout
from ...forms.auth.forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage


def activate(request, uidb64, token):
    uid = force_text(urlsafe_base64_decode(uidb64))
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            print(request.POST)
            user = User.objects.get(pk=uid)
            user.set_password(request.POST.get('password1'))
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
        else:
            print('ERROR')
    else:
        try:
            user = User.objects.get(pk=uid)

        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            form = NewPassForm(request.POST)
            return render(request, 'auth/newpass.html', {'form': form})
        else:
            return HttpResponse('Activation link is invalid!')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            authenticate(request, email=user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'auth/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        try:
            user = User.objects.filter(email=request.POST.get('email'))[0]
            login(request, user, backend='skill.backends.EmailAuthBackend')
        except(TypeError, ValueError, OverflowError, User.DoesNotExist, IndexError):
            user = None

        return redirect('/signin/')

    else:
        form = AuthForm()
        return render(request, 'auth/signin.html', {'form': form})


def exit(request):
    logout(request)
    return redirect('/signin/')


def forgot(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST.get('email'))[0]
        current_site = get_current_site(request)
        message = render_to_string('mail/pass.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        mail_subject = 'Activate your blog account.'
        to_email = request.POST.get('email')
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()
        return render(request, 'auth/forgot.html', {})
    else:
        return render(request, 'auth/forgot.html', {})


def api(request):
    return render(request, 'react.html', {})
