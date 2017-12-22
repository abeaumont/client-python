from bblfsh.client import BblfshClient
from bblfsh.pyuast import filter, iterator
from bblfsh.aliases import *

class TreeOrder:
    pre_order = 0
    post_order = 1
    level_order = 2

# "in" is a reserved keyword in Python thus can't be used as package name, so
# we import by string

class RoleSearchException(Exception):
    pass


def role_id(role_name):
    try:
        name = DESCRIPTOR.enum_types_by_name["Role"].values_by_name[role_name].number
    except KeyError:
        raise RoleSearchException("Role with name '{}' not found".format(role_name))

    return name


def role_name(role_id):
    try:
        id_ = DESCRIPTOR.enum_types_by_name["Role"].values_by_number[role_id].name
    except KeyError:
        raise RoleSearchException("Role with ID '{}' not found".format(role_id))

    return id_
