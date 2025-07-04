# f=open("file1.txt",'r')
# text=f.read()
# f.close()


with open("file1.txt",'a') as f:  # it is used to access a file without the need of closing it after use (automatic close)
    f.write("I am using with function to write this\n")

#new=open("file99.txt",'x') this will create new file


#you can use 'rb' to read a file as binary  and 'rt' is default mode to read file as text
#using 'w' to read will delete prvious content in that file and will write the new one
#'a' i.e. append can be used to write new content in a file without deleting old content
#'x' can be used to create a new file