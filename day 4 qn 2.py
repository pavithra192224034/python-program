def calculate_users(total_users, staff_users):
    student_users = total_users - staff_users
    non_teaching_staff_users = staff_users // 3
    total_staff_users = staff_users + non_teaching_staff_users
    return student_users, non_teaching_staff_users, total_staff_users

def main():
    total_users = int(input("Enter the total number of users: "))
    staff_users = int(input("Enter the number of staff users: "))

    student_users, non_teaching_staff_users, total_staff_users = calculate_users(total_users, staff_users)

    print(f"Number of Student Users: {student_users}")
    print(f"Number of Non-Teaching Staff Users: {non_teaching_staff_users}")
    print(f"Number of Total Staff Users: {total_staff_users}")

if __name__ == "__main__":
    main()




