
import os

def get_garden_plants():
    plants = []
    for file in os.listdir("."):
        if file.endswith(".txt"):
            with open(file) as f:
                content = f.read()
                plant_name, plant_species = content.split(", ")
                plants.append((plant_name, plant_species))
    return plants