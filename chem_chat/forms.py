from django import forms
from django.forms import ModelForm
from .models import ChemSmiles

class SmilesForm(forms.Form):
    input_smiles = forms.CharField(label="usersmiles", max_length=500)
    
    def clean_smiles(self):
        smiles = self.cleaned_data["input_smiles"]
        try:
            mol = Chem.MolFromSmiles(smiles)
        except Exception:
            raise forms.ValidationError("適正なsmilesが入力されませんでした")


class ModelBindedSmilesForm(ModelForm):
    class Meta:
        model = ChemSmiles
        fields = ["smiles"]
