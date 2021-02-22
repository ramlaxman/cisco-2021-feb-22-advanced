#!/usr/bin/env python3

def hello(name: str) -> str:   # type hint or type annotation
    return f'Hello, {name}!'

print(hello('world'))
print(hello(5))
s = hello(