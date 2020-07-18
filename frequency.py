try:
    with open(r"C:\Users\lenovo\Desktop\final project.txt", "w") as file:   #here you have to write the path directory on your pc, where your file is located.
        sentence = "There is something new"
        frequency = {}
        for words in sentence:
            if words != " ":
                frequency[words] = frequency.get(words, 0) + 1
                # this line is the shorter form of this ---> ⬇⬇⬇
                # if words in frequency:
                #   frequency[words] += 1
                # else:
                #   frequency[words] = 1
        
        sorts = sorted(frequency.items(),
                       key=lambda row: row[1],
                       reverse=True)
        mapping = map(lambda sort: "{} : {}".format(sort[0], sort[1]), sorts)
        file.write(f"Hi there! Welcome to this file."
                   f"\nHere is the sentence--> '{sentence}' \n"
                   f"And The number of frequency is given below:\n\n")
        for x in mapping:
            print(x)
            file.write("  {}\n".format(x))

except (ValueError, TypeError):
    print("You've inputted a wrong value")
