# 2: Pseudocode
# ask user for input
input_str = input("What is your input string? ")
# check each character 
output_str = ""
for i in range(len(input_str)):
#   if a, change to *
    if input_str[i] == "a":
        output_str += "*"
    #   if e, change to &
    if input_str[i] == "e":
        output_str += "&"
    #   if i, change to #
    if input_str[i] == "i":
        output_str += "#"
    #   if o, change to +
    if input_str[i] == "o":
        output_str += "+"
    else:
        output_str += input_str[i]



#   if u, change to !
# print ouputs