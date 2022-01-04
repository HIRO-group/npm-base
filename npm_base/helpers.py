import pdb

import pybullet as pb
from .datatypes import Point, Quaternion
import dataclasses as dc


def convert_orientation(orientation, euler):
    if (type(orientation) == Point and euler) or (type(orientation) == Quaternion and not euler):
        return orientation
    elif type(orientation) == Point:
        return Quaternion(*pb.getQuaternionFromEuler(dc.astuple(orientation)))
    elif type(orientation) == Quaternion:
        return Point(*pb.getEulerFromQuaternion(dc.astuple(orientation)))
