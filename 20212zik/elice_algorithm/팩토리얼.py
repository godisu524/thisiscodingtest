factorials = [0,1,2]
def factorial(num):
    if num <= len(factorials):
        return factorials[num]
    else:
        for i in range(3,num+1):
            i = factorials.append(i*factorials[-1])
    return factorials[num]
    

def main():
    print(factorial(5)) # should return 120

if __name__ == "__main__":
    main()