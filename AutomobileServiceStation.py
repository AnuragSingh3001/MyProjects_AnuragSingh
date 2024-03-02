import mysql.connector as project
import datetime
print("________________________________")
print("|>>>>>>>QuickFIX Motors<<<<<<<<|")

# Global variables
conn = None
cursor = None


def connect_to_database():
    global conn, cursor
    try:
        conn = project.connect(host="localhost", user="root", passwd="Pythonsql@123", database="anudb")
        cursor = conn.cursor()
    except project.Error as e:
        print(f"Error connecting to MySQL: {e}")


def close_database_connection():
    global conn, cursor
    if conn and conn.is_connected():
        cursor.close()
        conn.close()


def password(username):
    new_password = input("Enter new strong password: ")
    if len(new_password) >= 8:
        try:
            hashed_password = "@@".join(new_password)
            sql = "UPDATE user1_info SET pass = %s WHERE username = %s"
            values = (hashed_password, username)
            cursor.execute(sql, values)
            conn.commit()
            print("Password updated. Please login again.")
        except project.Error as e:
            print(f"Error updating password: {e}")
    else:
        print("Password must be at least 8 characters long.")


def update_phone(username):
    new_phone = input("Enter 10-digit new phone number: ")
    if len(new_phone) == 10 and new_phone.isdigit():
        try:
            sql = "UPDATE user1_info SET phone = %s WHERE username = %s"
            values = (new_phone, username)
            cursor.execute(sql, values)
            conn.commit()
            print("Phone number updated. Please login again.")
            login()
        except project.Error as e:
            print(f"Error updating phone number: {e}")
    else:
        print("Invalid phone number format.")


def book():

    print("----------------------------------------")
    print("****VEHICLE TYPE AND SERVICING RATES****")
    print("----------------------------------------")
    print("| S.No|    VEHICLE TYPE     |   RATE   |")
    print("| [1] |HATCHBACK            | RS  3000 |")
    print("| [2] |SEDAN                | RS  3700 |")
    print("| [3] |SUV                  | RS  5000 |")
    print("| [4] |HATCHBACK(IMPORTED)  | RS  5500 |")
    print("| [5] |SEDAN(IMPORTED)      | RS  6300 |")
    print("| [6] |SUV(IMPORTED)        | RS  7000 |")
    print("| [7] |SUPER CAR(ANY)       | RS 13000 |")
    print("----------------------------------------")

    x = int(input("ENTER VEHICLE TYPE'S S.No:"))

    if x == 1:
        print("CAR TO BE SERVICED IS A HATCHBACK ")
        s = 3000
    elif x == 2:
        print("CAR TO BE SERVICED IS A SEDAN ")
        s = 3700
    elif x == 3:
        print("CAR TO BE SERVICED IS A SUV ")
        s = 5000
    elif x == 4:
        print("CAR TO BE SERVICED IS AN IMPORTED HATCHBACK ")
        s = 5500
    elif x == 5:
        print("CAR TO BE SERVICED IS AN IMPORTED SEDAN ")
        s = 6300
    elif x == 6:
        print("CAR TO BE SERVICED IS AN IMPORTED SUV ")
        s = 7000
    elif x == 7:
        print("CAR TO BE SERVICED IS A SUPER CAR ")
        s = 13000
    else:
        print("Invalid option")

    print("SERVICE AMOUNT =", s, "\n")

    print("-------------------------------------------------")
    print("***********CHOOSE ADDITIONAL SERVICES************")
    print("-------------------------------------------------")
    print("| S.No|     ADDITIONAL SERVICE        |   RATE  |")
    print("| [1] |   PAINT JOB                   | RS 1400 |")
    print("| [2] |   RIM CHANGE                  | RS 1200 |")
    print("| [3] |   INTERIOR CHANGE             | RS 1500 |")
    print("| [4] |   NEW TYRES                   | RS 1000 |")
    print("| [5] |   PAINT JOB & RIM CHANGE      | RS 2800 |")
    print("| [6] |   INTERIOR CHANGE & NEW TYRES | RS 2200 |")
    print("| [7] |   COMPLETE MAKEOVER           | RS 4500 |")
    print("| [8] |   NONE                        | RS 0000 |")
    print("-------------------------------------------------")

    n = int(input("ENTER ADDITIONAL SERVICE'S S.No:"))

    if n == 1:
        print("PAINT JOB TO BE DONE ")
        p = s+1400
    elif n == 2:
        print("RIM CHANGE TO BE DONE ")
        p = s+1200
    elif n == 3:
        print("INTERIOR CHANGE TO BE DONE ")
        p = s+1500
    elif n == 4:
        print("NEW TYRES TO BE ADDED ")
        p = s+1000
    elif n == 5:
        print("PAINT JOB AND RIM CHANGE TO BE DONE ")
        p = s+2800
    elif n == 6:
        print("INTERIOR CHANGE AND NEW TYRES TO BE ADDED ")
        p = s+2200
    elif n == 7:
        print("COMPLETE MAKEOVER TO BE DONE ")
        p = s+4500
    elif n == 8:
        print("NO ADDITIONAL SERVICE REQUIRED ")
        p = s+0
    else:
        print("Invalid option")

    print("TOTAL SERVICING COST :RS ", p, "\n")

    print("Book function code here")
    # Gather necessary information from user
    name = input("Enter customer name: ")
    vno = input("Enter vehicle number: ")
    maker_name = input("Enter maker name: ")
    model_type = input("Enter model type: ")
    phone = input("Enter customer phone number: ")
    user_id = int(input("Enter user ID: "))
    price = float(input("Enter servicing cost as displayed:RS "))
    mechanic = input("Enter mechanic name: ")
    book_date = datetime.datetime.now()

    try:
        sql = "INSERT INTO create_receipt (name, vno, maker_name, model_type, phone, user_id, book_date, price, " \
              "mechanic) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, vno, maker_name, model_type, phone, user_id, book_date, price, mechanic)
        cursor.execute(sql, values)
        conn.commit()
        print("Receipt created successfully.")
        main()
    except project.Error as e:
        print(f"Error creating receipt: {e}")


def update():
    print("Update function code here")
    # Gather necessary information from user
    user_ch_3 = input("Enter 1 for updating phone, 2 for updating password, and any other key to exit: ")

    if user_ch_3 == '1':
        username = input("Enter username: ")
        update_phone(username)
    elif user_ch_3 == '2':
        username = input("Enter username: ")
        password(username)
    else:
        print("Exiting update menu.")


def view_receipt():
    print("View receipt function code here")
    phone = input("Enter customer phone number: ")
    user_id = int(input("Enter user ID: "))

    try:
        sql = "SELECT * FROM create_receipt WHERE phone = %s AND user_id = %s"
        values = (phone, user_id)
        cursor.execute(sql, values)
        receipts = cursor.fetchall()

        if receipts:
            for receipt in receipts:
                print("Receipt ID:", receipt[0])
                print("Customer Name:", receipt[1])
                print("Vehicle Number:", receipt[2])
                print("Maker Name:", receipt[3])
                print("Model Type:", receipt[4])
                print("Phone:", receipt[5])
                print("User ID:", receipt[6])
                print("Book Date:", receipt[7])
                print("Price:", receipt[8])
                print("Mechanic:", receipt[9])
                print("--------------------")
                main()
        else:
            print("No receipts found for the given phone number and user ID.")
    except project.Error as e:
        print(f"Error fetching receipts: {e}")


def delete():
    print("Delete function code here")
    # Gather necessary information from user
    user_id = int(input("Enter user ID to delete: "))

    try:
        sql = "DELETE FROM user1_info WHERE user_id = %s"
        values = (user_id,)
        cursor.execute(sql, values)
        conn.commit()
        print("User deleted successfully.")
        main()
    except project.Error as e:
        print(f"Error deleting user: {e}")


def generate_receipt():
    print("Generate receipt function code here")
    # Gather necessary information from user
    user_id = int(input("Enter user ID: "))

    try:
        sql = "SELECT * FROM create_receipt WHERE user_id = %s"
        values = (user_id,)
        cursor.execute(sql, values)
        receipts = cursor.fetchall()

        for receipt in receipts:
            filename = f"Receipt_{receipt[1]}_{receipt[2]}.txt"
            with open(filename, "w") as file:
                file.write(f"Receipt ID: {receipt[0]}\n")
                file.write(f"Customer Name: {receipt[1]}\n")
                file.write(f"Vehicle Number: {receipt[2]}\n")
                file.write(f"Maker Name: {receipt[3]}\n")
                file.write(f"Model Type: {receipt[4]}\n")
                file.write(f"Phone: {receipt[5]}\n")
                file.write(f"User ID: {receipt[6]}\n")
                file.write(f"Book Date: {receipt[7]}\n")
                file.write(f"Price: {receipt[8]}\n")
                file.write(f"Mechanic: {receipt[9]}\n")
            print(f"Receipt generated as {filename}")
            main()
    except project.Error as e:
        print(f"Error generating receipts: {e}")


def issue():
    print("Issue function code here")
    # Gather necessary information from user
    phone = input("Enter customer phone number: ")
    issue_text = input("Enter issue: ")

    try:
        sql = "INSERT INTO report (phone, issue) VALUES (%s, %s)"
        values = (phone, issue_text)
        cursor.execute(sql, values)
        conn.commit()
        print("Issue reported successfully.")
        main()
    except project.Error as e:
        print(f"Error reporting issue: {e}")


def report():
    print("Report function code here")
    # Gather necessary information from user
    phone = input("Enter customer phone number: ")

    try:
        sql = "SELECT * FROM report WHERE phone = %s"
        values = (phone,)
        cursor.execute(sql, values)
        issues = cursor.fetchall()

        if issues:
            for issue in issues:
                print("Issue ID:", issue[0])
                print("Phone:", issue[1])
                print("Issue:", issue[2])
                print("--------------------")
                main()
        else:
            print("No issues reported for the given phone number.")
    except project.Error as e:
        print(f"Error fetching issues: {e}")


def logout():
    print("Logout function code here")
    # Simply reset the global user_id to empty string
    global user_id
    user_id = ""
    print("You have been logged out.")
    main()


def main():
    try:
        print("------------\n1. Book a Slot\n2. View Receipt\n3. Report Issue\n4. View Report\n5. Generate Receipt\n"
              "6. Log Out\n---------------")
        user_choice = input("Enter your choice: ")
        if user_choice == '1':
            book()
        elif user_choice == '2':
            view_receipt()
        elif user_choice == '3':
            issue()
        elif user_choice == '4':
            report()
        elif user_choice == '5':
            generate_receipt()
        elif user_choice == '6':
            logout()
        else:
            print("Invalid input")
            main()
    except project.Error as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        close_database_connection()


def desc():
    print("Description function code here")
    print("HELLO USER! THIS SYSTEM HAS BEEN CREATED FOR YOUR AUTOMOBILE SERVICE STATION\n"
          "USING WHICH YOU WOULD BE ABLE TO BOOK SLOTS, ASSIGN JOBS, AND CREATE RECEIPTS FOR YOUR CUSTOMERS.\n"
          "IT ALSO COMES WITH THE SIGNUP AND LOGIN FEATURE")
    log_sign()


def login():
    try:
        phone = input("Enter your 10-digit phone number: ")
        password = input("Enter your password: ")
        if len(phone) == 10 and phone.isdigit() and len(password) >= 8:
            try:
                sql = "SELECT * FROM user1_info WHERE phone = %s AND pass = %s"
                values = (phone, password)
                cursor.execute(sql, values)
                user_data = cursor.fetchone()
                if user_data:
                    user_id = user_data[0]
                    main()
                else:
                    print("Incorrect phone number or password.")
                    login()
            except project.Error as e:
                print(f"Error logging in: {e}")
        else:
            print("Invalid phone number or password format.")
            login()
    except KeyboardInterrupt:
        print("Exiting...")
        close_database_connection()


def signup():
    try:
        username = input("Enter a username: ")
        password = input("Enter a strong password (at least 8 characters): ")
        phone = input("Enter your 10-digit phone number: ")
        if len(password) >= 8 and len(phone) == 10 and phone.isdigit():
            try:
                sql = "INSERT INTO user1_info (username, pass, phone) VALUES (%s, %s, %s)"
                values = (username, password, phone)
                cursor.execute(sql, values)
                conn.commit()
                print("Account created successfully. Please login.")
                log_sign()
            except project.Error as e:
                print(f"Error creating account: {e}")
        else:
            print("Invalid input format. Password must be at least 8 characters long, and phone number must be "
                  "10 digits.")
            signup()
    except KeyboardInterrupt:
        print("Exiting...")
        close_database_connection()


def log_sign():
    try:
        print("________________________________\n| Registered User ---> Press(1)|\n|  New User       ---> Press(2)|\n"
              "________________________________")
        choice = input("")
        if choice == '1':
            login()
        elif choice == '2':
            signup()
        else:
            print("Invalid choice")
            log_sign()
    except KeyboardInterrupt:
        print("Exiting...")
        close_database_connection()


# Main program
try:
    connect_to_database()
    user_id = ""
    if user_id == "":
        log_sign()
    if user_id != "":
        main()
except project.Error as e:
    print(f"Error: {e}")
finally:
    close_database_connection()
