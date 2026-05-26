import random


NUMBER_OF_PARKING_LOTS = 100
TERMINAL_COSTS = 200
FREE_PARKING_LOT_PROBABILITY = 0.05


def costs(parking_lot: int) -> int:
    """Calculate the costs if the agent chooses a specific parking lot"""
    if parking_lot == 0:
        return TERMINAL_COSTS
    return parking_lot


def is_parking_lot_free() -> bool:
    """Calculate if a parking lot is free given a specific probability"""
    return random.random() <= FREE_PARKING_LOT_PROBABILITY


def main():
    random.seed(1)

    for parking_lot in reversed(range(NUMBER_OF_PARKING_LOTS + 1)):
        if parking_lot == 0:
            print(f"{parking_lot}: No parking spot was chosen; driving to expensive garage")
        elif is_parking_lot_free():
            print(f"{parking_lot}: parking lot is free; deciding what to do")
        else:
            print(f"{parking_lot}: parking lot is occupied; driving to next parking lot")


if __name__ == "__main__":
    main()
