"""Unique ID module.

Consists of the unique id generator, and necessary but hidden
utility functions.

  Typical usage example:

  # Simple.
  uniqid()

  # With a prefix.
  uniqid('hello-')

  # With a prefix and a postfix.
  uniqid('hello-', '-goodbye')

  # With only a postfix.
  uniqid('', '-goodbye')
"""

import os
import time
import netifaces
from numpy import base_repr


def __get_pid():
    return os.getpid()


def __get_netifaces():
    """Retrieves an appropriate MAC address.

    Returns:
        A string containing the MAC address.
    """

    network_interfaces = netifaces.interfaces()
    for ni in network_interfaces:
        nif = netifaces.ifaddresses(ni)
        if ni == 'lo' or netifaces.AF_LINK not in nif:
            continue
        return netifaces.ifaddresses(ni)[netifaces.AF_LINK][0]['addr']
    return '0'


def __get_mac():
    """Returns MAC address as an integer.

    Strips all non-integer characters from the MAC address and returns the
    result.

    Returns:
        Integer version of the MAC address.
    """

    mac = __get_netifaces()
    return int(''.join(list(filter(lambda x: x.isdigit(), list(mac)))))


def __get_time():
    return int(time.time() * 1000)


def __tob36(item):
    """Converts an item to base 36.

    Args:
        item: The item to convert, ideally integer.

    Returns:
        The item converted into base 36 format.
    """

    item_int = int(item)
    return base_repr(item_int, 36)


def uniqid(prefix='', postfix=''):
    """Generates a unique id.

    Combination of MAC address, process ID and time to generate a unique id.

    Args:
        prefix: Optional string prefix for the ID, appearing at the beginning.
        postfix: Optional string postfix for the ID, appearing at the end.

    Returns:
        A unique ID, as a string.
    """

    return ''.join([
        prefix,
        __tob36(__get_mac()),
        __tob36(__get_pid()),
        __tob36(__get_time()),
        postfix
    ]).lower()
