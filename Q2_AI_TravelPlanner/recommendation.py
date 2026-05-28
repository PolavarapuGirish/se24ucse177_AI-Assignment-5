from knowledge_base import tourist_places, food_data

def recommend_place(interest):
    results = []

    for city, details in tourist_places.items():
        if details["type"].lower() == interest.lower():
            results.append(city)

    return results

def recommend_food(city):
    return food_data.get(city, [])

def generate_plan(city, days):
    places = tourist_places[city]["places"]

    plan = []

    for i in range(days):
        if i < len(places):
            plan.append(f"Day {i+1} -> {places[i]}")
        else:
            plan.append(f"Day {i+1} -> Free Exploration")

    return plan
