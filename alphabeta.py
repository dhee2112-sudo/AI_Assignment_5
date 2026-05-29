import math
MAX = 1000
MIN = -1000
# Terminal node values
scores = [3, 5, 2, 9, 12, 5, 23, 23]
def alphabeta(depth,
              node_index,
              maximizing_player,
              values,
              alpha,
              beta,
              max_depth):

    # Base case
    if depth == max_depth:
        return values[node_index]
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
            # Alpha-Beta Pruning
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
            # Alpha-Beta Pruning
            if beta <= alpha:
                break
        return best

# Tree depth
tree_depth = math.log2(len(scores))
# Call function
result = alphabeta(0,
                   0,
                   True,
                   scores,
                   MIN,
                   MAX,
                   int(tree_depth))

print("Scores:", scores)
print("Optimal Value:", result)