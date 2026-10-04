class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        if iterations == 0:
            return init
        
        minimizer = init * ((1 - 2 * learning_rate) ** iterations)
        return round(minimizer, 5)

