from __future__ import unicode_literals

from django.db import models

from events.models import Event

SHOLARSHIP_TYPE = (('PM', 'permanent'),
                    ('BS', 'bursary'))

INSTITUTION_TYPE = (('UNI', 'university'),('POL', 'polytechnic'), ('NUR', 'School of Nursing'), ('COE','College of Education'))

GENDER = (('M', 'Male'), ('F', 'Female'))


# Create your models here.

# Scholarship program in an event
class Scholarship(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title

# Empowerment program in an event
class Empowerment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title

# beneficiaries of the scholarship and bursary
class ScholarshipBeneficiary(models.Model):
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE, related_name='beneficiaries')
    full_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=1, choices=GENDER)
    institution = models.CharField(max_length=500, null=True, blank=True)
    institution_type = models.CharField(max_length=3, choices=INSTITUTION_TYPE)
    course = models.CharField(max_length=200)
    level = models.IntegerField()
    matric_number = models.CharField(max_length=20, null=True, blank=True)
    
    scholarship_type = models.CharField(max_length=2, choices=SHOLARSHIP_TYPE)
    description = models.TextField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "%s %s" %(self.full_name, self.scholarship)


class EmpowermentBeneficiary(models.Model):
    empowerment = models.ForeignKey(Empowerment, on_delete=models.CASCADE, related_name='beneficiaries')
    gender = models.CharField(max_length=1, choices=GENDER)
    full_name = models.CharField(max_length=150)
    ward = models.CharField(max_length=50)
    trade = models.CharField(max_length=50)
    item = models.CharField(max_length=100, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return "%s %s" %(self.full_name, self.empowerment)