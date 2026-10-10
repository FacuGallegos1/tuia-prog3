from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        frontera = PriorityQueueFrontier()
        frontera.add(node=root, priority=root.cost)

        # Empiezo el bucle
        while(not frontera.is_empty()):
            nodo_actual = frontera.pop()
            if grid.objective_test(nodo_actual.state):
                return Solution(nodo_actual, reached, nodo_actual.cost)
            for accion in grid.actions(nodo_actual.state):
                estado_nuevo = grid.result(nodo_actual.state, accion)
                costo_nuevo = nodo_actual.cost + grid.individual_cost(
                    nodo_actual.state, accion)
                if (estado_nuevo not in reached or 
                costo_nuevo < reached[estado_nuevo]):
                    nodo_nuevo = Node(value="", state=estado_nuevo, 
                        cost=costo_nuevo, parent=nodo_actual, action=accion)
                    reached[nodo_nuevo.state] = nodo_nuevo.cost
                    frontera.add(node=nodo_nuevo, 
                                 priority=nodo_nuevo.cost)

        return NoSolution(reached)
