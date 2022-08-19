"""
This file contains the classes TaxonomyTree and TaxonomyNode

@Author Aneel Biswas
@Version 0.1
@Date 2022Aug19
"""

from __future__ import annotations


class TaxonomyTree:

    elements = {}
    roots = {}

    def __init__(self):
        self.elements = {}
        self.roots = {}

    def add_node(self, name, parent):
        if name not in self.elements:
            new_node = TaxonomyNode(name, parent)
            if parent not in self.elements:
                self.roots[name] = new_node
                self.elements[name] = new_node
            else:
                self.elements[parent].add_child(new_node)
                self.elements[name] = new_node


class TaxonomyNode:

    name = ''
    parent = ''
    children = {}

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def add_child(self, child):
        self.children[child.name] = child

    def __str__(self):
        if not self.children:
            return '{\n' + self.name + '\n}'
        return '{\n' + self.name + ':\n' + ",\n".join(self.children) + '\n}'
