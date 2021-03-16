# Hashtables
<!-- Short summary or background information -->
- Implement a Hashtable

## Challenge
<!-- Description of the challenge -->
- The  Hashtable with the following methods:
 - ADD: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
 - GET: takes in the key and returns the value from the table.
 - CONTAINS: takes in the key and returns a boolean, indicating if the key exists in the table already.
 - HASH: Takes in an arbitrary key and returns an index in the collection.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
 - Hashtables generally have a big o of 'o(1)', unless there are multiple values at an index, in which case it moves to a o(n) at the worst case scenario

