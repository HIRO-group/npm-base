import dataclasses as dc
import json

import numpy as np
import pybullet as pb
import transformations
import yaml

from .datatypes import Pose, Point
from .datatypes import Quaternion


def load_yaml(filepath):
    with open(filepath, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


def write_yaml(filepath, data):
    with open(filepath, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)


def load_json(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data


def write_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)


def load_txt(filepath):
    with open(filepath, 'r') as f:
        data = f.read()
    return data


def write_txt(filepath, data):
    with open(filepath, 'w') as f:
        f.write(data)


def convert_orientation(orientation, euler):
    if (type(orientation) == Point and euler) or (type(orientation) == Quaternion and not euler):
        return orientation
    elif type(orientation) == Point and not euler:
        return Quaternion(*pb.getQuaternionFromEuler(orientation.tolist()))
    elif type(orientation) == Quaternion and euler:
        return Point(*pb.getEulerFromQuaternion(orientation.tolist()))


def pose_to_mat(pose):
    orientation = convert_orientation(pose.orientation, euler=True)
    return transformations.compose_matrix(angles=dc.astuple(orientation), translate=dc.astuple(pose.position))


def mat_to_pose(mat, euler=False):
    _, _, orientation, position, _ = transformations.decompose_matrix(mat)
    return Pose(position=Point(*position), orientation=convert_orientation(Point(*orientation), euler=euler))


def node_distance(node1, node2):
    """
    node* = (x, y, theta_degrees)
    """

    assert type(node1) == type(node2) == tuple

    xy_dist = np.linalg.norm(np.array(node1[:2]) - np.array(node2[:2]))

    # https://www.intmath.com/analytic-trigonometry/2-sum-difference-angles.php
    ang1 = np.deg2rad(node1[2])
    ang2 = np.deg2rad(node2[2])
    theta_dist = np.rad2deg(np.arccos(np.cos(ang1) * np.cos(ang2) + np.sin(ang1) * np.sin(ang2)))

    return xy_dist, theta_dist


def is_within_radius(node1, node2, radius):
    """
    node* = (x, y, theta_degrees)
    radius = ([meters], [degrees])
    """

    assert type(node1) == type(node2) == tuple
    assert type(radius) == tuple

    xy_dist, theta_dist = node_distance(node1, node2)

    return xy_dist <= radius and theta_dist <= radius


def pos_is_similar(orig_pos, current_pose, threshold):
    """
    tells if two points or vectors are similar
    @param orig_pos [list or np.ndarray]
    @param current_pose [list or np.ndarray]

    @return bool
    """
    if type(orig_pos) is not np.ndarray:
        orig_pos = np.array(orig_pos[0])
    if type(current_pose) is not np.ndarray:
        current_pose = np.array(current_pose[0])
    dist = np.linalg.norm(orig_pos - current_pose)
    return dist <= threshold
