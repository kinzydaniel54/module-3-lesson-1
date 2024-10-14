restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Soda": 2.75, "Beer": 7.50}
restaurant_menu["Main Course"].update({"Steak": 17.99})
restaurant_menu["Starters"].pop("Bruschetta")

for key, value in restaurant_menu.items():
    print("-" * 50)
    print(key, value)
    print("-" * 50) 
