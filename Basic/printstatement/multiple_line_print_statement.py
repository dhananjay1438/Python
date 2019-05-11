# We can write multiple lines with the help of triple delimeter (' or ")

# If you write like this there will be tab at start of first 2 lines and there will be 2 tabs
# at the third line as python will consider pre tabbed as tabbed space by the user so you must start
# writing adjacent print's 'p'

print("This is first line")
print("""
    This thing will be formated
    This will be on next line
        This will be formated with tab as well""")

######################################################
# This is the output of the above line(s)
######################################################
#     This thing will be formated
#     This will be on next line
#         This will be formated with tab as well

# Even writing like this will cause print statements to get printed one line below as it will leave one line
# as we left it while typing
print("""
Hello this will start without any tab(space)
This is next line
    This line will start with tab""")

######################################################
# This is the output of the above line(s)
######################################################
# Hello this will start without any tab(space)
# This is next line
#   This line will start with tab
