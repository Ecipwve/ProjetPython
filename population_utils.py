from population_api import fetch_departments_population, fetch_city_population

def recuperer_population(code):

    # Détermine si l'utilisateur a entré un département ou un code postal, puis récupère la population correspondante.

    if code.isdigit():
        if len(code) == 2:  # Département
            name, population = fetch_departments_population(code)
            if name and population:
                return f"{name} (Département)", f"Environ {population} habitants"
            return None, "Impossible de récupérer la population du département."

        elif len(code) == 5:  # Commune
            name, population = fetch_city_population(code)
            if name and population:
                return name, f"Population estimée à {population} habitants"
            return None, "Aucune commune trouvée avec ce code postal."

    return None, "Veuillez entrer un code départemental (2 chiffres) ou un code postal valide (5 chiffres)."
