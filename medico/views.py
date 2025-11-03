
from django.shortcuts import render
from django.http import Http404

from medico.models import *

# Create your views here.

def about(request):
    return render(request, "medico/about.html")

def consultation(request, consultation_id):
    try:
        consultation = Consultation.objects.get(pk=consultation_id)
    except Consultation.DoesNotExist:
        raise Http404("La consultation n'existe pas")
    return render(request, "medico/consultations.html", {"consultation":consultation})