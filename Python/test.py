class Project(object):

    def __init__(self, pro_name, pro_begin, pro_end):
        self.pro_name = pro_name
        self.pro_begin = pro_begin
        self.pro_end = pro_end


    def a(self,pro_name, pro_begin, pro_end):
        self.pro_name = pro_name
        self.pro_begin = pro_begin
        self.pro_end = pro_end
        print('%s: %s- %s' % (self.pro_name, self.pro_begin, self.pro_end))



#print(Pro.pro_name,Pro.pro_begin,Pro.pro_end)

    def print_score(self):
        # print('%s: %s- %s' % (self.pro_name, self.pro_begin ,self.pro_end))
        return self.pro_name, self.pro_begin ,self.pro_end

#Pro = Project('AUX', '201805', '201905')

Pro = Project('A','B','C')

Pro.a('1','2','3')

# Pro.print_score()
print(Pro.print_score())
# print(print())