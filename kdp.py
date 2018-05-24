import itertools


class Kdp:
    """
    Columns are blocks
    Rows are points
    """
    
    def __init__(self, incidence_matrix):
        self.points = len(incidence_matrix)
        self.blocks = len(incidence_matrix[0])
        self._incidence_matrix = incidence_matrix
    
    def __getitem__(self, item):
        return self._incidence_matrix[item]
    
    def __repr__(self):
        return repr(self._incidence_matrix)
    
    def __str__(self):
        return '\n'.join(
            [' '.join(map(str, x)) for x in self._incidence_matrix])
    
    def sorted(self):
        return sorted(self._incidence_matrix)
        return Kdp(list(zip(*sorted(zip(*sorted(self._incidence_matrix))))))
    
    """
    Returns Kdp(n, n(n-1)//2) where each pair of members uses separate key
    """
    
    @staticmethod
    def get_trivial_kdp(n):
        incidence_matrix = []
        for i in range(n):
            incidence_matrix.append([])
        for combination in itertools.combinations(range(n), 2):
            for j in range(n):
                incidence_matrix[j].append(1 if j in combination else 0)
        return Kdp(incidence_matrix)
    
    """
    Returns Kdp(n,n)
    """
    
    @staticmethod
    def get_extremal_kdp(n):
        incidence_matrix = []
        for i in range(n):
            incidence_matrix.append([1 if x != i else 0 for x in range(n)])
        return Kdp(incidence_matrix)
    
    """
    Returns kdp which matrix is a vertical concatenation of first and second kdp matrices
    """
    
    @staticmethod
    def unite(first, second):
        return Kdp(first._incidence_matrix + second._incidence_matrix)
    
    def to_matrix(self):
        return self._incidence_matrix
