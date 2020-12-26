# Problem: Create a funciton that reverses a string.
#   Input: "Hi My Name is Daniel"
#  Output: "lienaD si emaN yM iH"


def reverse(str):
  reversed = []
  for x in range (len(str)-1, -1, -1):
    reversed.append(str[x])
  return ''.join(reversed)

def reverse2(str):
  return str[::-1]


print(reverse("Daniel"))
print(reverse2("Daniel"))