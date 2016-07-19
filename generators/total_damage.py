def total_damage():
    """Calculate the total damage done over the course of the whole game
    """
    with open("gamelog.txt") as f:
        damage = 0
        for line in f:
            parts = line.split()
            if parts[0] == "attack":
                damage += int(parts[-1])
    return damage

assert total_damage() == 66
