name = input("What is your name? ")
hours = int(input("How many hours can you study each day? "))

print("Nice to meet you,", name)

if hours >= 3:
    print("That is a great plan. You can finish the roadmap in about 5 weeks.")
elif hours >= 1:
    print("That is a good start. It may take about 10 weeks, and that is fine.")
else:
    print("Even 30 minutes a day counts. Try to be regular.")