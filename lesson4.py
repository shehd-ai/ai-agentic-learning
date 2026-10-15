me = {
    "name": "Shahad",
    "city": "Kannur",
    "goal": "AI agent trainee",
    "hours_per_day": 1
}

print("Name:", me["name"])
print("Goal:", me["goal"])

me["college"] = "Yenepoya University"


def weeks_needed(hours_per_day):
    if hours_per_day >= 3:
        return 5
    return 10


weeks = weeks_needed(me["hours_per_day"])
print("At", me["hours_per_day"], "hours a day, I need about", weeks, "weeks")