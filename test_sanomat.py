# SANOMAT.PY-MODULIN TESTIT

# Modulien ja kirjastojen lataukset
import sanomat

# Testataan, että merkkijonon erotinmerkit tulevat oikein
def test_muodosta_sanoma():
    assert sanomat.muodosta_sanoma(3000, 4000, 5000, 0) == '3000|4000|5000|0|'
    
# Sama testi, mutta Janin funtiota käyttäen
def test_muodosta_sanoma2():
    assert sanomat.muodosta_sanoma2(3000, 4000, 5000, 0) == '3000|4000|5000|0|'
    
def test_summaa_merkit():
    assert sanomat.summaa_merkit('3000|4000|5003|3|') == 1138

def test_laske_varmiste():
    assert sanomat.laske_varmiste(1138) == 122
    assert sanomat.laske_varmiste(127) == 0
    assert sanomat.laske_varmiste(128) == 1
    
def test_lopullinen_sanoma():
    assert sanomat.lopullinen_sanoma('3000|4000|5003|3|', 122) == '<3000|4000|5003|3|122>'
    
def test_muodosta_varmiste():
    merkit = '3000|4000|5003|3|'
    jakaja = 127
    assert sanomat.muodosta_varmiste(merkit, jakaja) == '122'