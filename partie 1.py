import sys ### INUTILE / POSSIBLE DE SUPPRIMER
sys.path.append(r"C:\Users\aresv\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages") ### INUTILE / POSSIBLE DE SUPPRIMER
import requests

def recuperer_population(code):

    if code.isdigit():
        if len(code) == 2:  # Département
            url_dep = f"https://geo.api.gouv.fr/departements/{code}"
            url_villes = f"https://geo.api.gouv.fr/departements/{code}/communes"

            try:
                rep_dep = requests.get(url_dep, verify=False)
                rep_villes = requests.get(url_villes, verify=False)

                if rep_dep.ok and rep_villes.ok:
                    info_dep = rep_dep.json()
                    villes = rep_villes.json()
                    total_population = sum(ville["population"] for ville in villes)
                    return f"{info_dep['nom']} (Département)", f"Environ {total_population} habitants"
                
                return None, "Les informations n'ont pas pu être récupérées"

            except requests.exceptions.RequestException:
                return None, "Une erreur est survenue lors de la récupération des données"

        elif len(code) == 5:  # Commune
            url = f"https://geo.api.gouv.fr/communes?codePostal={code}"

            try:
                rep = requests.get(url, verify=False)
                if rep.ok:
                    villes = rep.json()
                    if villes:
                        total_pop = sum(ville["population"] for ville in villes)
                        noms_villes = ", ".join(ville["nom"] for ville in villes)
                        return noms_villes, f"Population estimée à {total_pop} habitants"
                    
                    return None, "Aucune ville trouvée avec ce code postal"

                return None, "Impossible d'obtenir les informations"

            except requests.exceptions.RequestException:
                return None, "Un problème de connexion empêche l'accès aux données"

    return None, "Veuillez entrer un code départemental (2 chiffres) ou un code postal valide (5 chiffres)"

def programme_principal():
    code = input("Entrez un code de département (ex: 75) ou un code postal (ex: 75001) : ")
    nom, population = recuperer_population(code)

    if nom:
        print(f"{nom} : {population}")
    else:
        print(population)

if __name__ == "__main__":
    programme_principal()
