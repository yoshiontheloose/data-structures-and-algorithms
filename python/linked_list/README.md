# Singly Linked List
<!-- Short summary or background information -->
A static data structure that needs a single block of memory. Made up of nodes that reference the next node, ends with a node pointing to a null value.

## Challenge
<!-- Description of the challenge -->
**Features**:

**Node**:

Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

**Linked List**:

- Create a Linked List class

- Within your Linked List class, include a head property.

  - Upon instantiation, an empty Linked List should be created.

<br>

- The class should contain the following methods:

  - insert

    - Arguments: value
    - Returns: nothing
    - Adds a new node with that value to the head of the list with an O(1) Time performance.

  - includes

    - Arguments: value
    - Returns: Boolean
      - Indicates whether that value exists as a Node’s value somewhere within the list.

  - to string

    - Arguments: none
    - Returns: a string representing all the values in the Linked List, formatted as:

> `"{ a } -> { b } -> { c } -> NULL"`

<br>

- Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

- Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).

**Structure and Testing**:

Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:

1. Can successfully instantiate an empty linked list

2. Can properly insert into the linked list

3. The head property will properly point to the first node in the linked list

4. Can properly insert multiple nodes into the linked list

5. Will return true when finding a value within the linked list that exists

6. Will return false when searching for a value in the linked list that does not exist

7. Can properly return a collection of all the values that exist in the linked list

Ensure your tests are passing before you submit your solution.

**Stretch Goal**:

Create a new branch called `doubly-linked-list`, and using the resources available to you online, implement a doubly linked list (completely separate from your singly linked list).

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## API
<!-- Description of each method publicly available to your Linked List -->
