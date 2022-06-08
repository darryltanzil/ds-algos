## Linked Lists
Information is from the following:
* https://www.freecodecamp.org/news/python-interview-question-guide-how-to-code-a-linked-list-fd77cbbd367d/

## Definition
* An ordered collection of objects that **store references as part of their own elements**, as opposed to lists, which use contigous memory blocks to store references to their data
* Each element of a linked list is called a node, which has two different fields
    1. **Data** is the value stored in Node
    2. **Pointer** to the next node on the list
* First is called the **head**, always the starting point
* Last is called the **tail**
* Last node must have its next reference pointing to **None** to determine the end of the list

* Singly linked means that each node only points to at most 1 other node, the node in front of it. 

![image](https://user-images.githubusercontent.com/5387769/172727440-efcf97dc-4975-4871-9af6-59ef83c1fd57.png)

* Doubly linked means that each node can point to 2 other nodes, the node in front of it and the node behind it. 

![image](https://user-images.githubusercontent.com/5387769/172727475-6f51d621-62c4-45fb-b71c-417717c8df18.png)

## Practical Application

* Can be used to make queues, stacks, or graphs

## Implementing in Code

In a coding interview, all you're going to be given is a head node.

```python
class Solution(object):
    def linkedListSolution(self, head): # all that's being passed is head node
```

#### Defining a Node
```python
class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode
```
#### Traversing through a Node
```python
currentNode = head 
while currentNode is not None: 
    print currentNode.value, # do items with current Node
    currentNode = currentNode.nextNode
```

### Inserting a Node
```python
while currentNode is not None:
    if currentNode.nextNode is None:
        currentNode.nextNode = linkedListNode(valueToInsert)
        return head
    currentNode = currentNode.nextNode
```
#### Deleting a Node
```python
def deleteNode(head, valueToDelete):
    currentNode = head
    previousNode = None

    while currentNode is not None:
        if currentNode.value == valueToDelete:
            if previousNode is None:
                 newHead = currentNode.nextNode
                currentNode.nextNode = None
                return newHead # Deleted the head
            previousNode.nextNode = currentNode.nextNode
            return head
        previousNode = currentNode
        currentNode = currentNode.nextNode
    return head # Value to delete was not found.
```

## Time Complexity
* Inserting to the back of the Linked List— We go through all n elements to find the tail and insert our new node. O(n)
* Inserting to the front of the Linked List — We simply create the new node and set its nextNode to the head. No need to traverse the list. O(1)
* Traversing — We go through all n elements once. O(n)
* Deleting — Worst case scenario, the node we’re deleting is the last node, causing us to traverse through the entire list. O(n)
