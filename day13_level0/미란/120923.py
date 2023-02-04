'''
연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 두 정수 num과 total이 주어집니다. 연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.
'''

def solution(num, total):
    if num % 2:
        l = int((num - 1) / 2)
        end = int(total/num)
        
        for i in range(end-1, end-l-1, -1):
            result.append(i)
        for j in range(end, end+l+1):
            result.append(j)
    else:
        l = int((num - 2) / 2)
        mid1 = int(total/num)
        mid2 = int(total/num)+1
        for i in range(mid1, mid1-l-1, -1):
            result.append(i)
        for j in range(mid2, mid2+l+1):
            result.append(j)
    return sorted(result)
