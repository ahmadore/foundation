from django.shortcuts import render
from django.http import HttpResponse
from .models import Scholarship, Empowerment, ScholarshipBeneficiary, EmpowermentBeneficiary
from events.models import Event, EventGallery

# Create your views here.
def index(request):
    scholarships = Scholarship.objects.all()
    empowerments = Empowerment.objects.all()
    context = {
        'scholarships': scholarships,
        'empowerments': empowerments
    }
    return render(request, 'foundation/scholarships.html', context)

def scholarship_detail(request, pk):
    beneficiaries = ScholarshipBeneficiary.objects.filter(scholarship__id=pk)
    scholarship = Scholarship.objects.get(id=pk)
    context = {
        "beneficiaries": beneficiaries,
        "scholarship": scholarship
    }
    return render(request, 'foundation/scholarship_detail.html', context)

def empowerment_detail(request, pk):
    beneficiaries = EmpowermentBeneficiary.objects.filter(empowerment=pk)
    empowerment = Empowerment.objects.get(id=pk)
    context = {
        "beneficiaries": beneficiaries,
        "empowerment": empowerment
    }
    return render(request, 'foundation/empowerment_detail.html', context)
