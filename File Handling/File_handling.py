import os
#
# with open("readme.txt", "r+", encoding="UTF-8") as f:
#     f.truncate()

os.rename("readme.txt", "test.txt")

# file = "readme.txt"
# if os.path.exists(file):
#     os.remove(file)
#     print("File deleted successfully")
# else:
#     print("File is not present")
