def water_plants(days=1):
    # Check if plants need watering
    plants = get_plants()
    for plant in plants:
        if plant.get("water") < 10:
            # Water the plant
            plant.set("water", 10)
