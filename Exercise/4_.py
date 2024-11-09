password = "123456124545545454"

pass_len = len(str(password))
if pass_len < 6:
    print("Password must be at least 6 characters long. Your password is weak")
elif pass_len < 10:
    print("Password must be at least 10 characters long. Your password is moderate")
else:
    print("Password is strong")
