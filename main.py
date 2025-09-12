from user_manager import save_user, load_users

def main():
    users = load_users()

    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))  # may raise ValueError
        user = {"name": name, "age": age}
        users.append(user)

        save_user(users)

    except ValueError:
        print("Error: Age must be a number!")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
