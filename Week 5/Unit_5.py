def reaction_path(user_input):
    reaction_path_float = user_input * 0.3
    return reaction_path_float


def brake_distance(user_input):
    brake_distance_float = (user_input / 10) * (user_input / 10)
    return brake_distance_float


def stopping_distance(user_input):
    brake = brake_distance(user_input)
    reaction = reaction_path(user_input)
    stopping_distance_float = brake + reaction
    return stopping_distance_float


speed = int(input("Please enter the speed of your car in km/h: "))
print(stopping_distance(speed))
