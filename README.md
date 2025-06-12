import myfitnesspal
from datetime import timedelta, date


client = myfitnesspal.Client('gqfhcfp7nq@privaterelay.appleid.com', 'G0d!sL0ve9845')

day = client.get_date(2024, 6, 4)

print(day.totals)  # {'calories': 1200, 'carbohydrates': 90, 'fat': 40, 'protein': 130}
print(day.meals)   # You can iterate over meals and entries

start = date(2024, 5, 15)
end = date(2025, 6, 5)

for n in range((end - start).days):
    day = client.get_date(start + timedelta(n))
    print(day.date, day.totals)
