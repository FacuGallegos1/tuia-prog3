from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        
        # Initialize frontier with the root node
        frontier = QueueFrontier()
        frontier.add(root)
        
        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        # Checkeo si la raíz es el nodo objetivo
        if(grid.objective_test(root)):
            return Solution(root, reached, root.cost)
        
        # Empiezo el bucle
        while(not frontier.is_empty()):
            nodo_actual = frontier.remove()
            for accion in grid.actions(nodo_actual.state):
                estado_nuevo = grid.result(nodo_actual.state, accion)
                if estado_nuevo not in reached:
                    nodo_nuevo = Node(value="", state=estado_nuevo,
                            cost=nodo_actual.cost + 
                            grid.individual_cost(nodo_actual.state, accion),
                            parent=nodo_actual, action=accion)
                    reached[nodo_nuevo.state] = True
                    if grid.objective_test(nodo_nuevo.state):
                        return Solution(nodo_nuevo, reached, nodo_nuevo.cost)
                    frontier.add(nodo_nuevo)

        # En caso de que la frontera quede vacía
        return NoSolution(reached)
