### A Unique Hexatridecimal ID generator.

It will always create unique id's based on the current time, process and machine name.
This package is a copy of a widely popular Node module of the same name.

```
pip3 install pyuniqid
```

## Usage

```python3
from pyuniqid import uniqid

print(uniqid()) # -> 17ps24e9kgckbv6a3e4
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

// usage with suffix only
uniqid('', '-goodbye') -> "4n5pxq24kpiob12og9-goodbye"
```

## **License**

(The MIT License)

Copyright (c) 2020 [Boris Skurikhin](http://boriskurikhin.github.io) <boriskurikhin@gmail.com> 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
