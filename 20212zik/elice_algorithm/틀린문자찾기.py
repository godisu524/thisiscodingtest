
def findDifference(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    
    for letter in str1:
        str2.remove(letter)
    
    return str2[0]

def main():
    print(findDifference("apple", "azlppe"))
    

if __name__ == "__main__":
    main()
