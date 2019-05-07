#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: cylisery@outlook.com


# depth first search
# return True if value is found, else False
def dfs(node, val):
    stack = [node]
    visited = []

    while len(stack) != 0:
        item = stack.pop()
        print "%s -> " % item.val
        if item.val == val:
            return True

        visited.append(item)
        for subitem in item.connections:
            if subitem not in visited and subitem not in stack:
                stack.append(subitem)

    return False
