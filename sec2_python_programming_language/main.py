
def main():
    print("Hey this is my first project on python :)")


    int_ = int(input("Enter Your Number : "))

    print(int_)


def main():
    print("Hey this is the first one to go")
    
    while True:    
        try:
            num = int(input("Enter The Number you want: "))
            break
        except Exception as err:
            print(f"An error ocurred as {err}")
            print("Try Again with a valid input :) \n")
            continue
        
    print("".join(str(num) + " " for num in range(1, num+1)))
        
    return
        
if __name__ == "__main__":
    main()
    


