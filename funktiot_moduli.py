# X-funktio tarkistaa onko kulma suora
# TODO:Lisää funktioon virheen laskenta millimetreinä
def suorakulma(sivuA, sivuB, lavistaja):
    """Tarkistaa suorakulmaisuuden käyttäen Pythagoraan lausetta

    Args:
        sivuA (float): Ensimmäisen seinän pituus
        sivuB (float): Toisen seinän pituus
        lavistaja (float): Huoneen lävistäjän pituus

    Returns:
        boolean: TRUE -> suorakulma
    """
    A_nelio = sivuA * sivuA
    B_nelio = sivuB * sivuB
    l_nelio = lavistaja * lavistaja
    # FIXME: jos antaa vahingossa kirjaimen arvoksi -> kaatuu
    if A_nelio + B_nelio == l_nelio:
        suora = True
    else:
        suora = False
    return suora

# Testataan, että toimii, poista tämä myöhemmin
if __name__ == "__main__":
    # Testi kulma on suora
    vastaus = suorakulma(3, 4, 5)
    print(vastaus)

    # Testi kulma ei ole suora
    vastaus = suorakulma(3, 4, 6)
    print(vastaus)