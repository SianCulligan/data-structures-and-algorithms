


# Challenge Summary
<!-- Short summary or background information -->
- Create a brand new PseudoQueue class. Do not use an existing Queue. Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below), but will internally only utilize 2 Stack objects. Ensure that you create your class with the following methods:

- The Stack instances have only push, pop, and peek methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.

## Challenge Description
<!-- Description of the challenge -->
Write 2 methods: 
- enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.
- dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- Enqueue: o(1) - will only ever reassign the front, regardless of queue length
- Dequeue: o(n) - needs to find the last item in the queue to dequeue, will always need to traverse the nodes. 

## Solution

[Whiteboard Solution](assets/queues2.png)