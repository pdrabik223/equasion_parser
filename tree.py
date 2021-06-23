class Value:
    def __init__(self, value):
        self._content = value
        self._left = None
        self._right = None

    def set_left(self, node):
        self._left = node

    def set_right(self, node):
        self._right = node


class Add:
    def __init__(self):
        self._left = None
        self._right = None

    def set_left(self, node):
        self._left = node

    def set_right(self, node):
        self._right = node


class Sub:
    def __init__(self):
        self._left = None
        self._right = None

    def set_left(self, node):
        self._left = node

    def set_right(self, node):
        self._right = node


class Mul:
    def __init__(self):
        self._left = None
        self._right = None

    def set_left(self, node):
        self._left = node

    def set_right(self, node):
        self._right = node


class Div:
    def __init__(self):
        self._left = None
        self._right = None

    def set_left(self, node):
        self._left = node

    def set_right(self, node):
        self._right = node


class Pow:
    def __init__(self):
        self._left = None
        self._right = None

    def set_left(self, node):
        self._left = node

    def set_right(self, node):
        self._right = node