Architecture proposée

  - Pathology : représente une entrée JSON (name, body_part, phases, etc.). Tu peux en faire une @dataclass
    avec une méthode describe() qui encapsule tout l’affichage actuellement dans get_pathology_by_name
    (project.py:67-96), afin que l’objet sache déjà formater ses données.
  - PathologyRepository : s’occupe de lire pathologies_data.json une seule fois et de fournir
    list_all(), find_by_name(), list_sorted_by_body_part(), etc. Cela remplace les lectures répétées dans
    list_all_pathologies et get_pathology_by_body_part (project.py:47-104). Tu pourrais stocker les objets
    Pathology dans une liste et indexer par nom normalisé.
  - PathologyCLI ou PathologyApp : encapsule tout ce que fait aujourd’hui main() (project.py:8-44). Cette
    classe possède une instance de PathologyRepository et gère l’interface (menu, choix utilisateur,
    figlet). Chaque option du menu devient une méthode privée (_show_all(), _search_by_name(), etc.) qui
    appelle le repository et affiche le résultat.

  Étapes concrètes

  - Extraire la lecture du fichier dans PathologyRepository.__init__ pour charger les données et instancier
    les Pathology. Prévois des méthodes comme get_all_names() (remplaçant list_all_pathologies) et
    get_by_name(name) qui renvoient l’objet.
  - Dans Pathology.describe(), réutilise le code d’affichage de get_pathology_by_name pour centraliser
    la logique de présentation. Ainsi, quand PathologyCLI récupère un objet, il lui suffit d’appeler
    print(pathology.describe()).
  - Déplacer la boucle while True et les input() dans PathologyCLI.run(). Le champ figlet peut être une
    dépendance injectée dans cette classe si tu veux pouvoir tester sans la vraie bannière.

  Exemple d’esquisse

  @dataclass
  class Pathology:
      name: str
      body_part: str
      phases: list[str]
      prognosis: str
      # …

      def describe(self) -> str:
          lines = [
              f"{self.name}",
              f"Typical duration (weeks): {self.typical_duration_weeks}",
              "Phases:",
              *(f"  - {phase}" for phase in self.phases),
              # …
          ]
          return "\n".join(lines)

  class PathologyRepository:
      def __init__(self, data_path: Path):
          self._pathologies = [Pathology(**data) for data in json.load(open(data_path))]
          self._index = {p.name.lower(): p for p in self._pathologies}

      def list_all(self) -> list[Pathology]:
          return self._pathologies

      def find_by_name(self, name: str) -> Pathology | None:
          return self._index.get(name.strip().lower())

      def sort_by_body_part(self) -> list[Pathology]:
          return sorted(self._pathologies, key=lambda p: p.body_part)

  class PathologyCLI:
      def __init__(self, repo: PathologyRepository, banner: Figlet):
          self.repo = repo
          self.banner = banner

      def run(self):
          print(self.banner.renderText("Welcome"))
          # menu loop inspiré de main()

  Cette structuration te permet de garder le même comportement tout en séparant clairement la logique métier
  (objets Pathology), l’accès aux données (repository) et l’interface utilisateur (CLI). Ensuite, tu peux
  tester chaque composant indépendamment et faire évoluer la version orientée objet sur ta branche dédiée.