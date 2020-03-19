from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.color = None

class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        self.graph = {}
        vfile = open(filename,'r')
        for line in vfile:
            new_line = line.split()
            self.add_vertex(new_line[0])
            self.add_vertex(new_line[1])
            self.add_edge(new_line[0], new_line[1])
        vfile.close()

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if key not in self.graph:
            self.graph[key] = Vertex(key)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if key in self.graph:
           return self.graph[key]
        else:
            return None

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        if v2 not in self.graph[v1].adjacent_to:
            self.graph[v1].adjacent_to.append(v2)
        if v1 not in self.graph[v2].adjacent_to:
            self.graph[v2].adjacent_to.append(v1)

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        key_list = []
        for key in self.graph.keys():
            key_list.append(key)
        return key_list.sort()

    def conn_components(self): 
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        my_stack = Stack(len(self.graph))
        key_list = list(self.graph.keys())
        final_list = []
        small_list = []
        while len(key_list) != 0:
            my_stack.push(key_list[0])
            while not my_stack.is_empty():
                current_key = my_stack.pop()
                current_vertex = self.get_vertex(current_key)
                adjacency_list = current_vertex.adjacent_to
                for vertex in adjacency_list:
                    if vertex not in small_list:
                        my_stack.push(vertex)
                if current_key not in small_list:
                    small_list.append(current_key)
            for key in small_list:
                if key in key_list:
                    key_list.remove(key)
            small_list.sort()
            final_list.append(small_list)
            small_list = []
        return final_list

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        components = self.conn_components()
        if components is None:
            components = self.conn_components()
        queue = Queue(len(self.get_vertices()))
        if components is None:
            return False
        else:
            for component in components:
                first = component[0]
                queue.enqueue(component[0])
                self.get_vertices[first].color = "yes"
                while queue.is_empty() is not True:
                    current = queue.dequeue()
                    for adjacent in self.get_vertices[current].adjacent_to:
                        if self.get_vertices[adjacent].color is None:
                            self.get_vertices[adjacent].color == self.get_vertices[current].color[::-1]
                            queue.enqueue(adjacent)
                        elif self.get_vertices[adjacent].color == self.get_vertices[current].color:
                            return False
            return True



