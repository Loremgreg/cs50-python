main()
  ↓
Crée PathologyDatabase → charge JSON → liste d'objets Pathology en mémoire
  ↓
Crée PathologyMenu(database) → menu.database pointe vers PathologyDatabase
  ↓
menu.run() → affiche menu → utilisateur choisit option 2
  ↓
menu.handle_search_by_name() → demande nom → appelle self.database.get_by_name()
  ↓
database.get_by_name() → cherche dans self.pathologies → retourne objet Pathology
  ↓
print(pathology) → appelle pathology.__str__() → affiche le résultat