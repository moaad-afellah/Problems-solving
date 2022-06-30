listremove = []
def inputWords(stdin):
    listSet = set(stdin)
    print(len(listSet))
    for word in stdin:
        sum = 0
        case = True
        for wordRemove in listremove:
            if word == wordRemove:
                case = False
        if case == True:
            for str in stdin:
                if str == word:
                    sum = sum + 1
            print(sum, end=" ")
        listremove.append(word)



words = ["bcdef","abcdefg","bcde","bcdef"]
inputWords(words)
