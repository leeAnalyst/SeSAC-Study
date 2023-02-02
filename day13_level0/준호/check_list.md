### level 0 (Day 13)

- [ ] 옹알이(1)
- [ ] 다음에 올 숫자
  def solution(common):
    add = common[2] - common[1]
    prod = common[2] / common[1]
    
    if common[1] - common[0] == common[2] - common[1]:
        return common[-1] + add
    else:
        return common[-1] * prod
- [ ] 연속된 수의 합
- [X] 종이 자르기
  def solution(M, N):
    return M*N-1
- [ ] 문자열 밀기
- [ ] 잘라서 배열로 저장하기
