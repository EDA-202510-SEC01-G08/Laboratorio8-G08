from DataStructures.Tree import bst_node as bst
def new_map():
    return {"root": None}

def put(my_bst, key, value):

    nodo = bst.new_node(key, value)

    if my_bst["root"] is None:
        my_bst["root"] = nodo
    else:
        insert_node(my_bst["root"], key, value)
    return my_bst

def size(my_bst):
    if my_bst["size"] is None:
        return 0
    else:
        return my_bst["size"]
    


    
def insert_node(root, key, value):
    if root is None:
        return bst.new_node(key, value)
    if key < root["key"]:
        root["left"] = insert_node(root["left"], key, value)
    elif key > root["key"]:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value
    root["size"] = 1 + size(root["left"]) + size(root["right"])
    return root