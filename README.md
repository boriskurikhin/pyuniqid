[![PyPI](https://img.shields.io/pypi/v/pyuniqid)](https://pypi.org/project/pyuniqid) [![PyPI - Downloads](https://img.shields.io/pypi/dm/pyuniqid)](https://pypi.org/project/pyuniqid/#files) [![License](https://img.shields.io/github/license/boriskurikhin/pyuniqid)](https://raw.githubusercontent.com/boriskurikhin/pyuniqid/master/LICENSE)

### A Unique Hexatridecimal ID generator.

Generates unique ids based on the current time, process and machine name.
This package is an adaptation of a widely popular [node module of the same name](https://github.com/adamhalasz/uniqid).

```
pip3 install pyuniqid
```

## Usage

```python3
from pyuniqid import uniqid

print(uniqid()) # -> 4n5pxq24kpiob12og9
```

## Features

- Very fast
- Generates unique id's on multiple processes and machines even if called at the same time.

# How it works

- With the current time the ID's are always unique in a single process.
- With the Process ID the ID's are unique even if called at the same time from multiple processes.
- With the MAC Address the ID's are unique even if called at the same time from multiple machines and processes.

## API:

#### **uniqid(** prefix _optional string_ , suffix _optional string_ **)**

Generate unique ids based on the time, process id and mac address. Works on multiple processes and machines.

```python3
uniqid() -> "4n5pxq24kpiob12og9"
uniqid('hello-') -> "hello-4n5pxq24kpiob12og9"
uniqid('hello-', '-goodbye') -> "hello-4n5pxq24kpiob12og9-goodbye"

# usage with suffix only
uniqid('', '-goodbye') -> "4n5pxq24kpiob12og9-goodbye"
```
## **License**

[MIT License](https://raw.githubusercontent.com/boriskurikhin/pyuniqid/master/LICENSE)
