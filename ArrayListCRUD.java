import java.util.ArrayList;
import java.util.Scanner;

public class ArrayListCRUD {
    public static void main(String[] args) {
        // 1. Create an ArrayList of Strings
        ArrayList<String> list = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        int choice;

        do {
            // Menu
            System.out.println("\n--- ArrayList CRUD Operations ---");
            System.out.println("1. Create (Add Element)");
            System.out.println("2. Read (Display Elements)");
            System.out.println("3. Update (Modify Element)");
            System.out.println("4. Delete (Remove Element)");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();
            sc.nextLine(); // consume newline

            switch (choice) {
                case 1: // Create
                    System.out.print("Enter element to add: ");
                    String element = sc.nextLine();
                    list.add(element);
                    System.out.println("Element added!");
                    break;

                case 2: // Read
                    System.out.println("ArrayList Elements:");
                    for (int i = 0; i < list.size(); i++) {
                        System.out.println(i + ": " + list.get(i));
                    }
                    break;

                case 3: // Update
                    System.out.print("Enter index to update: ");
                    int indexToUpdate = sc.nextInt();
                    sc.nextLine(); // consume newline
                    if (indexToUpdate >= 0 && indexToUpdate < list.size()) {
                        System.out.print("Enter new value: ");
                        String newValue = sc.nextLine();
                        list.set(indexToUpdate, newValue);
                        System.out.println("Element updated!");
                    } else {
                        System.out.println("Invalid index!");
                    }
                    break;

                case 4: // Delete
                    System.out.print("Enter index to delete: ");
                    int indexToDelete = sc.nextInt();
                    sc.nextLine(); // consume newline
                    if (indexToDelete >= 0 && indexToDelete < list.size()) {
                        list.remove(indexToDelete);
                        System.out.println("Element removed!");
                    } else {
                        System.out.println("Invalid index!");
                    }
                    break;

                case 5: // Exit
                    System.out.println("Exiting...");
                    break;

                default:
                    System.out.println("Invalid choice! Try again.");
            }

        } while (choice != 5);

        sc.close();
    }
}
