
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
            # Si un objet spécial a été sélectionné, décrémenter le stock
            if traitement.objet_special_id:
                try:
                    inv = InventoryItem.objects.select_for_update().get(item_id=traitement.objet_special_id)
                except InventoryItem.DoesNotExist:
                    inv = None
                if inv and inv.quantite > 0:
                    inv.quantite -= 1
                    inv.save()
            
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
        old_objet_id = traitement.objet_special_id
        form = TraitementForm(request.POST, instance=traitement)
        if form.is_valid():
            updated = form.save()
            new_objet_id = updated.objet_special_id
            # Ajuster le stock si l'objet spécial change
            if old_objet_id != new_objet_id:
                # restituer l'ancien si existait
                if old_objet_id:
                    inv_old, _ = InventoryItem.objects.get_or_create(item_id=old_objet_id, defaults={'quantite': 0})
                    inv_old.quantite += 1
                    inv_old.save()
                # consommer le nouveau si existe
                if new_objet_id:
                    inv_new, _ = InventoryItem.objects.get_or_create(item_id=new_objet_id, defaults={'quantite': 0})
                    if inv_new.quantite > 0:
                        inv_new.quantite -= 1
                        inv_new.save()
        return HttpResponseRedirect(f"/medico/consultations/{id_consultation}")
    else:
        form = TraitementForm(instance=traitement)
    return render(request,f"medico/modifier_traitement.html",{'form' : form, 'id_consultation': id_consultation})

def black_market_confirm(request):
    return render(request, "medico/black_market_confirm.html")

def black_market(request):
    items = BlackMarketItem.objects.all()
    panier = request.session.get('panier', {})
    nombre_articles = 0
    if isinstance(panier, dict):
        for item in panier.values():
            nombre_articles += item.get('quantite', 0)
    return render(request, "medico/black_market.html", {"items": items, "panier_nombre_articles": nombre_articles})

def ajouter_au_panier(request, item_id):
    item = get_object_or_404(BlackMarketItem, pk=item_id)
    
    panier = request.session.get('panier', {})
    
    item_id_str = str(item_id)
    
    if item_id_str in panier:
        panier[item_id_str]['quantite'] += 1
    else:
        panier[item_id_str] = {
            'nom': item.nom_item,
            'prix': float(item.prix),
            'quantite': 1,
            'image_url': item.image_url
        }
    
    request.session['panier'] = panier
    request.session.modified = True
    
    return redirect('black_market')

def panier(request):
    panier = request.session.get('panier', {})
    
    if not isinstance(panier, dict):
        panier = {}
        request.session['panier'] = panier
    
    total = 0
    nombre_articles = 0
    
    for item in panier.values():
        if isinstance(item, dict):
            total += item.get('prix', 0) * item.get('quantite', 0)
            nombre_articles += item.get('quantite', 0)
    
    context = {
        'panier': panier,
        'total': total,
        'nombre_articles': nombre_articles
    }
    
    return render(request, 'medico/panier.html', context)

def retirer_du_panier(request, item_id):
    panier = request.session.get('panier', {})
    item_id_str = str(item_id)
    
    if item_id_str in panier:
        del panier[item_id_str]
        request.session['panier'] = panier
        request.session.modified = True
    
    return redirect('panier')

def retirer_un_du_panier(request, item_id):
    panier = request.session.get('panier', {})
    item_id_str = str(item_id)

    if item_id_str in panier and isinstance(panier[item_id_str], dict):
        current_qte = panier[item_id_str].get('quantite', 0)
        if current_qte > 1:
            panier[item_id_str]['quantite'] = current_qte - 1
        else:
            del panier[item_id_str]

        request.session['panier'] = panier
        request.session.modified = True

    return redirect('panier')

def ajouter_un_au_panier(request, item_id):
    item = get_object_or_404(BlackMarketItem, pk=item_id)

    panier = request.session.get('panier', {})
    item_id_str = str(item_id)

    if item_id_str in panier:
        panier[item_id_str]['quantite'] = panier[item_id_str].get('quantite', 0) + 1
    else:
        panier[item_id_str] = {
            'nom': item.nom_item,
            'prix': float(item.prix),
            'quantite': 1,
            'image_url': item.image_url
        }

    request.session['panier'] = panier
    request.session.modified = True

    return redirect('panier')

def vider_panier(request):
    if 'panier' in request.session:
        del request.session['panier']
    return redirect('panier')

def valider_achat(request):
    panier = request.session.get('panier', {})
    
    if not panier:
        return redirect('panier')
    
    total = sum(item['prix'] * item['quantite'] for item in panier.values())
    # Persister en inventaire global (pas de notion d'utilisateur ici)
    for item_id_str, item in panier.items():
        try:
            item_id = int(item_id_str)
        except (TypeError, ValueError):
            continue
        quantite = int(item.get('quantite', 0))
        if quantite <= 0:
            continue
        inv, _ = InventoryItem.objects.get_or_create(item_id=item_id, defaults={'quantite': 0})
        inv.quantite += quantite
        inv.save()

    del request.session['panier']

    return render(request, 'medico/achat_confirme.html', {'total': total})

