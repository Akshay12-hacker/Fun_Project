responses = [
    "Come on, say yes! 🥺",
    "Are you sure? 😢",
    "I won't give up! 😠",
    "You're breaking my heart! 💔",
    "Just say yes, please! 🙏"
]

print("Do you Love Me?")

index = 0
while True:
    answer = input("Enter 'yes' or 'no': ").strip().lower()
    if answer == "yes":
        print("I love you too! ❤️")
        break
    else:
        print(responses[index])
        index = (index + 1) % len(responses)