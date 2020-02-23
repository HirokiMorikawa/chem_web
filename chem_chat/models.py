from django.db import models
from rdkit import Chem

# Create your models here.

class ChemSmiles(models.Model):
    smiles = models.CharField(max_length=500) # smiles

    