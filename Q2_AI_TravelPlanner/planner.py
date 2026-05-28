from recommendation import recommend_place
from recommendation import recommend_food
from recommendation import generate_plan
from budget import estimate_cost

def create_travel_plan():
    print("AI Travel Planner")

    interest = input("Enter Interest (Beach/Historical/Hill Station): ")

    budget_level = input("Enter Budget (Low/Medium/High): ")

    days = int(input("Enter Number of Days: "))

    places = recommend_place(interest)

    if not places:
        print("No matching destinations found.")
        return

    city = places[0]

    foods = recommend_food(city)

    plan = generate_plan(city, days)

    total_cost = estimate_cost(budget_level, days)

    print()
    print("Recommended City:", city)

    print()
    print("Tourist Places:")

    for place in plan:
        print(place)

    print()
    print("Recommended Food:")

    for food in foods:
        print("-", food)

    print()
    print("Estimated Cost:", total_cost)
