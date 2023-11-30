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