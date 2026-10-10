from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        # Initialize frontier with the root node
        frontera = StackFrontier()
        frontera.add(root)
        
        # Checkeo si la raíz es el nodo objetivo
        if(grid.objective_test(root)):
            return Solution(root, expanded, root.cost)

        # Empiezo el bucle
        while(not frontera.is_empty()):
            nodo_actual = frontera.remove()
            if nodo_actual.state in expanded:
                continue
            expanded[nodo_actual.state] = True
            for accion in grid.actions(nodo_actual.state):
                estado_nuevo = grid.result(nodo_actual.state, accion)
                if estado_nuevo not in expanded:
                    nodo_nuevo = Node(value="", state=estado_nuevo,
                            cost=nodo_actual.cost + 
                            grid.individual_cost(nodo_actual.state, accion),
                            parent=nodo_actual, action=accion)
                    if grid.objective_test(nodo_nuevo.state):
                        return Solution(nodo_nuevo, expanded, nodo_nuevo.cost)
                    frontera.add(nodo_nuevo)

        return NoSolution(expanded)
