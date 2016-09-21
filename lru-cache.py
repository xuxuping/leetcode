#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node(object):

    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None


class DoubleLinkedList(object):

    def __init__(self):
        self.tail = None
        self.head = None

    def is_empty(self):
        return not self.tail

    def remove_last(self):
        self.remove(self.tail)

    def remove(self, node):
        if self.head == self.tail:
            self.head, self.tail = None, None
            return
        if node == self.head:
            node.next.prev == None
            self.head = node.next
            return
        if node == self.tail:
            node.prev.next = None
            self.tail = node.prev
            return
        node.prev.next = node.next
        node.next.prev = node.prev

    def addFirst(self, node):
        if not self.head:
            self.head = self.tail = node
            node.prev = node.next = None
            return
        node.next = self.head
        self.head.prev = node
        self.head = node
        node.prev = None

class LRUCache(object):
	def __init__(self, capacity):
		self.capacity = capacity
		self.size = 0
		self.hashmap = dict()
		self.cache = DoubleLinkedList()

	def get(self, key):

