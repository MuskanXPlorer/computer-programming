'''Write a piece of code to find the longest common prefix among a list of strings.'''
strs = ["flower", "flow", "flight"]
if not strs:
    print("")
else:
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                print("")
                break
    print(prefix) 
  # Output: "fl"
