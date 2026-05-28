from knowledge_base import budget_data

def estimate_cost(level, days):
    daily_budget = budget_data.get(level, 5000)

    total_cost = daily_budget * days

    return total_cost
