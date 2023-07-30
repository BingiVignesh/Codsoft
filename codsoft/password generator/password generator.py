import string,random
def generate(n):
    s1 = string.ascii_letters
    s2=string.digits
    s3=string.punctuation

    final = s1+s2+s3

    l1 = list(final)
    random.shuffle(l1)

    pw_list = []

    i=0
    while i<n:
        pw_list.extend(random.choice(l1))
        i+=1

    random.shuffle(pw_list)
    password = ''.join(pw_list)
    print("Password: "+password)


if __name__ == "__main__":
    c="y"
    while c=="y":
        try:
            n = int(input("Enter desired length of password: "))
            generate(n)
            c=input("Do you want to generate another password? (y/n): ").lower()
        except:
            print("Please Enter integer value for length")
       

           

