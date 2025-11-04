
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponseRedirect

from medico.models import *
from medico.forms import *

# Create your views here.

def about(request):
    return render(request, "medico/about.html")

def accueil(request):
    dernieres_consultations = Consultation.objects.order_by('-date_consultation')[:5]
    return render(request, "medico/accueil.html", {"dernieres_consultations": dernieres_consultations})

def consultation(request, consultation_id):
    consultation = get_object_or_404(Consultation, pk=consultation_id)
    traitements = consultation.traitement_set.all()
    return render(request, "medico/consultations.html", {"consultation":consultation, "traitements":traitements})


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

def changer_consultation(request, consultation_id):
    consultation = get_object_or_404(Consultation,pk=consultation_id)
    if request.method == "POST":
        form = ConsultationForm(request.POST, instance=consultation)
        id = check_save(form)
        return redirect("consultation", consultation_id=id)
    else:
        form = ConsultationForm(instance=consultation)
    return render(request, "medico/changer_consultation.html", {"form" : form ,"button_label": "Modifier"})


def nouveau_traitement(request,consultation_id):
    consultation = get_object_or_404(Consultation,pk=consultation_id)
    if request.method=="POST":
        form = TraitementForm(request.POST)
        if form.is_valid():
            traitement = form.save(commit=False)
            traitement.consultation=consultation
            traitement.save()
        return HttpResponseRedirect(f"/medico/consultations/{consultation_id}")
    else:
        form= TraitementForm()
    return render(request,f"medico/nouveau_traitement.html",{'form':form, "consultation_id":consultation_id})

def supprimer_traitement(request,traitement_id):
    traitement=get_object_or_404(Traitement,pk=traitement_id)
    if request.method =="POST":
        traitement.delete()
        return redirect('consultation', consultation_id = traitement.consultation.id)
    return render(request,"medico/supprimer_traitement.html",{"traitement":traitement})

def modifier_traitement(request,traitement_id):
    traitement = get_object_or_404(Traitement,pk=traitement_id)
    id_consultation = traitement.consultation.id
    if request.method == "POST":
        form = TraitementForm(request.POST, instance=traitement)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(f"/medico/consultations/{id_consultation}")
    else:
        form = TraitementForm(instance=traitement)
    return render(request,f"medico/modifier_traitement.html",{'form' : form, 'id_consultation': id_consultation})
