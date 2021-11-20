def wordPattern(pattern, strList):
    visited={}
    patterns = list(pattern)
    for n,letter in enumerate(patterns):
        if letter not in visited:
            visited[letter] = strList[n]
    for n,letter in enumerate(patterns):
        if visited[letter] != strList[n]:
            return False
    
        
        
            
    
    return True

def main():
    print(wordPattern("aabb", ["elice", "elice", "alice", "alice"])) # should return True
    print(wordPattern("abab", ["elice", "elice", "alice", "alice"])) # should return False
    

if __name__ == "__main__":
    main()
