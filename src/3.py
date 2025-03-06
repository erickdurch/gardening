import os
import random

def plant_selection():
    plants = ['rose', 'sunflower', 'daisy', 'dandelion']
    selected_plant = random.choice(plants)
    print(f"You have selected {selected_plant} as your gardening project.")

plant_selection()