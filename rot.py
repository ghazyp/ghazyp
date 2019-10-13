# Ghazy P.
# Reverse Rot solution
# rot.py

def main():
    file = open("rot.in", 'r')
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    result = ""

    for line in file:
        white_space = line.find(" ")
        N = line[:white_space] # get the integers
        plain = line[white_space+1:-1] # get the entire string
        reverse = plain[::-1] # reverse the string
        
        for c in reverse:
            x = alphabet.index(c)
            result += alphabet[(x + int(N)) % len(alphabet)]
        result += '\n'
    print(result, end="")
                  
main()
