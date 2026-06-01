import pandas as pd
import random

# Vegetables
vegetables = [
    "Tomato",
    "Potato",
    "Onion",
    "Ladyfinger",
    "Brinjal",
    "Carrot",
    "Cabbage",
    "Cauliflower",
    "Spinach",
    "Peas",
    "Cucumber",
    "Pumpkin",
    "Beans",
    "Capsicum",
    "Radish",
    "Bottle Gourd",
    "Bitter Gourd"
]

# Seasons
seasons = [
    "Winter",
    "Summer",
    "Monsoon",
    "Spring"
]

# Condition
conditions = [
    "Poor",
    "Average",
    "Good"
]

# Base prices
base_prices = {
    "Tomato": 40,
    "Potato": 25,
    "Onion": 35,
    "Ladyfinger": 50,
    "Brinjal": 30,
    "Carrot": 45,
    "Cabbage": 20,
    "Cauliflower": 35,
    "Spinach": 25,
    "Peas": 60,
    "Cucumber": 30,
    "Pumpkin": 28,
    "Beans": 70,
    "Capsicum": 80,
    "Radish": 22,
    "Bottle Gourd": 30,
    "Bitter Gourd": 55
}

data = []

# Generate 500 rows
for _ in range(500):

    vegetable = random.choice(vegetables)
    season = random.choice(seasons)

    month = random.randint(1, 12)
    temp = random.randint(10, 45)

    disaster = random.choice([0, 1])

    condition = random.choice(conditions)

    price = base_prices[vegetable]

    # Temperature effect
    if temp > 35:
        price += random.randint(5, 20)

    # Disaster effect
    if disaster == 1:
        price += random.randint(20, 80)

    # Quality effect
    if condition == "Poor":
        price -= random.randint(5, 15)

    elif condition == "Good":
        price += random.randint(5, 20)

    # Random fluctuation
    price += random.randint(-5, 10)

    price = max(10, price)

    data.append([
        vegetable,
        season,
        month,
        temp,
        disaster,
        condition,
        price
    ])

# Create DataFrame
df = pd.DataFrame(
    data,
    columns=[
        "Vegetable",
        "Season",
        "Month",
        "Temp",
        "Disaster",
        "Condition",
        "Price_per_kg"
    ]
)

# Save CSV
df.to_csv("vegetable_market_500.csv", index=False)

print("✅ Dataset created successfully!")
print("📁 File saved as: vegetable_market_500.csv")
print(f"📊 Total rows: {len(df)}")