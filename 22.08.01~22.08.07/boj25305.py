n, k = map(int, input().split())
grade = list(map(int, input().split()))
grade.sort()
print(grade[-k])

