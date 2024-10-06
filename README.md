# Pathfinding Starter Code

The player cannot return to the start.
The player must visit the target before the exit.
The player cannot revisit nodes that have already been visited in a single path.

Random Path Generation: 
    Precondition: 
        Verify that the start, target, and exit are valid nodes within the graph ie more than 2 nodes

    Random Path Generation:
        Randomly generate a path from the start to the target.
        Randomly generate a path from the target to the exit.
        Follow player rules

    Postcondition:
        Verify the path starts at the start node, includes the target node, and ends at the exit node.