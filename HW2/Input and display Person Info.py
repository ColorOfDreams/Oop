import sys
sys.stdout.reconfigure(encoding='utf-8')

class NhanVien:
    """
    Lớp nhân viên, khai báo định nghĩa và đặt ra điều kiện cho lớp
    """
    def __init__(self, name='Huy', salary=200.0, address="Hưng Yên"):
        self.name = name
        self.salary = salary
        self.address = address

    def __str__(self):
        return f"Tên: {self.name}; Lương cơ bản: {self.salary}; Địa chỉ: {self.address}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Yêu cầu họ tên không trống và chỉ được chứa kí tự chữ.")
        self._name = value.strip()

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Yêu cầu địa chỉ không trống và chỉ được chứa kí tự chữ.")
        self._address = value.strip()

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Yêu cầu lương phải là số và có giá trị lớn hơn 0.")
        self._salary = value

def input_nhan_vien():
    """
    Hàm nhập thông tin nhân viên từ người dùng, giao việc xác thực cho setter trong class NhanVien.
    """
    while True:
        try:
            name = input("Nhập tên nhân viên: ").strip()
            address = input("Nhập địa chỉ nhân viên: ").strip()
            salary = float(input("Nhập lương nhân viên: ").strip())

            # Tạo đối tượng nhân viên (setter sẽ xử lý mọi lỗi)
            return NhanVien(name=name, address=address, salary=salary)
        except ValueError as e:
            print(f"Lỗi: {e}. Vui lòng nhập lại thông tin.\n")




def InsertionSorting(lst):
    """
    Sắp xếp danh sách nhân viên theo lương bằng thuật toán Insertion Sort.
    """
    n = len(lst)

    for i in range(1,n):
        x = lst[i]
        j = i - 1

        while(x < lst[j] and j >=0):
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = x



def main():
    """
    Chương trình chính để nhập và hiển thị thông tin nhân viên.
    """
    nhan_vien_list = []

    for i in range(3):  # Nhập thông tin cho 3 nhân viên
        print(f"\nNhập thông tin cho nhân viên {i + 1}:")
        nhan_vien = input_nhan_vien()
        nhan_vien_list.append(nhan_vien)

    print("\nDanh sách nhân viên vừa nhập:")
    for nv in nhan_vien_list:
        print(nv)

    # Sắp xếp danh sách nhân viên theo lương
    InsertionSorting(nhan_vien_list)

    print("\nDanh sách nhân viên sau khi sắp xếp theo lương:")
    for nv in nhan_vien_list:
        print(nv)


if __name__ == "__main__":
    main()

    

