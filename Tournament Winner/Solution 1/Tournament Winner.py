def tournamentWinner(competitions, results):
    output = {}
    for i in range(len(competitions)):
        if results[i] == 0:
            if competitions[i][1] in output:
                output[competitions[i][1]] += 3
            else:
                output[competitions[i][1]] = 3
        else:
            if competitions[i][0] in output:
                output[competitions[i][0]] += 3
            else:
                output[competitions[i][0]] = 3
    winner = max(output, key=output.get)
    return winner