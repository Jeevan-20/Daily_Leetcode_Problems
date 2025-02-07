class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}  
        color_count = defaultdict(int)  
        result = []
        distinct_colors = 0
        for ball, color in queries:
            if ball in ball_colors:
                previous_color = ball_colors[ball]
                color_count[previous_color] -= 1
                if color_count[previous_color] == 0:
                    distinct_colors -= 1  
            ball_colors[ball] = color
            if color_count[color] == 0:
                distinct_colors += 1  
            color_count[color] += 1          
            result.append(distinct_colors)
        return result

