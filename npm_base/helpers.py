import dataclasses as dc

import pybullet as pb
import transformations

from .datatypes import Pose, Point
from .datatypes import Quaternion


def convert_orientation(orientation, euler):
    if (type(orientation) == Point and euler) or (type(orientation) == Quaternion and not euler):
        return orientation
    elif type(orientation) == Point:
        return Quaternion(*pb.getQuaternionFromEuler(dc.astuple(orientation)))
    elif type(orientation) == Quaternion:
        return Point(*pb.getEulerFromQuaternion(dc.astuple(orientation)))


def pose_to_mat(pose):
    orientation = convert_orientation(pose.orientation, euler=True)
    return transformations.compose_matrix(angles=dc.astuple(orientation), translate=dc.astuple(pose.position))


def mat_to_pose(mat, euler=False):
    _, _, orientation, position, _ = transformations.decompose_matrix(mat)
    return Pose(position=Point(*position), orientation=convert_orientation(Point(*orientation), euler=euler))
