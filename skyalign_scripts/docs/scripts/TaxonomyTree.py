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

    def __init__(self, elements={}, roots={}):
        self.elements = elements
        self.roots = roots

    def add_node(self, name, parent):
        if name not in self.elements:
            new_node = TaxonomyNode(name, parent)
            if parent not in self.elements:
                new_node.depth = 0
                self.roots[name] = new_node
                self.elements[name] = new_node
            else:
                self.elements[parent].add_child(new_node)
                self.elements[name] = new_node
                new_node.depth = new_node.parent.depth + 1

    def __str__(self):
        if len(self.elements) == 1:
            name, node = self.roots.items()
            return node[0].name
        return '{\n' + \
               ';\n'.join(['\t' + root + ': {\n' + self.elements[root].name + str(self.elements[root].children.keys()) + '\n}' for root in self.roots])\
               + '\n}'

class TaxonomyNode:

    name = ''
    parent = ''
    children = {}
    depth = 0


    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def add_child(self, child):
        self.children[child.name] = child

    def to_tree(self) -> TaxonomyTree:
        including_self = self.children.copy()
        including_self[self.name] = self
        return TaxonomyTree(elements=including_self, roots={self.name: self})

    def __str__(self):
        if not self.children:
            return self.name
        return str(self.to_tree())

    @property
    def num_of_members(self):
        return len(self.children)
