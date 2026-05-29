import math
# Terminal node values
scores = [3, 5, 2, 9, 12, 5, 23, 23]
def minimax(depth, node_index, is_maximizing, scores, max_depth):
    # Base condition
    if depth == max_depth:
        return scores[node_index]
    # Maximizer's turn
    if is_maximizing:
        left = minimax(depth + 1,
                       node_index * 2,
                       False,
                       scores,
                       max_depth)

        right = minimax(depth + 1,
                        node_index * 2 + 1,
                        False,
                        scores,
                        max_depth)

        return max(left, right)
    # Minimizer's turn
    else:
        left = minimax(depth + 1,
                       node_index * 2,
                       True,
                       scores,
                       max_depth)

        right = minimax(depth + 1,
                        node_index * 2 + 1,
                        True,
                        scores,
                        max_depth)

        return min(left, right)


# Height of tree
tree_depth = math.log2(len(scores))
# Call minimax
result = minimax(0, 0, True, scores, int(tree_depth))
print("Scores:", scores)
print("Optimal Value:", result)