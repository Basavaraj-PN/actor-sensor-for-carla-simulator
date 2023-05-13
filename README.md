# Actor Sensor: FOV sensor

Actor Sensor is a module that allows you to filter other actors in the environment based on your own actor's location and field of view. It is built using the CARLA simulator and its Python API.

## Requirements

- CARLA simulator (version 0.9.13)
- Python 3.x
- `carla` Python module (version 0.9.13)

## Installation

1. Download and install the [CARLA simulator](https://carla.org/2021/06/03/release-0.9.11/).
2. Clone or download the `actor_sensor.py` file from this repository.
3. Place the `actor_sensor.py` file in your CARLA Python client directory.

## Usage

1. `CARLA_EGG_FILE_PATH`: Update this variable to your carla .egg file in `actor_sensor.py`
2. Import the `actor_sensor` function from `actor_sensor.py`:

```python
from actor_sensor import actor_sensor 
```

The `actor_sensor()` function takes the following arguments:

- ego_player_id: The ID of the ego vehicle.
- world: The CARLA world.
- h_fov: The horizontal field of view (in degrees). Default is 45.
- v_fov: The vertical field of view (in degrees). Default is 1.
- show_transform: If set to True, draws lines to show the transforms of the actors within the field of view. Default is False.
- range_: The range (in meters) of the field of view. Default is 50.
- actor_filter: The actor filter to use. Default is 'vehicle.*'.
- Return the array containing filtered actors

## To Run demo example

You need to get ego vehicle actor ID and set `ego_player_id` in `demo.py` accordingly, 
then run example.

```python3 demo.py```

![alt text](https://github.com/Basavaraj-PN/actor-sensor-for-carla-simulator/blob/main/demo_result/demo_result.png)
