'''
문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.
'''

def solution(cipher, code):
    return ''.join([cipher[x] for x in range(code-1, len(cipher), code)])
