import json
# Load knowledge base
with open("places.json", "r") as file:
    places = json.load(file)
print("\n========== AI TRAVEL PLANNER ==========\n")
print("Choose Travel Type:")
print("1. Beach")
print("2. Mountain")
print("3. City")
choice = input("\nEnter your choice: ")
# User preference
if choice == "1":
    preference = "Beach"
elif choice == "2":
    preference = "Mountain"
else:
    preference = "City"
# Budget input
budget = int(input("Enter your budget: "))
print("\n========== RECOMMENDED PLACES ==========\n")
found = False
for place in places:
    if place["type"] == preference and place["budget"] <= budget:
        found = True
        print("Place :", place["name"])
        print("Type  :", place["type"])
        print("Budget:", place["budget"])
        print("Food  :", place["food"])
        print("--------------------------------")
if not found:
    print("No places found within your budget.")