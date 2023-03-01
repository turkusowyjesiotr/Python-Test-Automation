class UserModel:
    def __init__(self, user_no, first_name, last_name, email, age, salary, department):
        self.user_no = user_no
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.salary = salary
        self.department = department

    def get_user_info_list(self):
        return [self.first_name, self.last_name, self.email, self.age, self.salary, self.department]
