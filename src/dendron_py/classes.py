def is_dendron(d):
    """
    is d an instance of `Dendron` or its derivatives?
    * Defined in .lisp as `dendrop`
    """
    return isinstance(d, Dendron)

class Pattern:
    """
    Root class for patterns.
    """
    def __init__(self,
                 relaxed_support=0,
                 support=0,
                 occurrence=0,
                 membership={}):

        self.relaxed_support = relaxed_support
        self.support = support
        self.occurrence = occurence
        self.membership = membership

class PatternSet(Pattern):
    """
    Class of patterns considered as leaves.
    """
    def __init__(self,
                 elements=None,
                 cardinal=0):
        self.elements = elements
        self.cardinal = cardinal

    def initialize_instance(self):
        """
        Sort elements of a given pattern set (canonical form)
        """
        self.elements = self.leaf_sorting_function()
        self.cardinal = len(self.elements)

    def leaf_sorting_function(self):
        # Do something with self.elements
        return 0



class Dendron(Pattern):
    """
    Class of patterns considered as trees.
    """
    def __init__(self,
                 first_child=None,
                 second_child=None,
                 distance=0,
                 associated_pattern_set=0,
                 ordinal=0,
                 name="a",
                 weight=0,
                 ):
        self.first_child = first_child
        self.second_child = second_child
        self.distance = distance
        self.associated_pattern_set = associated_pattern_set
        self.ordinal = ordinal
        self.name = name
        self.weight = weight
        self._is_leaf()

    def _is_leaf(self):
        if self.first_child == None and self.second_child == None:
            return True
        return False

    def canonicalise(self):
        """
        The canonical form of a dendrogram is defined as
        - If FIRST-CHILD and SECOND-CHILD are both leaves, FIRST-CHILD and SECOND-CHILD
            are ordered alphabetically.
        - If one of them is not a leave, it must be SECOND-CHILD
        - Otherwise, FIRST-CHILD must be heavier than SECOND-CHILD.
        - If they are equally heavy, then are ordered alfabetically according
            to their elements.
        """
        if self.first_child._is_leaf() and self.second_child._is_leaf():
            # Case both are leaf
            if self.first_child.name < self.second_child.name:
                # Order by name
                self.swap_children()

        elif not self.first_child._is_leaf() and self.second_child._is_leaf():
            # Case first_child is not leaf, but second_child is
            self.swap_children()

        elif not self.first_child._is_leaf() and not self.second_child._is_leaf():
            # Case none is leaf
            if self.first_child.weight < self.second_child.weight:
                # Order by weight
                self.swap_children()

    def swap_children(self):
        (self.first_child, self.second_child) = (self.second_child, self.first_child)

    def __repr__(self):
        s = f"""
        {self.name}
        |---- {self.first_child.name}: {self.first_child.weight}
        |---- {self.second_child.name}: {self.second_child.weight}
        """
        return s

class Dendrogram:
    """
    A full dendrogram.
    Has a root and is composed of dendrons.
    """
    def __init__(self, root):
        self.root = root
