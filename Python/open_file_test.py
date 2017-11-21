#常规方式覆盖文件内容，若文件不存在，则新建
fp = open("../../Documents/open file link_test","w")
fp.write("new text\n")
fp.close
#常规方式打开文件
fp = open("../../Documents/open file link_test")
for line in fp:
    print(line)
fp.close
#with方式编辑文件，若文件不存在，则新建
with open("../../Documents/open file link_test","a") as with_open_file:
    with_open_file.write("write by with function\n")
#with方式打开文件
with open("../../Documents/open file link_test","r") as with_open_file:
    print(with_open_file.read())
