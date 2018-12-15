#!/usr/bin/python

from collections import Counter

# pre-sorted input with "$ sort input.txt > input-sorted.txt"
file = open("input-sorted.txt")
lines = file.read().split("\n")

guard_sleepy_times = dict()

sleepiestGuardId = ""
sleepiestGuardIdMinute = ""
for line in lines:
    if "Guard" in line:
        guardId = line.split(" ")[3]
    elif "falls asleep" in line:
        asleepLine = line.split(" ")
        date = asleepLine[0].replace("[", "")
        fromTime = int(asleepLine[1].replace("]", "").split(":")[1])
    elif "wakes up" in line:
        wakeupLine = line.split(" ")
        date = wakeupLine[0].replace("[", "")
        toTime = int(wakeupLine[1].replace("]", "").split(":")[1])
        sleepyTime = toTime - fromTime
        
        try:
            guard_sleepy_times[guardId]
        except:
            guard_sleepy_times[guardId] = dict()
            guard_sleepy_times[guardId]["totalSleepyTime"] = 0
            guard_sleepy_times[guardId]["sleepyMinutes"] = []
        
        guard_sleepy_times[guardId]["totalSleepyTime"] += sleepyTime
        guard_sleepy_times[guardId]["sleepyMinutes"].extend(list(range(fromTime, toTime)))
        guard_sleepy_times[guardId]["sleepiestMinute"] = Counter(guard_sleepy_times[guardId]["sleepyMinutes"]).most_common(1).pop()
        
        if sleepiestGuardId == "" or guard_sleepy_times[guardId]["totalSleepyTime"] > guard_sleepy_times[sleepiestGuardId]["totalSleepyTime"]:
            sleepiestGuardId = guardId

        if sleepiestGuardIdMinute == "" or guard_sleepy_times[guardId]["sleepiestMinute"][1] > guard_sleepy_times[sleepiestGuardIdMinute]["sleepiestMinute"][1]:
            sleepiestGuardIdMinute = guardId
        
sleepiestMinute = guard_sleepy_times[sleepiestGuardId]["sleepiestMinute"][0]
checkSum = sleepiestMinute * int(sleepiestGuardId.replace("#", ""))
print "sleepiest guard (based on totalSleepyTime)"
print "guardId: %s, sleepiestMinute: %d, checkSum %d" % (sleepiestGuardId, sleepiestMinute, checkSum)

sleepiestMinute = guard_sleepy_times[sleepiestGuardIdMinute]["sleepiestMinute"]
checkSum = sleepiestMinute[0] * int(sleepiestGuardIdMinute.replace("#", ""))
print "sleepiest guard (based on sleepiestMinute)"
print "guardId: %s, sleepiestMinute: %s, checkSum %d" % (sleepiestGuardIdMinute, sleepiestMinute, checkSum)