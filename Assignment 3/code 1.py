
# Priority and Round Robin Scheduling Simulation

# ---------- Priority Scheduling ----------
processes = []
n = int(input("Enter number of processes: "))

for i in range(n):
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    pr = int(input(f"Enter Priority (lower number = higher priority) for P{i+1}: "))
    processes.append((i+1, bt, pr))

# Sort processes by priority (lower number = higher priority)
processes.sort(key=lambda x: x[2])

wt = 0
total_wt = 0
total_tt = 0

print("\nPriority Scheduling:")
print("PID\tBT\tPriority\tWT\tTAT")

for pid, bt, pr in processes:
    tat = wt + bt
    print(f"{pid}\t{bt}\t{pr}\t\t{wt}\t{tat}")
    total_wt += wt
    total_tt += tat
    wt += bt

print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
print(f"Average Turnaround Time: {total_tt / n:.2f}")

# ---------- Round Robin Scheduling ----------
print("\nRound Robin Scheduling:")
quantum = int(input("Enter Time Quantum: "))

bt = [p[1] for p in processes]
rem_bt = bt[:]
wt = [0] * n
t = 0  # Current time

while True:
    done = True
    for i in range(n):
        if rem_bt[i] > 0:
            done = False
            if rem_bt[i] > quantum:
                t += quantum
                rem_bt[i] -= quantum
            else:
                t += rem_bt[i]
                wt[i] = t - bt[i]
                rem_bt[i] = 0
    if done:
        break

tat = [bt[i] + wt[i] for i in range(n)]

print("PID\tBT\tWT\tTAT")
for i in range(n):
    print(f"{processes[i][0]}\t{bt[i]}\t{wt[i]}\t{tat[i]}")

print(f"\nAverage Waiting Time: {sum(wt) / n:.2f}")
print(f"Average Turnaround Time: {sum(tat) / n:.2f}")
