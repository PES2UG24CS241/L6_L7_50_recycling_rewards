
import math


def parse_collection(text):
    if not isinstance(text, str):
        return None

    parts = text.split(':')

    if len(parts) != 2:
        return None

    material, kg = parts
    material = material.strip()

    if not material:
        return None

    try:
        weight = float(kg.strip())
    except ValueError:
        return None

    if not math.isfinite(weight) or weight < 0:
        return None

    return material.title(), weight


def weight_average(weights_csv):
    if not isinstance(weights_csv, str):
        return None

    values_list = weights_csv.split(',')

    if not values_list or any(not value.strip() for value in values_list):
        return None

    try:
        values = [int(value.strip()) for value in values_list]
    except ValueError:
        return None

    if any(value < 0 for value in values):
        return None

    return sum(values) // len(values)


def net_points(text):
    if not isinstance(text, str):
        return None

    parts = text.split('|')

    if len(parts) != 2:
        return None

    points, penalty = parts

    try:
        points = float(points.strip())
        penalty = float(penalty.strip())
    except ValueError:
        return None

    if not math.isfinite(points) or not math.isfinite(penalty):
        return None

    if points < 0 or penalty < 0:
        return None

    total = points * 2 - penalty

    return max(total, 0)


def main():
    print("==== Running parse_collection ====")
    user_input = input("Enter material:weight in kg (e.g. paper:12): ")
    result = parse_collection(user_input)
    print("Material and Weight:", result)

    print("\n==== Running weight_average ====")
    user_input = input("Enter weights in kg as CSV (e.g. 5,12,20): ")
    result = weight_average(user_input)
    print("Average Weight:", result)

    print("\n==== Running net_points ====")
    user_input = input("Enter points|penalty (e.g. 80|10): ")
    result = net_points(user_input)
    print("Net Points:", result)


if __name__ == "__main__":
    main()
