# class XYZ:
#     def __init__(self,name,address,o_amount,n_amount):
#         self.name=name
#         self.address=address
#         self.o_amount=o_amount
#         self.n_amount=n_amount


#     def Tiennuoc(self):
#         self.tong=self.amount*8000
#         # self.tong=tong
#         return f'Tên chủ hộ: {self.name}\nĐịa chỉ: {self.address}\ntiền nước cần trả là {self.tong} đồng'
    

# class A(XYZ):
#     def __init__(self, name, address, o_amount, n_amount, person):
#         super().__init__(name, address, o_amount, n_amount)
#         self.person=person
#         self.amount=(self.n_amount-self.o_amount)-5*self.person

# class B(XYZ):
#     def __init__(self, name, address, o_amount, n_amount):
#         super().__init__(name, address, o_amount, n_amount)
#         self.amount=(self.n_amount-self.o_amount)*80/100

# class C(XYZ):
#     def __init__(self, name, address, o_amount, n_amount, work_related_person):
#         super().__init__(name, address, o_amount, n_amount)
#         self.work_related_person=work_related_person
#         self.amount=(self.n_amount-self.o_amount)-10*self.work_related_person


    
    
# r1=A("Andrew","greenstreet",6000,8000,4)
# print(r1.Tiennuoc())





class ABC:
    def __init__(self,code, name, birth_year, gender, salary_ratio,start_year):
        self.code=code
        self.name=name
        self.birth_year=birth_year
        self.gender=gender
        self.salary_ratio=salary_ratio
        self.start_year=start_year


class A(ABC):
    