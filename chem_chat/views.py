from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.http.response import JsonResponse
from .models import ChemSmiles
from .forms import SmilesForm
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def index(request):
    smiles_input_form = SmilesForm()
    return render(
        request,
        "chem_chat/index.html",
        {"smiles_input_form": smiles_input_form}
    )
    
@require_http_methods(["POST"])
def chem_chat(request):
    """
    POST only
    """

    smiles_form = SmilesForm(request.POST)
    chem_chat= {
        "smiles": ""
    }
    if smiles_form.is_valid():
        ChemSmiles.objects.create(
            smiles=smiles_form.cleaned_data["input_smiles"])
        # smiles_form.save(commit=True)
        chem_chat["smiles"] = smiles_form.cleaned_data["input_smiles"]
    else:
        chem_chat["smiles"] = "cannot convert your smiles text."
    return JsonResponse(chem_chat)
            
            