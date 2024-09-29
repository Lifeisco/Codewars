def solution(text, ending):
    return True if ending == text[len(text)-len(ending):] else False

print(solution("eypkvahj", "pkvahj"))
