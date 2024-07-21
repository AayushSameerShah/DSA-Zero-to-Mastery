# **Store anywhere you want in memory**

## Why AND Why-not LinkedList?

**Advantages:**

1. **Dynamic Size:** Linked lists can dynamically grow and shrink during runtime, allowing for efficient memory usage.
2. **Insertions and Deletions:** Insertions and deletions can be performed quickly at any position in the list, with constant time complexity, $O(1)$ if the position is known.
3. **No Wastage of Memory:** Memory is allocated only when needed, eliminating memory wastage compared to arrays.
4. **Ease of Implementation:** Linked lists are relatively easy to implement and understand, making them suitable for beginners.
5. **Versatility:** Different types of linked lists (singly, doubly, circular) offer versatility to suit specific requirements.

**Disadvantages:**

1. **No Random Access:** Unlike arrays, linked lists do not support random access to elements. Traversing requires sequential access from the beginning.
2. **Memory Overhead:** Each node in a linked list requires extra memory for storing a pointer/reference to the next node, leading to memory overhead.
3. **Slower Access Time:** Accessing elements in a linked list is slower compared to arrays due to the lack of direct indexing.
4. **Traversal Overhead:** Traversing a linked list requires iterating through each node, which can result in slower performance for large lists.
5. **Cache Unfriendly:** Linked lists may not utilize CPU cache efficiently due to scattered memory locations of nodes.

> 💡 So Linkedlist only shines **in faster insertions and deletions**.

## Time

- prepand - `O(1)`
- append - `O(1)`
- lookup - `O(n)`
- insert - `O(n)`
- delete - `O(n)`

Note: The `insert` and `delete` may look like *not advantage* than the arrays, but they are. As we would not usually insert or delete at the end of the list.

## Okay, but how is LL different than HashTables?

- See, LL stores the data with some "address" just like the "hash tables" do.
- The main difference is **the order** that the LL provides. In Hash Tables, there is no order.

## Singly LL

- The same stuff, traverse in the single direction
- Simple, but with `O(n)` time in deletion and insertion

## Doubly LL

- Holds addresses of previous and next block
- Optimized insertions and deletions; technically still `O(n)` (which is `O(n/2)`) but you can see, it is faster.

Sure! Here's a revised version of your markdown text for better readability and clarity:

### When Should We Use Singly vs. Doubly Linked Lists?

#### ✅ Singly Linked Lists

- Simple implementation
- Less memory usage
- Fewer operations
- Ideal when memory is limited
- Suitable for applications with minimal searching requirements

#### ✅ Doubly Linked Lists

- Can be iterated from both the front and back

#### ❌ Singly Linked Lists

- If the `head` node is lost, the list is lost in memory forever
- Not recommended for applications with extensive searching requirements

#### ❌ Doubly Linked Lists

- Requires extra memory
- Involves additional operations
