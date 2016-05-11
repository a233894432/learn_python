# from sys import argv
#
# script, filename = argv
#
# txt = open(filename)
#
# print "Here's your file %r:" % filename
# print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again, 'w')

# 清空文件数据
txt_again.truncate()

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

txt_again.write(line1)
txt_again.write("\n")
txt_again.write(line2)
txt_again.write("\n")
txt_again.write(line3)
txt_again.write("\n")

print "And finally, we close it."
txt_again.close()
