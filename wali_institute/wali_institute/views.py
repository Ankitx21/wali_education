from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import AdmissionEnquiry

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def courses(request):
    return render(request, 'courses.html')

def facilities(request):
    return render(request, 'facilities.html')

def admissions(request):
    return render(request, 'admissions.html')

def about_us(request):
    return render(request, 'about_us.html')

def gallery(request):
    return render(request, 'gallery.html')

def submit_enquiry(request):
    if request.method == 'POST':
        try:
            enquiry = AdmissionEnquiry(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                subject=request.POST.get('subject'),
                email=request.POST.get('email'),
                mobile=request.POST.get('mobile')
            )
            enquiry.save()
            return JsonResponse({'status': 'success', 'message': 'Enquiry submitted successfully!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})