#!/usr/bin/env python
# -*- coding: utf-8 -*-

def greet(name):
    """向指定的名字打招呼"""
    return f"你好，{name}！"

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "世界"
    print(greet(name))