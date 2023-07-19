"""This is a random file that is used for testing"""
<<<<<<< HEAD
from tensorflow.python.client import device_lib


print(device_lib.list_local_devices())
=======
import Tiles

tile = Tiles.DesignGoalTile(23, "Nahala")

if isinstance(tile, Tiles.DesignGoalTile):
    print("Design")
else:
    print("Normal")

>>>>>>> 9547a0e8ec4ef8f4222379a007778205e058e264


