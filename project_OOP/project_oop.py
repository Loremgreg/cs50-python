import json

class Pathology:
    def __init__(self, name, body_part, typical_duration_weeks, phases, prognosis, red_flags, key_points):
        self.name = name
        self.body_part = body_part
        self.typical_duration_weeks = typical_duration_weeks
        self.phases = phases
        self.prognosis = prognosis
        self.red_flags = red_flags
        self.key_points = key_points
    
    def __str__(self):
        return f"Pathology: {self.name}"

    def load_pathologies():
        with open("pathologies_data.json") as data_file:
            parsed_json = json.load(data_file)

        list_of_patho = []
        for pathology in parsed_json:
            if pathology["name"]:
                list_of_patho.append(pathology["name"])
        
        print("List of pathologies:\n")
        for patho in list_of_patho:
            print(f" - {patho}")

        return list_of_patho