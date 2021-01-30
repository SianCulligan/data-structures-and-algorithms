# Trees
<!-- Short summary or background information -->
Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge.

## Challenge
<!-- Description of the challenge -->
- *Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.*
- *Create a BinaryTree class*
- Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.
- *Create a BinarySearchTree class*
- Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
- Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- Traversal methods: o(n), no mater what method is chosen, the function will always need to traverse all nodes in the tree
- Add & contains: o(n), I'm not sure on this one, but I figure worst case, it would need to traverse all nodes and either add a leaf at the bottom of the tree or return the value

[Open PR](https://github.com/SianCulligan/python-data-structures-and-algorithms/pull/17)