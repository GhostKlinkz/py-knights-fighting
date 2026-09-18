def prepare_knight(knight):
    knight["protection"] = sum(
        armour["protection"] for armour in knight["armour"]
    )

    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        for stat, value in knight["potion"]["effect"].items():
            knight[stat] += value


def fight(knight_1, knight_2):
    knight_1["hp"] -= knight_2["power"] - knight_1["protection"]
    knight_2["hp"] -= knight_1["power"] - knight_2["protection"]

    knight_1["hp"] = max(knight_1["hp"], 0)
    knight_2["hp"] = max(knight_2["hp"], 0)


def battle(knightsConfig):
    for knight in knightsConfig.values():
        prepare_knight(knight)

    fight(
        knightsConfig["lancelot"],
        knightsConfig["mordred"],
    )

    fight(
        knightsConfig["arthur"],
        knightsConfig["red_knight"],
    )

    return {
        knight["name"]: knight["hp"]
        for knight in knightsConfig.values()
    }
