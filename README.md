# Graph-Implementation-in-Python

### Visual Example

Given a graph:

```
        *       *
A---B---C---D---E
```

The `find_path(A, E, 2)` is a valid, achievable path, because between `A` and `C` there are 2 hops, and `C` and `E` are two hops, so the Quokkas will survive. This will then return: `[A, B, C, D, E]`.

Whereas `find_path(A, E, 1)` cannot be reached, because `A` to `B` is 1 hop, and the Quokkas will need food. So this returns `None`.

`exists_path_with_extra_food(A, E, 1, 3)` returns `True`, because adding 3 extra food to (at least) `B`, and `D` will make the path `[A, B, C, D, E]` achievable as there is food at least 1 hop away for each vertex.

**ORDER MATTERS IN THE PATH RETURNS, IT SHOULD BE A SEQUENCE.**

### About the code

Implement 2 major files, `vertex.py` and `graph.py`.

### vertex.py

The `Vertex` class provides the information of the vertex in the graph.

**Properties**

* `has_food` - [Boolean] indicates whether the vertex has food or not.
* `edges` - [List[Vertex]] the list of vertices connected to this vertex, forming edges in the graph.

#### Functions

```
add_edge(v)
```

Adds an edge between this vertex and the Vertex `v`.

```
rm_edge(v)
```

Removes the edge between this vertex and the Vertex `v`.


### graph.py

This `QuokkaMaze` class provides the implementation of the graph for the Quokkas to traverse.

**Properties**

* `vertices` - [List[Vertex]] the list of vertices in the graph.

#### Functions

```
add_vertex(v) -> bool
```

Adds the Vertex `v` to the graph, returning `True` if the operation was successful, `False` if it was not, or it was invalid.

```
fix_edge(u, v) -> bool
```

Fixes an edge between two vertices, `u` and `v`.
If an edge already exists, or the edge is invalid, then this operation should return `False`. Else, if the operation succeeds, return `True`.

Example:
If an edge between `u` and `v` already exists or is invalid, `fix_edge(u, v)` should return False.

```
block_edge(u, v) -> bool
```

Blocks the edge between two vertices, u and v.
Removes the edge if it exists, and returns `True` if the operation was successful.
If the edge does not exist or is invalid, it should be unsuccessful an return `False`.


```
find_path(s, t, k) -> List[Vertex] or None
```

Find a **SIMPLE PATH** between Vertex `s` and Vertex `t` such that from any location with food along this path we reach the next location with food in at most `k` steps.

This function returns: The list of vertices to form the simple path from `s` to `t` which satisfies the condition, or, `None` if there is no path that exists in the graph.

If there are invalid aspects (invalid path, invalid input), then this function returns `None`.


```
exists_path_with_extra_food(s, t, k, x) -> bool
```

Determines whether it is possible for the quokkas to make it from Vertex `s` to Vertex `t` along a **SIMPLE path** where from any location with food we reach the next location with food in at most `k` steps, by placing food at at most `x` new locations.

This function returns `True` if we can complete the simple path with at most `x` additional food, else it returns `False`.

If there are invalid aspects (invalid path, invalid input), then this function returns `False`.

## IMPORTANT INFORMATION

* We will be performing minor adversarial testing, which means:
    * CHECK YOUR PARAMS, for example:
        * `k` should always be >= 0 for `find_path()` and `exists_path_with_extra_food()`.
        * `x` should always be >= 0 for `find_path()` and `exists_path_with_extra_food()`.
    * You must be careful for **ALL** functions.

* List of Vertices as edges in a vertex are **unordered**, but when we fix an edge between two vertices, it should update both!

* The list of vertices returned by path functions (such as `find_path`) **IS ORDERED**, which means you return the sequence to form the path.
