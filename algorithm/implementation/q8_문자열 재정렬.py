# 문자열 재정렬

def solution(strings):
    s = []
    n = 0
    for string in strings:
        if string.isalpha():
            s.append(string)
        else:
            n += int(string)

    s = ''.join(sorted(s))
    s += str(n)

    return s


if __name__ == '__main__':
    strings = 'K1KA5CB7'
    strings = 'AJKDLSI412K4JSJ9D'
    print(solution(strings))
