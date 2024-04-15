import pixela
from utils import clear_screen

def main():
    logged_in_user = None
    logged_in_token = None

    while True:
        if not logged_in_user:
            print("Pixela API Interaction")
            print("1. Login")
            print("2. Create User")
            print("3. Exit \n")
            choice = input("Enter your choice: ")
            if choice == '1':
                logged_in_user, logged_in_token = pixela.login()
            elif choice == '2':
                pixela.create_user()
            elif choice == '3':
                break
            else:
                print("Invalid choice.")
        else:
            user_graphs = pixela.get_user_graphs(logged_in_user, logged_in_token)
            print(f"Pixela API Interaction (Logged in as {logged_in_user})")
            print("1. Create Graph")
            print("2. Post Pixel")
            print("3. Update Pixel")
            print("4. Delete Pixel")
            print("5. Get User Graphs")
            print("6. Logout")
            print("7. Exit \n")
            user_choice = input("Enter your choice: ")
            if user_choice == '1':
                pixela.create_graph(logged_in_user, logged_in_token, user_graphs)
            elif user_choice == '2':
                pixela.post_pixel(logged_in_user, logged_in_token, user_graphs)
            elif user_choice == '3':
                pixela.update_pixel(logged_in_user, logged_in_token, user_graphs)
            elif user_choice == '4':
                pixela.delete_pixel(logged_in_user, logged_in_token, user_graphs)
            elif user_choice == '5':
                pixela.print_graphs(user_graphs)
            elif user_choice == '6':
                logged_in_user = None
                logged_in_token = None
                print("Logged out.")
            elif user_choice == '7':
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
