
""" This program creates a queue, which works on a first-in, first-out (FIFO) basis.
This program manages a ticket line and serves each person in first-come, first-served order until the queue is empty."""

"""Homework:
Task: Manage a line of people buying tickets.         class Queue: and ticket_queue = Queue()
Setup: A queue of people ["Alice", "Bob", "Charlie"].  ticket_queue.enqueue("Alice") 
                                                       ticket_queue.enqueue("Bob")"""

"""Goal: Show the order in which people are served.
Logic (Give If Needed):
New Arrival: A new person ("David") joins the line. Add them to the queue.   ticket_queue.enqueue("David")"""
"""Serve: The person at the front buys a ticket and leaves.                     person = ticket_queue.dequeue()
Remove them from the queue                                                   return self.queue.pop(0)
and print "[Name] bought a ticket."                                          print(person, "bought a ticket.")"""
"""Repeat until the line is empty.                                              while not ticket_queue.is_empty():

"""

class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, person):
        self.queue.append(person)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.queue.pop(0)

ticket_queue = Queue()

ticket_queue.enqueue("Alice")
ticket_queue.enqueue("Bob")
ticket_queue.enqueue("Charlie")

ticket_queue.enqueue("David")

while not ticket_queue.is_empty():
    person = ticket_queue.dequeue()

    print(person, "bought a ticket.")
