'''
N명의 선수들에 대해 선수들의 실력 값이 차례대로 주어진다.
이 선수들 중 일부를 골라서 팀을 구성할 것이다.
유일한 조건은 실력 차이가 K를 초과하는 선수들이 팀에 선발되면 안된다는 것이다.
조건을 만족하며 최대 인원이 되도록 팀을 구성할 때 그 인원 수를 제시하라.

예를 들어, N = 4, K = 2이고 선수들의 실력이 각각 6, 4, 2, 3인 경우를 생각하자.
실력이 2, 3, 4인 선수들을 선발하여 총 3명인 팀을 구성하는 것은 가능하다
그러나, 총 4명인 팀을 구성할 방법은 없다'''


'''
3                           // 테스트 케이스의 수

4 2                         // N = 4, 테스트 케이스 #1 3
6 4 2 3

4 3                         // N = 4, 테스트 케이스 #2 4
1 2 3 4

4 1                         // N = 4, 테스트 케이스 #3 1
1 3 7 5
'''

T = int(input())

for test_case in range(1, T + 1):
    N=list(map(int,input().split())) #[2,4]
    person=list(map(int,input().split())) #[6,4,2,3]

    teams=list()
    new_teams=list()
    answer=0
    for i in person:
        for j in person[i:]:
            if j<=i+N[1]:
                if([i,j] in teams):
                    continue
                else:
                    teams.append([i,j])
                    if j in new_teams:
                        continue
                    else:
                        new_teams.append(j)
                        answer+=1
        
    if answer==0:
        answer=1
    print(f"#{test_case} {answer}")