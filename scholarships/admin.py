from django.contrib import admin
from .models import Scholarship, Empowerment, ScholarshipBeneficiary, EmpowermentBeneficiary
# Register your models here.


admin.site.register(Scholarship)
admin.site.register(ScholarshipBeneficiary)

admin.site.register(Empowerment)
admin.site.register(EmpowermentBeneficiary)