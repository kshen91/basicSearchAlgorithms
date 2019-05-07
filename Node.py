#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: cylisery@outlook.com


class Node():

    def __init__(self, val):
        self.val = val
        self.connections = []

    def connect(self, node):
        self.connections.append(node)

    def disconnect(self, node):
        if node in self.connections:
            self.connections.remove(node)
        else:
            print "Node is not connected, please verify"
