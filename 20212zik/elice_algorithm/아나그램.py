def isAnagram(str1, str2):
    str1=list(str1).sort()
    str2=list(str2).sort()
    if str1==str2:
        return True
    else:
        return False
    return None

def main():
    print(isAnagram('iamlordvoldemort', 'tommarvoloriddle')) # should return True
    print(isAnagram('cat', 'cap')) #should return False
    

if __name__ == "__main__":
    main()
