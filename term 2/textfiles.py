try:
    ##def second(elem):
    ##    return elem[1]
    ##names = []
    ##scores = []
    ##sets = []
    ##name = " "
    ##
    ##
    ##text_file = open("readme.txt","r")
    ##lines = text_file.readlines()
    ##
    ##for i in range(len(lines)):
    ##    lines[i] = lines[i].strip("\n")
    ##
    ##while name:
    ##    name = text_file.readline().strip("\n")
    ##    score = text_file.readline().strip("\n")
    ##    print(score)
    ##    names.append(name)
    ##    scores.append(score)
    ##    pair = [name,score]
    ##    sets.append(pair)
    ##sets.sort(key=second,reverse = True)
    ##print (sets)
    ##
    ##print(lines)
    ##text_file.close()
    ##
    ##
    tf = open("readme.txt", "w")


    tf.write("this is line 1\n")
    line2 = "this is line 2\n"
    tf.write(line2)
    line3 = 69
    line3 = str(line3)
    tf.write(line3)
    lines =["\nthis is line 1\n", "making this line 2\n",
            "and this line 3"]
    tf.writelines(lines)

    tf.close()
