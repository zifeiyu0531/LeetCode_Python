def change_color(sub_list, time, light_time):
    while time > 0:
        if time > sum(light_time):
            time -= sum(light_time)
        elif time == 0:
            return
        elif time < sub_list[1]:
            sub_list[1] -= time
            return
        else:
            time -= sub_list[1]
            if sub_list[0] == 1:
                sub_list[0] = 3
                sub_list[1] = light_time[2]
            elif sub_list[0] == 2:
                sub_list[0] = 1
                sub_list[1] = light_time[0]
            elif sub_list[0] == 3:
                sub_list[0] = 2
                sub_list[1] = light_time[1]

light_time = list(map(int, input().split()))
n = int(input())
time_list = []
for i in range(n):
    time_list.append(list(map(int, input().split())))
time = 0
for sub_list in time_list:
    if sub_list[0] == 0:
        time += sub_list[1]
    else:
        change_color(sub_list, time, light_time)
        if sub_list[0] == 1:
            time += sub_list[1]
        elif sub_list[0] == 2:
            time += sub_list[1] + light_time[0]
print(time)
