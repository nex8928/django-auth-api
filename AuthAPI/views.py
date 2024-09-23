from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return JsonResponse({"message": "Welcome to the Auth API"})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')

@login_required
def dashboard_view(request):
    # Example data to pass to the template
    line_chart_data = [65, 59, 80, 81, 56, 55, 40]
    bar_chart_data = [12, 19, 3, 5, 2, 3]
    pie_chart_data = [300, 50, 100]
    
    context = {
        'user': request.user,
        'line_chart_data': line_chart_data,
        'bar_chart_data': bar_chart_data,
        'pie_chart_data': pie_chart_data,
    }
    return render(request, 'dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')