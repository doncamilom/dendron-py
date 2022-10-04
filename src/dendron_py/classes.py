



class Pattern:
    """
    Root class for patterns.
    """
    def __init__(self,
                 relaxed_support=0,
                 support=0,
                 occurrence=0,
                 membership={}):
        return 0

class PatternSet(Pattern):
    """
    Class of patterns considered as leaves.
    """
    def __init__(self,
                 elements=None,
                 cardinal=0):
        return 0


class Dendron(Pattern):
    """
    Class of patterns considered as trees.
    """
    def __init__(self,
                 first_child,
                 second_child,
                 distance,
                 associated_pattern_set,
                 ordinal):
        return 0

class Dendrogram:
    """
    Class possesing a root dendron.
    """
    def __init__(self, root):
        return 0

    # Most methods are defined for this class
