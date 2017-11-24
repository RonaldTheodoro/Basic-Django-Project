from django.contrib.auth import login
from django.shortcuts import redirect, render

from . import forms


def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:index')

    else:
        form = forms.SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
