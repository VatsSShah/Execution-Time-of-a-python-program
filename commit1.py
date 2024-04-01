from time import time

# Python program to create acronyms
word = "Artificial Intelligence"

start = time()  # Start measuring time here

text = word.split()
acronym = " "
for i in text:
    acronym = acronym + str(i[0]).upper()

print(acronym)

end = time()  # End measuring time here
execution_time = end - start
print("Execution Time:", execution_time)
