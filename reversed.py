input =[[1, 2], [3, 4], [5, 6, 7]]
#output: [[[7, 6, 5], [4, 3], [2, 1]]
input=input[::-1]

for i in range(len(input)):
    (input[i])=(input[i])[::-1]
print(input)