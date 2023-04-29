# Actor Sensor

Actor Sensor is a module that allows you to detect other actors in the environment based on your own actor's location and field of view. It is built using the CARLA simulator and its Python API.

## Requirements

- CARLA simulator (version 0.9.13)
- Python 3.x
- `carla` Python module (version 0.9.13)

## Installation

1. Download and install the [CARLA simulator](https://carla.org/2021/06/03/release-0.9.11/).
2. Clone or download the `actor_sensor.py` file from this repository.
3. Place the `actor_sensor.py` file in your CARLA Python client directory.

## Usage

1. Import the `actor_sensor` function from `actor_sensor.py`:

```python
from actor_sensor import actor_sensor
