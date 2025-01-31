
import java.util.Scanner;

class palindrome {

    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            System.out.println("Enter the String: ");
            String original = in.nextLine();
            StringBuilder sb = new StringBuilder(original);
            String reverse = sb.reverse().toString();
            if (original.equals(reverse)) {
                System.out.println("palindrome");
            } else {
                System.out.println("Not Palindrome");
            }
        }

    }
}
