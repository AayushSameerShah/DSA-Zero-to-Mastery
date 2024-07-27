# In graph...

The DFS and BFS have the same (similar) get going. Now, we have something different this time. **Shortest path**.

For this, we need to know 2 main methods:

1. Dijikstra
2. Ballman

> 👉🏻 We usually talk "BFS" is used for *shortest path* but **that algorithm doesn't care about the weight**. So, the Dijkistra and Ballman uses the weights for each node to calculate the shortest path.

Let's review them. 

#### Dijkstra

- Doesn't accomodate the negative weights 
- Faster than ballman

#### Ballman

- Great, works on all sort of weights
- Slow, has time complexity of `O(n^2)`.