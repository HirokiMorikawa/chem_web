from django.shortcuts import render

from django.http.response import JsonResponse
from .models import ChemSmiles
from .forms import SmilesForm
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def index(request):
    pass

def chem_chat(request):
    """
    POST only
    """
    
    if request.method == "POST":
        smiles_form = SmilesForm(request.POST)
        if smiles_form.is_valid():
            chem_smiles = ChemSmiles.objects.create(
                smiles=smiles_form.cleaned_data["input_smiles"])
            # smiles_form.save(commit=True)
            return JsonResponse(
                {
                    "smiles": smiles_form.cleaned_data["input_smiles"]
                }
            )
        else:
            smiles_form = SmilesForm()
    return render(request, None, None)