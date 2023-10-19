def print_btree(node, depth):
    if isinstance(node, list):
        print('.' * depth + str(node[0]))
        if len(node) > 1:
            print_btree(node[1], depth + 1)
    else:
        print('.' * (depth + 1) + str(node))

print_btree([1,[[11,[111,112]], [12,[121,[122,[1221,1222]]]]]], 0)