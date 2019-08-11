from django.contrib import admin
from .models import Candidate_Enrollment, Voters_Enrollment
# Register your models here.
admin.site.register(Candidate_Enrollment)
admin.site.register(Voters_Enrollment)