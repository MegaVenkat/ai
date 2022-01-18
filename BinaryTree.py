from binarytree import build
n = int(input("Enter nodes in level order one by one : "))
print("Enter nodes in level order one by one : ")
i = 0
nodes = []
while i != n:
    nodes.append(int(input()))
    i = i+1

binary_tree = build(nodes)
print('Binary tree from list :', binary_tree)

print('List from binary tree :', binary_tree.values)
