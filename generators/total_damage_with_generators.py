def events(f):
    "generate events from a file"
    for line in f:
        yield line.split()


def attacks(events):
    "filter a generator of events to only the attacks"
    for e in events:
        if e[0] == "attack":
            yield e


def values(events):
    """given a generator of events, get their values. in the case of
    attacks, the values are how much damage is done, in the case of heals,
    damage is how much damage is healed
    """
    for event in events:
        yield int(event[-1])


def total_damage():
    game_log = open("gamelog.txt")
    game_events = events(game_log)
    game_attacks = attacks(game_events)
    damages = values(game_attacks)
    return sum(damages)


assert total_damage() == 66


# task: write another function, total_damage_to_dragon, that returns
# what it's name suggests. do this by writing another generator to
# "plug in" to the pipeline we've already written

# challenege: use generator pipelines to determine the amount of
# damage done by swords. what about the total change in the fighter's
# hit points over the course of the game?
