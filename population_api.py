import requests

def fetch_departments_population(department_code):

    # Récupère la population totale d'un département en additionnant les populations de ses communes
    url_dep = f"https://geo.api.gouv.fr/departements/{department_code}"
    url_villes = f"https://geo.api.gouv.fr/departements/{department_code}/communes"

    try:
        rep_dep = requests.get(url_dep, verify=False)
        rep_villes = requests.get(url_villes, verify=False)

        if rep_dep.ok and rep_villes.ok:
            info_dep = rep_dep.json()
            villes = rep_villes.json()
            total_population = sum(ville["population"] for ville in villes)
            return info_dep["nom"], total_population

    except requests.exceptions.RequestException:
        return None, None
    
    return None, None

def fetch_city_population(postal_code):

    #Récupère la population d'une ou plusieurs communes à partir d'un code postal
    url = f"https://geo.api.gouv.fr/communes?codePostal={postal_code}"

    try:
        rep = requests.get(url, verify=False)
        if rep.ok:
            villes = rep.json()
            if villes:
                total_population = sum(ville["population"] for ville in villes)
                city_names = ", ".join(ville["nom"] for ville in villes)
                return city_names, total_population

    except requests.exceptions.RequestException:
        return None, None
    
    return None, None
