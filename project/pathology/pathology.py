
'''
creer un fichier pathology_data.py
PATHOLOGIES = [
    {
        "slug": "epaule-gelee",
        "name": "Épaule gelée (capsulite adhésive)",
        "typical_duration_weeks": 40,
        "phases": ["Phase douloureuse", "Phase gelée", "Phase de récupération"],
        "prognosis": "Bon sur le long terme, mais récupération lente.",
        "red_flags": [
            "Douleur nocturne insupportable",
            "Perte de force importante non expliquée",
        ],
        "key_points": [
            "Informer le patient sur la durée potentiellement longue.",
            "Adapter la charge et éviter les mobilisations trop agressives.",
        ],

'''

'''
fonction 

1. recherche non sensible de nom : normalize_name() 
2. Retourne la pathologie dont le slug correspond: get_pathology_by_slug()
3. Recherche simple par mot clé (ou partie du nom): search_pathologies_by_query()
4. filtrer selon MS, MI, Dos, Traumatologie (fracture, elongation): search_pathologies_by_body_part: 

main 
Si tape :
1. liste toutes les patho
2. Recherche par nom (par slug) : get_pathology_by_slug()
3. Recherche par mot clé:  search_pathologies_by_query()
4. filtrer selon partie du corps: search_pathologies_by_body_part: 
5. quitter 


print 
le menu interractif 
→ plusieurs actions
→ saisie utilisateur
→ affichage formaté
→ moteur de recherche simple
'''
 

