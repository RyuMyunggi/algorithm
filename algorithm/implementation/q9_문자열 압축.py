# 문자열 압축

def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가면서 확인
    # 모든 경우의 수에 대한 완전탐색
    for step in range(1, len(s) // 2 + 1):
        compressed = ''
        # 앞에서부터 step만큼 문자열 추출
        prev = s[0:step]
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상의 압축이 불가능 하다면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                # 다시 상태 초기화
                prev = s[j: j + step]
                count = 1

        # 남아있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))

    return answer


if __name__ == '__main__':
    s = 'abcabcabs'
    s = 'aaaabbabbabb'
    print(solution(s))