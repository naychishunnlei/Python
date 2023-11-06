popularity_scores = {
    "C++" : 99.7,
    "C" : 96.7,
    "Java" : 97.5,
    "Python" : 100,
    "C#" : 97.5
}

def ranking_scores(popularity_scores):
    temp = []
    #turns the dictionary to list for bubble sort listing

    for language, scores in popularity_scores.items():
        temp.append([language, scores])

    for i in range(len(temp)):
        for j in range(len(temp) - i - 1):
            if temp[j][1] < temp [j+1][1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]
            elif temp[j][1] == temp[j+1][1]:
                temp[j][0] += ", " + temp[j+1][0]
                del temp[j+1]
            else:
                pass

    ranked = {}
    for i in range(len(temp)):
        if i+1 not in ranked:
            ranked[i+1] = temp[i][0]
        else:
            pass
    return ranked

print(ranking_scores(popularity_scores))