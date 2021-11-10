# Mở file để ghi
n = open("data.txt", "w")

# Ghi dữ liệu lên file
n.write("Tobe or not tobe. \n  helloword ! \n");

# Close opened file
n.close()

print("Ghi file thanh cong !")
# Mở file để đọc dữ liệu
n = open("data.txt", "r+")

# Đọc một chuỗi trong file
str = n.read(20)

# In ra chuỗi được đọc
print("Chuỗi được đọc là: ", str)

# Đóng file lại