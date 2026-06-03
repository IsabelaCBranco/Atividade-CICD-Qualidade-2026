import os, sys, pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from calculadora import juros_compostos, soma

def test_juros_doze_periodos():
   assert juros_compostos(1000, 0.05, 12) == 1795.86

def test_principal_negativo_levanta_erro():
   with pytest.raises(ValueError):
     juros_compostos(-1, 0.05, 12)

@pytest.mark.parametrize("a,b,e", [(1,2,3),(0,0,0),(-1,1,0)])
def test_soma(a, b, e):
   assert soma(a, b) == e