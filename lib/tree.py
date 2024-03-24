class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        def depth_first_search(node):
            if node is None:
                return None
            if node.get('id') == id:
                return node
            for child in node.get('children', []):
                result = depth_first_search(child)
                if result:
                    return result
            return None
        
        # Call the depth-first search function with the root node
        return depth_first_search(self.root)

    def breadth_first_traversal(self):
        if self.root is None:
            return []
        
        result = []
        nodes_to_visit = [self.root]

        while len(nodes_to_visit) > 0:
            # Remove the first node from the `nodes_to_visit` list
            node = nodes_to_visit.pop(0)
            # Add its value to the result list
            result.append(node['value'])
            # Add its children (if any) to the END of the `nodes_to_visit` list
            nodes_to_visit.extend(node.get('children', []))

        return result

# Example usage:
tree = Tree({
    'value': 1,
    'children': [
        {'value': 2, 'children': []},
        {'value': 3, 'children': []},
        {'value': 4, 'children': []}
    ]
})

print(tree.breadth_first_traversal())
