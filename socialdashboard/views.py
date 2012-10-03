from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

def home(request):
    users = get_user_model().objects.filter(is_active=True)
    return render(request, 'socialdashboard/home.html', {'users': users})

def user_detail(request, identifier):
    user_model = get_user_model()
    user = get_object_or_404(user_model, **{user_model.USERNAME_FIELD: identifier})
    return render(request, 'socialdashboard/user.html', {'user': user})

