def create_user_profile(username, age=18, premium=False):
    if premium:
        user_type = "Premium User"
    else:
        user_type = "Standard User"

    return f"{username} (age: {age}) - {user_type}"


# ตัวอย่างการใช้งาน
print(create_user_profile("Alice"))
print(create_user_profile("Bob", 25))
print(create_user_profile("Charlie", 30, True))
