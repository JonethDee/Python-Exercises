greeting = input("Greetings")
greet = greeting.lower()

if "hello" in greet:
    print("$0")
elif "h" in greet[0]:
    print("$20")
else:
    print("$100")


