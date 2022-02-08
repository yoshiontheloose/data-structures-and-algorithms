# Trees
<!-- Short summary or background information -->
![sampletree](/code_challenges/trees/sampletree.png)

sample tree image from: [Source](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/Trees.html)

## Challenge
<!-- Description of the challenge -->
**Node**
Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

**Binary Tree**
Create a Binary Tree class

- Define a method for each of the depth first traversals:

  - `pre order`
  - `in order`
  - `post order`
    - returns an array of the values, ordered appropriately.

Any exceptions or errors that come from your code should be semantic, capture-able errors.
For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

**Binary Search Tree**
Create a Binary Search Tree class

- This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
- `Add`
  - Arguments: value
  - Return: nothing
  -Adds a new node with that value in the correct location in the binary search tree.

- `Contains`
  - Argument: value
  - Returns: boolean indicating whether or not the value is in the tree at least once.

**Write tests to prove the following functionality:**

1. Can successfully instantiate an empty tree
2. Can successfully instantiate a tree with a single root node
3. For a Binary Search Tree, can successfully add a left child and right child properly to a node
4. Can successfully return a collection from a preorder traversal
5. Can successfully return a collection from an inorder traversal
6. Can successfully return a collection from a postorder traversal
7. Returns true | false for the contains method, given an existing or non-existing node value

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## API
<!-- Description of each method publicly available in each of your trees -->

-----

# Tree Max
<!-- Description of the challenge -->
Write the following method for the Binary Tree class

find maximum value

- Arguments: none
- Returns: number

Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## Solution
<!-- Show how to run your code, and examples of it in action -->

-----

# Tree Breadth First
<!-- Description of the challenge -->
Write a function called `breadth first` with an argument of `tree`
Return a list of all values in the tree, in the order they were encountered

Write Unit tests

## Whiteboard Process
<!-- Embedded whiteboard image -->

![breadth](/code_challenges/trees/breadth.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O: Space and Time O(n)

## Solution
<!-- Show how to run your code, and examples of it in action -->

---

# Tree Fizz Buzz

Write a function called fizz buzz tree with an argument of k-ary tree
Return a new k-ary

Create a new tree with the same structure as the original, but the values modified as follows:

- If the value is divisible by 3, replace the value with “Fizz”
- If the value is divisible by 5, replace the value with “Buzz”
- If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
- If the value is not divisible by 3 or 5, simply turn the number into a String.

## Whiteboard Process
<!-- Embedded whiteboard image -->

![tree-fizz-buzz](/code_challenges/trees/roughfizzboard.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## Solution
