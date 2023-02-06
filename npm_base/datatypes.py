from dataclasses import dataclass
from typing import Union

import numpy as np


@dataclass
class Point:
    x: float
    y: float
    z: float

    def tolist(self):
        return [self.x, self.y, self.z]


@dataclass
class Quaternion:
    x: float
    y: float
    z: float
    w: float

    def tolist(self):
        return [self.x, self.y, self.z, self.w]


@dataclass
class Pose:
    position: Point
    orientation: Union[Quaternion, Point]

    def tolist(self, flatten=False):
        ls = [self.position.tolist(), self.orientation.tolist()]
        if flatten:
            return [item for sublist in ls for item in sublist]
        return ls

    def tonode(self):
        from .utils import convert_orientation  # to avoid circular import
        ori = convert_orientation(self.orientation, euler=True)
        return Node(x=self.position.x, y=self.position.y, theta=ori.z)


@dataclass
class Velocity:
    linear: Point
    angular: Point

    def tolist(self):
        return [self.linear.tolist(), self.angular.tolist()]


@dataclass
class Effort:
    force: Point
    torque: Point

    def tolist(self):
        return [self.force.tolist(), self.torque.tolist()]


@dataclass
class JointLimits:
    angle: np.ndarray
    velocity: np.ndarray
    torque: np.ndarray
    acceleration: np.ndarray
    jerk: np.ndarray


@dataclass
class Node:
    x: float
    y: float
    theta: float  # radians

    def totuple(self):
        return self.x, self.y, self.theta

    def tolist(self):
        return [self.x, self.y, self.theta]

    def topose(self, z, euler):
        from .utils import convert_orientation  # to avoid circular import
        return Pose(position=Point(x=self.x, y=self.y, z=z),
                    orientation=convert_orientation(Point(x=0, y=0, z=self.theta), euler=euler))

    def distance(self, other):
        # only calculates positional distance
        return np.linalg.norm(np.array(self.totuple()[:2]) - np.array(other.totuple()[:2]))

