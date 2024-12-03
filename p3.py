import string
def pass_generator():
    len_pass=int(input("Enter the length of your pass (min 10):"))
    if len_pass <10:
        print("The length is invalid")
        return
    user_pass=input(f"Enter your password of {len_pass} characters:")
    if len(user_pass) != len_pass:
        print("Your password does not valid length")
        return
    if(any(c.islower() for c in user_pass) and
       any(c.isupper() for c in user_pass) and
       any(c.isdigit() for c in user_pass) and
       any(c in "#@&$" for c in user_pass)):
       print("Your password is valid!")
    else:
        print("Your password is invalid")
pass_generator()
       