"""
Quokka Maze
===========

This file represents the quokka maze, a graph of locations where a quokka is
trying to find a new home.

Please help the quokkas find a path from their current home to their
destination such that they have sufficient food along the way!
"""

from typing import List, Union

from vertex import Vertex

class QuokkaMaze:
    """
    Quokka Maze
    -----------

    This class is the undirected graph class that will contain all the
    information about the locations between the Quokka colony's current home
    and their final destination.

    We _will_ be performing some minor adversarial testing this time, so make
    sure you're performing checks and ensuring that the graph is a valid simple
    graph!

    ===== Functions =====

        * block_edge(u, v) - removes the edge between vertex `u` and vertex `v`
        * fix_edge(u, v) - fixes the edge between vertex `u` and `v`. or adds an
            edge if non-existent
        * find_path(s, t, k) - find a SIMPLE path from veretx `s` to vertex `t`
            such that from any location with food along this simple path we
            reach the next location with food in at most `k` steps
        * exists_path_with_extra_food(s, t, k, x) - returns whether it’s
            possible for the quokkas to make it from s to t along a simple path
            where from any location with food we reach the next location with
            food in at most k steps, by placing food at at most x new locations

    ===== Notes ======

    * We _will_ be adversarially testing, so make sure you check your params!
    * The ordering of vertices in the `vertex.edges` does not matter.
    * You MUST check that `k>=0` and `x>=0` for the respective functions
        * find_path (k must be greater than or equal to 0)
        * exists_path_with_extra_food (k and x must be greater than or equal to
            0)
    * This is an undirected graph, so you don't need to worry about the
        direction of traversing during your path finding.
    * This is a SIMPLE GRAPH, your functions should ensure that it stays that
        way.
    * All vertices in the graph SHOULD BE UNIQUE! IT SHOULD NOT BE POSSIBLE
        TO ADD DUPLICATE VERTICES! (i.e the same vertex instance)
    """

    def __init__(self) -> None:
        """
        Initialises an empty graph with a list of empty vertices.
        """
        self.vertices = []

    def add_vertex(self, v: Vertex) -> bool:
        """
        Adds a vertex to the graph.
        Returns whether the operation was successful or not.

        :param v - The vertex to add to the graph.
        :return true if the vertex was correctly added, else false
        """
        if (v is None):
            return False
        else:
            # Checking if v already exists in the graph
            if (v in self.vertices):
                return False
            else:
                self.vertices.append(v)
                # Checking if append worked
                if v not in self.vertices:
                    return False
                else:
                    return True

    def fix_edge(self, u: Vertex, v: Vertex) -> bool:
        """
        Fixes the edge between two vertices, u and v.
        If an edge already exists, then this operation should return False.

        :param u - A vertex
        :param v - Another vertex
        :return true if the edge was successfully fixed, else false.
        """

        # Andre's explanation of fix_edge
        # fix_edge fixes a blocked edge (i.e., adds it) if it doesn't exist yet: "Fixes an edge between two vertices, u and v. 
        # If an edge already exists, or the edge is invalid, then this operation should return False."

        #Checking if these vertices are valid
        if (u is None or v is None):
            return False

        # Checking if these vertices exist in this graph
        if (u not in self.vertices or v not in self.vertices):
            return False

        while u is not None or v is not None:
            # If edge doesn't exist
            if (v not in u.edges or u not in v.edges):
                u.add_edge(v) # Fixing edge
                v.add_edge(u) # Fixing edge
                # Checking if add_edge was successful
                if (v not in u.edges or u not in v.edges):
                    return False
                else:
                    return True
            else:
                return False

    def block_edge(self, u: Vertex, v: Vertex) -> bool:
        """
        Blocks the edge between two vertices, u and v.
        Removes the edge if it exists.
        If not, it should be unsuccessful.

        :param u - A vertex
        :param v - Another vertex.
        :return true if the edge was successfully removed, else false.
        """

        # Andre's explanation of block_edge
        # blocks (i.e., removes) an edge: "Blocks the edge between two vertices, u and v. 
        # Removes the edge if it exists, and returns True if the operation was successful. 
        # If the edge does not exist or is invalid, it should be unsuccessful and return False.
        
        #Checking if these vertices are valid
        if (u is None or v is None):
            return False

        # Checking if these vertices exist in this graph
        if (u not in self.vertices or v not in self.vertices):
            return False

        while u is not None or v is not None:
            # If edge exists
            if (v in u.edges or u in v.edges):
                u.rm_edge(v) # Blocking edge
                v.rm_edge(u) # Blocking edge
                # Checking if rm_edge was successful
                if (v in u.edges or u in v.edges):
                    return False
                else:
                    return True
            else:
                return False
                    
    # returns true or false based on if it's possible
    def dfs(self, at: Vertex, dest: Vertex, num_food_left: int, num_food_start: int) -> bool:
        if at == dest:
            if at not in self.good:
                self.good[at] = []
            self.good[at].append(num_food_left)
            return True
        for nxt in at.edges:
            num_food = num_food_left
            if at.has_food:
                num_food = num_food_start
            num_food -= 1
            if num_food < 0:
                continue
            if num_food not in self.last[nxt]:
                self.last[nxt][num_food] = at
                ret = self.dfs(nxt, dest, num_food, num_food_start)
                if ret:
                    self.good[at].append(num_food_left)
                    return True
        return False
    
    def find_path(self, s: Vertex, t: Vertex, k: int) -> Union[List[Vertex], None]:
        """
        find_path returns a SIMPLE path between `s` and `t` such that from any
        location with food along this path we reach the next location with food
        in at most `k` steps

        :param s - The start vertex for the quokka colony
        :param t - The destination for the quokka colony
        :param k - The maximum number of hops between locations with food, so
        that the colony can survive!
        :returns
            * The list of vertices to form the simple path from `s` to `t`
            satisfying the conditions.
            OR
            * None if no simple path exists that can satisfy the conditions, or
            is invalid.

        Example:
        (* means the vertex has food)
                    *       *
            A---B---C---D---E

            1/ find_path(s=A, t=E, k=2) -> returns: [A, B, C, D, E]

            2/ find_path(s=A, t=E, k=1) -> returns: None
            (because there isn't enough food!)

            3/ find_path(s=A, t=C, k=4) -> returns: [A, B, C]

        """
        self.last = {}
        self.good = {}

        for v in self.vertices:
            self.last[v] = {}
            self.good[v] = []

        if s not in self.vertices or t not in self.vertices:
            return None

        if s is None or t is None:
            return None

        if s == t:
            return [s]

        ret = self.dfs(s, t, k, k)
        if not ret:
            return None

        x = t
        ans = []
        ans.append(t)
        num_food_left = self.good[t][0]
        while x != s:
            for last_num_food, last_vertex in self.last[x].items():
                x = last_vertex
                break
            ans.append(x)
        ans = ans[::-1]
        return ans

    # returns true or false based on if it's possible
    def dfs2(self, at: Vertex, dest: Vertex, num_food_left: int, num_food_start: int, num_food_place_on_vertex: int) -> bool:
        if at == dest:
            return True
        self.seen.append((at, num_food_left, num_food_place_on_vertex))
        for nxt in at.edges:
            num_food = num_food_left
            if at.has_food:
                num_food = num_food_start
            num_food -= 1
            new_num_food_place_on_vertex = num_food_place_on_vertex
            if num_food < 0:
                if new_num_food_place_on_vertex > 0:
                    new_num_food_place_on_vertex -= 1
                    num_food = num_food_start - 1
                else:
                    continue
            if (nxt, num_food, new_num_food_place_on_vertex) not in self.seen:
                ret = self.dfs2(nxt, dest, num_food, num_food_start, new_num_food_place_on_vertex)
                if ret:
                    return True
        return False

    def exists_path_with_extra_food(self, s: Vertex, t: Vertex, k: int, x: int) -> bool:
        """
        Determines whether it is possible for the quokkas to make it from s to
        t along a SIMPLE path where from any location with food we reach the
        next location with food in at most k steps, by placing food at at most
        x new locations.

        :param s - The start vertex for the quokka colony
        :param t - The destination for the quokka colony
        :param k - The maximum number of hops between locations with food, so
        that the colony can survive!
        :param x - The number of extra foods to add.
        :returns
            * True if with x added food we can complete the simple path
            * False otherwise.

        Example:
        (* means the vertex has food)
                            *
            A---B---C---D---E

            1/ exists_with_extra_food(A, E, 2, 0) -> returns: False
                (because we can't get from A to E with k=2 and 0 extra food)

            2/ exists_with_extra_food(A, E, 2, 1) -> returns: True
                (Yes, if we put food on `C` then we can get to E with k=2)

            3/ exists_with_extra_food(A, E, 1, 6) -> returns: True
                (Yes, if we put food on `B`, `C`, `D` then we reach E!)

        """
        self.seen = []

        if not s or not t:
            return False

        if s not in self.vertices or t not in self.vertices:
            return False

        return self.dfs2(s,t,k,k,x)
