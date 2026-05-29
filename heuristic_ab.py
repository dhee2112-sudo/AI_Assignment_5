import math
MAX = 1000
MIN = -1000
# Heuristic values at terminal nodes
scores = [10, 8, 14, 5, 2, 7, 11, 4]
# Heuristic evaluation function
def heuristic(value):
    return value

def alphabeta(depth,
              node_index,
              maximizing_player,
              values,
              alpha,
              beta,
              max_depth):

    # Base condition
    if depth == max_depth:
        return heuristic(values[node_index])
    # Maximizer
    if maximizing_player:
        best = MIN
        for i in range(2):
            value = alphabeta(depth + 1,
                              node_index * 2 + i,
                              False,
                              values,
                              alpha,
                              beta,
                              max_depth)

            best = max(best, value)
            alpha = max(alpha, best)
            # Pruning
            if beta <= alpha:
                break

        return best
    # Minimizer
    else:
        best = MAX
        for i in range(2):
            value = alphabeta(depth + 1,
                              node_index * 2 + i,
                              True,
                              values,
                              alpha,
                              beta,
                              max_depth)

            best = min(best, value)
            beta = min(beta, best)
            # Pruning
            if beta <= alpha:
                break
        return best
# Depth of tree
tree_depth = math.log2(len(scores))
# Run algorithm
result = alphabeta(0,
                   0,
                   True,
                   scores,
                   MIN,
                   MAX,
                   int(tree_depth))

print("Heuristic Scores:", scores)
print("Best Heuristic Value:", result)