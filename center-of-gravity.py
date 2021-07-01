import math


def get_lift_height():
    """Get lift height from user input in mm"""
    return abs(float(input("Please enter the lift height in mm: ")))


def get_left_wheelbase():
    """Get left wheelbase from user input in mm."""
    return abs(float(input("Please enter the left wheelbase in mm: ")))


def get_right_wheelbase():
    """Get right wheelbase from user input in mm."""
    return abs(float(input("Please enter the right wheelbase in mm: ")))


def get_mean_wheelbase(left_wheelbase, right_wheelbase):
    """Return mean wheelbase from vehicle's left and right wheelbases in mm.

    Arguments:
    left_wheelbase -- vehicle's left wheelbase in mm.
    right_wheelbase -- vehicle's right wheelbase in mm.
    Return values:
    The mean vehicle wheelbase.
    """
    return (left_wheelbase + right_wheelbase) / 2


def get_rear_track():
    """Return vehicle rear track from user input in mm."""
    return abs(float(input("Please enter vehicle rear track in mm: ")))


def get_front_track():
    """Return vehicle front track from user input in mm."""
    return abs(float(input("Please enter vehicle front track in mm: ")))


def get_wheel_diameter():
    """Get lifted vehicle wheel diameter from user input in mm."""
    return abs(float(input("Please enter lifted vehicle wheel diameter in mm: ")))


def get_flattened_wheel_diameter():
    """Get lifted vehicle flattened wheel diameter from user input in mm."""
    return abs(float(input("Please enter lifted vehicle flattened wheel diameter in mm: ")))


def get_static_wheel_radius(wheel_diameter, flattened_wheel_diameter):
    """Return static wheel radius.

    Arguments:
    wheel_diameter -- lifted vehicle wheel_diameter in mm
    flattened_wheel_diameter -- lifted vehicle flattened_wheel_diameter in mm
    Return values:
    The static wheel radius in mm.
    """
    return flattened_wheel_diameter - (wheel_diameter / 2)


def get_rear_left_wheel_mass():
    """Get rear left wheel mass from user input in kg."""
    return abs(float(input("Please enter the rear left wheel mass in kg: ")))


def get_rear_right_wheel_mass():
    """Get rear right wheel mass from user input in kg."""
    return abs(float(input("Please enter the rear right wheel mass in kg: ")))


def get_front_left_wheel_mass():
    """Get front left wheel mass from user input in kg."""
    return abs(float(input("Please enter the front left wheel mass in kg: ")))


def get_front_right_wheel_mass():
    """Get front right wheel mass from user input in kg."""
    return abs(float(input("Please enter the front right wheel mass in kg: ")))


def get_rear_axle_mass(rear_left, rear_right):
    """Return rear axle mass from wheel masses in kg.

    Arguments:
    rear_left -- rear left wheel mass in kg.
    rear_right -- rear right wheel mass in kg.
    """
    return rear_left + rear_right


def get_front_axle_mass(front_left, front_right):
    """Return front axle mass form wheel masses in kg.

    Arguments:
    front_left -- front left wheel mass in kg.
    front_right -- front right wheel mass in kg.
    Return values:
    The frontal axle mass in kg.
    """
    return front_left + front_right


def get_vehicle_mass(rear_axle_mass, front_axle_mass):
    """Return vehicle mass from wheel masses in kg.

    Arguments:
    rear_axle_mass -- vehicle rear axle mass in kg.
    front_axle_mass -- vehicle front axle mass in kg.
    Return values:
    The total vehicle mass in kg.
    """
    return rear_axle_mass + front_axle_mass


def get_lifted_angle(lift_height, mean_wheelbase):
    """Return lifted angle from vehicle lift height and mean wheelbase.

    Arguments:
    lift_height -- lift height in mm.
    mean_wheelbase -- mean wheelbase in mm.
    Return values:
    The lifted angle in radians.
    """
    return math.atan(lift_height / mean_wheelbase)


def get_lifted_rear_left_wheel_mass():
    """Get lifted rear left wheel mass from user input in kg."""
    return abs(float(input("Please enter the lifted rear left wheel mass in kg: ")))


def get_lifted_rear_right_wheel_mass():
    """Get lifted rear right wheel mass from user input in kg."""
    return abs(float(input("Please enter the lifted rear right wheel mass in kg: ")))


def get_lifted_rear_axle_mass(lifted_rear_left_wheel_mass, lifted_rear_right_wheel_mass):
    """Return rear axle mass from wheel masses in kg.

    Arguments:
    rear_left -- rear left wheel mass in kg.
    rear_right -- rear right wheel mass in kg.
    """
    return lifted_rear_left_wheel_mass + lifted_rear_right_wheel_mass


def get_longitudinal_distance(vehicle_mass, rear_axle_mass, mean_wheelbase):
    """Return longitudinal distance in mm.

    Arguments:
    vehicle_mass -- vehicle total mass in kg..
    rear_axle_mass -- rear axle mass in kg.
    mean_wheelbase -- mean wheelbase in mm.
    Return values:
    The longitudinal distance of the center of gravity in mm.
    """
    return rear_axle_mass / vehicle_mass + mean_wheelbase


def get_transverse_distance(front_track, rear_track, rear_right_mass,
                            rear_left_mass, front_left_mass, front_right_mass, vehicle_mass):
    """Return transverse distance in mm.

    Arguments:
    front_track -- front track in mm.
    rear_track -- rear track in .
    rear_right_mass -- rear right wheel mass in kg.
    rear_left_mass -- rear left wheel mass in kg.
    front_left_mass -- front left wheel mass in kg.
    front_right_mass -- front right wheel mass in kg.
    vehicle_mass -- total vehicle mass in kg.
    Return values:
    The transverse distance of the center of gravity in mm.
    """
    return ((front_track * (front_left_mass - front_right_mass))
            + (rear_track * (rear_left_mass - rear_right_mass))) / (2 * vehicle_mass)


def get_height(mean_wheelbase, lifted_rear_axle_mass, rear_axle_mass, vehicle_mass, lifted_angle, static_wheel_radius):
    """Return height of the center of gravity in mm.

    Arguments:

    Return values:
    The height of the center of gravity in mm.
    """
    return ((mean_wheelbase * (lifted_rear_axle_mass - rear_axle_mass))
            / (vehicle_mass * math.tan(lifted_angle))) + static_wheel_radius


def get_center_of_gravity(vehicle_mass, rear_axle_mass, mean_wheelbase, front_track,
                          rear_track, rear_right_mass, rear_left_mass, front_left_mass,
                          front_right_mass, lifted_rear_axle_mass, lifted_angle, static_wheel_radius):
    """Return a vehicle's center of gravity.

    Argument:
    longitudinal_distance -- the longitudinal distance of the center of gravity.
    transverse_distance -- the transverse distance of the center of gravity.
    height -- the height of the center of gravity.
    Return values:
    A tuple made up from the XYZ coordinates of the center of gravity in mm.
    """
    longitudinal_distance = get_longitudinal_distance(vehicle_mass, rear_axle_mass, mean_wheelbase)
    transverse_distance = get_transverse_distance(front_track, rear_track, rear_right_mass,
                                                  rear_left_mass, front_left_mass, front_right_mass, vehicle_mass)
    height = get_height(mean_wheelbase, lifted_rear_axle_mass, rear_axle_mass,
                        vehicle_mass, lifted_angle, static_wheel_radius)

    return longitudinal_distance, transverse_distance, height


def main():
    lift_height = get_lift_height()

    left_wheelbase = get_left_wheelbase()
    right_wheelbase = get_right_wheelbase()
    mean_wheelbase = get_mean_wheelbase(left_wheelbase, right_wheelbase)

    rear_track = get_rear_track()
    front_track = get_front_track()

    wheel_diameter = get_wheel_diameter()
    flattened_wheel_diameter = get_flattened_wheel_diameter()
    static_wheel_radius = get_static_wheel_radius(wheel_diameter, flattened_wheel_diameter)

    rear_left_wheel_mass = get_rear_left_wheel_mass()
    rear_right_wheel_mass = get_rear_right_wheel_mass()
    front_left_wheel_mass = get_front_left_wheel_mass()
    front_right_wheel_mass = get_front_right_wheel_mass()
    rear_axle_mass = get_rear_axle_mass(rear_left_wheel_mass, rear_right_wheel_mass)
    front_axle_mass = get_front_axle_mass(front_left_wheel_mass, front_right_wheel_mass)
    vehicle_mass = get_vehicle_mass(rear_axle_mass, front_axle_mass)
    lifted_rear_left_wheel_mass = get_lifted_rear_left_wheel_mass()
    lifted_rear_right_wheel_mass = get_lifted_rear_right_wheel_mass()
    lifted_rear_axle_mass = get_lifted_rear_axle_mass(lifted_rear_left_wheel_mass, lifted_rear_right_wheel_mass)

    lifted_angle = get_lifted_angle(lift_height, mean_wheelbase)

    center_of_gravity = get_center_of_gravity(vehicle_mass, rear_axle_mass, mean_wheelbase, front_track, rear_track,
                                              rear_right_wheel_mass, rear_left_wheel_mass, front_left_wheel_mass,
                                              front_right_wheel_mass, lifted_rear_axle_mass, lifted_angle,
                                              static_wheel_radius)

    print(center_of_gravity)


if __name__ == '__main__':
    main()
