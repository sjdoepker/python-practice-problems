class Empty:

    def __init__(self):
        # nothing to do!
        pass

    def is_empty(self):
        return True

    def is_leaf(self):
        return False

    def num_nodes(self):
        return 0

    def height(self):
        return 0

    def contains(self, n):
        return False

    def insert(self, n):
        return Node(n, Empty(), Empty())

    def inorder(self):
        return []

    def min_item(self):
        return None

    def max_item(self):
        return None

    def balance_factor(self):
        return None

    def balanced_everywhere(self):
        return True

    def add_to_all(self, n):
        return Empty()

    def path_to(self, n):
        return None

    def __str__(self):
        return " "

class Node:

    def __init__(self, n, left, right):
        self.value = n
        self.left = left
        self.right = right

    def is_empty(self):
        return False

    def is_leaf(self):
        return self.left.is_empty() and self.right.is_empty()

    def num_nodes(self):
        return 1 + self.left.num_nodes() + self.right.num_nodes()

    def height(self):
        return 1 + max(self.left.height(), self.right.height())

    def contains(self, n):
        if n < self.value:
            return self.left.contains(n)
        elif n > self.value:
            return self.right.contains(n)
        else:
            return True

    def insert(self, n):
        if n < self.value:
            return Node(self.value, self.left.insert(n), self.right)
        elif n > self.value:
            return Node(self.value, self.left, self.right.insert(n))
        else:
            return self

    def inorder(self):
        if self.is_empty():
            return []
        else:
            return self.left.inorder() + [self.value] + self.right.inorder()

    def min_item(self):
        if self.is_empty():
            return None
        else:
            if self.left.is_empty():
                return self.value
            else:
                return self.left.min_item()

    def max_item(self):
        if self.is_empty():
            return None
        else:
            if self.right.is_empty():
                return self.value
            else:
                return self.right.min_item()

    def balance_factor(self):
        if self.is_empty():
            return None
        else:
            return (self.right.height() - self.left.height())

    def balanced_everywhere(self):
        if self.is_empty():
            return True
        else:
            return abs(self.balance_factor()) <= 1
        
    def add_to_all(self, n):
        if self.is_empty():
            return Empty()
        else:
            if self.is_leaf():
                return Node(self.value + n, Empty(), Empty())
            else:
                return Empty().insert(Node(self.value+n, self.left.add_to_all(n), self.right.add_to_all(n)))

    def path_to(self, n):
        if self.value == n:
            print('found')
            return [self.value]
        elif n < self.value:
            print('less')
            return [self.value] + self.left.path_to(n)
        elif n > self.value:
            print('more')
            return [self.value] + self.right.path_to(n)
        else: 
            return None

    def __str__(self):
        return str(self.left) + "<-" + str(self.value) + "->" + str(self.right)



if __name__ == "__main__":
    bst = Empty().insert(42).insert(10).insert(15).insert(63)

    print(f"The number of nodes is {bst.num_nodes()}")
    print(f"The height is {bst.height()}")
