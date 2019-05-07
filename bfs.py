#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: cylisery@outlook.com


# breadth first search
# return True if value is found, else False
def bfs(node, val):
    q = [node]

    for item in q:
        print "%s -> " % item.val
        if item.val == val:
            return True

        for subitem in item.connections:
            if subitem not in q:
                q.append(subitem)

    return False
