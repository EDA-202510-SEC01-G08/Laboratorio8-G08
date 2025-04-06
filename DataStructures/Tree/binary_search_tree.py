from DataStructures.Tree import bst_node as bst

def new_map():
    return {"root": None}

def put(my_bst, key, value):
    if my_bst["root"] is None:
        my_bst["root"] = bst.new_node(key, value)
    else:
        insert_node(my_bst["root"], key, value)
        my_bst["root"]["size"] += 1
    return my_bst

def insert_node(root, key, value):
    if key < root["key"]:
        if root["left"] is None:
            root["left"] = bst.new_node(key, value)
        else:
            insert_node(root["left"], key, value)

    elif key > root["key"]:
        if root["right"] is None:
            root["right"] = bst.new_node(key, value)

        else:
            insert_node(root["right"], key, value)
    else:
        root["value"] = value

def get(my_bst, key):

    if my_bst["root"] is None:
        return None
    else:
        return get_node(my_bst["root"], key)

def get_node(root, key):

    if root is None:
        return None
    if key < bst.get_key(root):
        return get_node(root["left"], key)
    elif key > bst.get_key(root):
        return get_node(root["right"], key)
    else:
        return bst.get_value(root)
    
def remove(my_bst, key):
    if my_bst["root"] is None:
        return my_bst
    else:
        print(my_bst)
        my_bst["root"] = remove_node(my_bst["root"], key)
        my_bst["root"]["size"] -= 1
        return my_bst

def remove_node(root, key):

    if key < bst.get_key(root):
        root["left"] = remove_node(root["left"], key)
    elif key > bst.get_key(root):
        root["right"] = remove_node(root["right"], key)
    else:
        if root["left"] is None:
            return root["right"]
        elif root["right"] is None:
            return root["left"]
        else:
            min_node = get_min_node(root["right"])
            root["key"] = min_node["key"]
            root["value"] = min_node["value"]
            root["right"] = remove_node(root["right"], min_node["key"])
            return root

def get_min(my_bst):
    if my_bst["root"] is None:
        return None
    else:
        return get_min_node(my_bst["root"])

def get_min_node(root):
    if root is None:
        return None
    while root["left"] is not None:
        root = root["left"]
    return bst.get_key(root)

def size(my_bst):
    return size_tree(my_bst["root"])

def size_tree(root):
    if root is None:
        return 0
    return root["size"] 
    

