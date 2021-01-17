# Challenge Summary
<!-- Short summary or background information -->
- Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.

## Challenge Description
<!-- Description of the challenge -->
Implement the following methods:

- enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
- dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- enqueue: o(1), always adding a new node onto the front no matter the length of the queue
- dequeue: o(n), queue needs to be traversed

## Solution
<!-- Embedded whiteboard image -->
[Whiteboard](assets/fifoas.png)

[Resource on inheritance](https://www.dummies.com/programming/python/how-to-extend-classes-to-make-new-classes-in-python/)

[Testing Resource](https://www.dummies.com/programming/python/how-to-extend-classes-to-make-new-classes-in-python/)
