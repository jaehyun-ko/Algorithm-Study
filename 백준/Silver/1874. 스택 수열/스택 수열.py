#  데이터 입력 받는 부분
N = int(input())
target_dataset = []
for i in range(N):
    target_dataset.append(int(input()))
result = []
ans = []
s = []
gen = iter(target_dataset)
try:
    target = next(gen)
except StopIteration:
    print("NO")
    exit()

i = 1
while i <= N or s:
    if i <= N and i == target:
        # Push and immediately pop
        ans.append("+")
        ans.append("-")
        result.append(i)
        i += 1
        try:
            target = next(gen)
        except StopIteration:
            break
    elif i <= N and i < target:
        # Push to stack
        s.append(i)
        ans.append("+")
        i += 1
    else:
        if s and s[-1] == target:
            # Pop from stack
            result.append(s.pop())
            ans.append("-")
            try:
                target = next(gen)
            except StopIteration:
                break
        else:
            print("NO")
            exit()

if result == target_dataset:
    print("\n".join(ans))
else:
    print("NO")
