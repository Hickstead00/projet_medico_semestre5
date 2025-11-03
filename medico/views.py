
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponseRedirect

from medico.models import *
from medico.forms import *

# Create your views here.

def about(request):
    return render(request, "medico/about.html")

def consultation(request, consultation_id):
    try:
        consultation = Consultation.objects.get(pk=consultation_id)
    except Consultation.DoesNotExist:
        raise Http404("La consultation n'existe pas")
    return render(request, "medico/consultations.html", {"consultation":consultation})


def consultations(request):
    consultations = Consultation.objects.order_by("-date_consultation")
    context = {"all_consultations" : consultations}
    return render (request,"medico/list_consultations.html",context)

def nouvelle_consultation(request):
    if request.method == "POST":
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consult = form.save(commit=False)
            consult.save()
        return HttpResponseRedirect(f"consultations/{consult.id}")
    else:
        form = ConsultationForm()
    return render(request,"medico/nouvelle_consultation_form.html",{"form" : form})

def effacer_consultation(request,consultation_id):
    consultation=get_object_or_404(Consultation,pk=consultation_id)
    if request.method =="POST":
        consultation.delete()
        return redirect("consultations")
    return render(request,"medico/effacer_consultation.html",{"consultation":consultation})

def check_save(form):
    if form.is_valid():
        consultation = form.save(commit=False)
        consultation.save()
    return consultation.id

def modifier_consultation(request, consultation_id):
    consultation = get_object_or_404(Consultation,pk=consultation_id)
    if request.method == "POST":
        form = ConsultationForm(request.POST, instance=consultation)
        id = check_save(form)
        return redirect("consultation", consultation_id=id)
    else:
        form = ConsultationForm(instance=consultation)
    return render(request, "medico/modifier_consultation.html", {"form" : form ,"button_label": "Modifier"})