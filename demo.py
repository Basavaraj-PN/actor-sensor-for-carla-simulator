from actor_sensor import actor_sensor
import carla

# Connect to the CARLA simulator
client = carla.Client('localhost', 2000)
client.set_timeout(2.0)
world = client.get_world()

ego_player_id = SET_THIS_TO_EGO_ID 

while True:
    filtered_actors = actor_sensor(ego_player_id=ego_player_id, world=world,
                                   h_fov=45, v_fov=5, show_transform=True, range_=30, actor_filter='vehicle.*')
    for actor in filtered_actors:
        print(world.get_actor(actor.id).get_transform())
