light_time = list(map(int, input().split()))
n = int(input())
time_list = []
for i in range(n):
    time_list.insert(0, list(map(int, input().split())))
time = 0
for sub_list in time_list:
    if sub_list[0] == 0:
        time += sub_list[1]
    elif sub_list[0] == 1:
        time += sub_list[1]
    elif sub_list[0] == 2:
        time += sub_list[1] + light_time[0]
print(time)