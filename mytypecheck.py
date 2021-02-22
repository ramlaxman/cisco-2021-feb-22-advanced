#!/usr/bin/env python3

from typing import Sequence, Any


def hello(name: str) -> str:   # type hint or type annotation
    return f'Hello, {name}!'


print(hello('world'))
# print(hello(5))
s = hello('world')
# print(s + 3)


def firstlast(data: Sequence[Any]) -> Any:
    return data[:1] + data[-1:]


print(firstlast('abcde'))
print(firstlast([10, 20, 30, 40, 50]))
print(firstlast((100, 200, 300)))
