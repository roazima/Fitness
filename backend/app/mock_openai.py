

def parse_food_input(text: str) -> dict:
    # This is fake logic, we are pretending this is the result of GPT
    if "chicken" in text:
        return {
            "food": "chicken",
            "weight": 50,
            "unit": "g",
            "macros": {"protein": 11, "carbs": 0, "fat": 1}
        }
    return {}
