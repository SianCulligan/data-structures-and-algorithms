# Code Challenge: Class 05: Linked List Implementation



## Singly Linked List
<!-- Short summary or background information -->

## Challenge
<!-- Description of the challenge -->
- Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
- Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
- Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
- Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
- Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- Insert: o(1), no matter the length, we just re-assign the head of the node to the new value and change the pointer to look at the old head value
- Includes: o(n), the more values the more the function needs to loop to find the passed value
- To String: o(n), the more values the more the function needs to loop to print values

## API
<!-- Description of each method publicly available to your Linked List -->
- n/a


[Linked List Resource](https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm)