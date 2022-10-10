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

    def tolist(self):
        return [self.position.tolist(), self.orientation.tolist()]


@dataclass
class Velocity:
    linear: Point
    angular: Point


@dataclass
class Effort:
    force: Point
    torque: Point


@dataclass
class JointLimits:
    angle: np.ndarray
    velocity: np.ndarray
    effort: np.ndarray


@dataclass
class Node:
    x: float
    y: float
    theta: float

    def totuple(self):
        return self.x, self.y, self.theta
