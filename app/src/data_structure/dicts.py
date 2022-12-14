player = {
    "name": "nico",
    "age": 12,
    "alive": True,
    "fav_food": ["🍔", "🍕"]
}

print(player.get("name"))
print(player["age"])
print(player.get("fav_food"))

print(player)
# player.clear()
# print(player)

player["xp"] = 1500
print(player)

player["fav_food"].append("🍜")
print(player.get("fav_food"))
