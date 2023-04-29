
from math import degrees, acos, sqrt
import carla
import sys

CARLA_EGG_FILE_PATH = "/home/user_name/CARLA_0.9.13/PythonAPI/carla/dist/carla-0.9.13-py3.7-linux-x86_64.egg"
try:
    sys.path.append(CARLA_EGG_FILE_PATH)
except IndexError:
    pass


def clamp(min_v, max_v, value):
    """
    Helper function to clamp a value between a minimum and maximum value.
    """
    return max(min_v, min(value, max_v))


def draw_transform(debug, trans1, trans2, col=carla.Color(0, 255, 0), lt=0.2):
    """
    Helper function to draw a line between two transforms.
    """
    debug.draw_line(
        trans1.location, trans1.location + trans2.location,
        thickness=0.08, color=col, life_time=lt)


def actor_sensor(ego_player_id, world, h_fov=45, v_fov=1, show_transform=False, range_=50, actor_filter='vehicle.*'):
    """
    Returns a list of actors filtered based on the given parameters.

    ego_player_id: the ID of the ego vehicle actor
    world: the Carla world object
    hFov: horizontal field of view in degrees
    vFov: vertical field of view in degrees
    show_transform: whether or not to draw a line between the ego vehicle and the filtered actors
    range_: the maximum range for filtering actors
    filter: the filter string for the actor types to be filtered

    """
    filtered_actors = []
    ego_actor = world.get_actor(ego_player_id)

    if not ego_actor:
        print(
            f"Error: Unable to retrieve ego actor with ID {ego_player_id}. Please set a correct ego ID.")
        return []

    ego_transform = ego_actor.get_transform()
    # Get all actors in the world that match the filter
    actors = world.get_actors().filter(actor_filter)

    # Define helper function to calculate distance between two locations
    def distance(l):
        return sqrt((l.x - ego_transform.location.x) ** 2 + (l.y - ego_transform.location.y) ** 2 + (l.z - ego_transform.location.z) ** 2)
    # Loop through all actors
    for actor in actors:
        # Ignore the ego vehicle
        if actor.id != ego_player_id:
            # Get the vector between the ego vehicle and current actor
            ego_to_actor_transform = actor.get_transform().location - ego_transform.location
            # Calculate the dot product between the forward vector of ego vehicle and the vector between ego vehicle and actor
            dot_projection = round(
                ego_transform.get_forward_vector().dot(ego_to_actor_transform), 2)
            # Calculate the dot product between the up vector of ego vehicle and the vector between ego vehicle and actor

            h_dot_projection2 = round(
                ego_transform.get_up_vector().dot(ego_to_actor_transform), 2)

            try:
                # Calculate the angle between the forward vector of ego vehicle and the vector between ego vehicle and actor
                angle_between_vectors = degrees(acos(
                    clamp(-1, 1, dot_projection / round(carla.Vector3D(ego_to_actor_transform).length(), 2))))
                # Calculate the angle between the up vector of ego vehicle and the vector between ego vehicle and actor

                angle_h_dot_projection2 = degrees(acos(
                    clamp(-1, 1, h_dot_projection2 / round(carla.Vector3D(ego_to_actor_transform).length(), 2))))
                # Check if the actor is within the FOV and range of the ego vehicle
                if angle_between_vectors <= h_fov + 0.01 and distance(actor.get_transform().location) <= range_ + 0.001 and abs(90 - angle_h_dot_projection2) <= v_fov + 0.001:
                    filtered_actors.append(actor)
                    # Draw transformation between ego and actor
                    if show_transform:
                        draw_transform(world.debug, ego_transform,
                                       carla.Transform(ego_to_actor_transform))

            except ZeroDivisionError:
                print("ZeroDivisionError")

    return filtered_actors
