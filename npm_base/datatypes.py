from typing import Union
import numpy as np
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float
    z: float


@dataclass
class Quaternion:
    x: float
    y: float
    z: float
    w: float


@dataclass
class Pose:
    position: Point
    orientation: Union[Quaternion, Point]


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
