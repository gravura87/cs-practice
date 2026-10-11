def winner(names: list[str], scores: list[float]) -> str:
    if not scores:
        return ""
    
    max_score = max(scores)
    winner_index = scores.index(max_score)
    return names[winner_index]


def average(scores: list[float]) -> float:
    if not scores:
        return 0.0
    
    return round(sum(scores) / len(scores), 2)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    indices = list(range(len(names)))
    sorted_indices = sorted(indices, key=lambda i: scores[i], reverse=True)
    return [names[i] for i in sorted_indices]