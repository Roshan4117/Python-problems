
import java.util.Scanner;

class plaindrome {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter the String: ");
        String original = in.nextLine();
        StringBuilder sb = new StringBuilder(original);
        String reverse = sb.reverse().toString();
        if (original.equals(reverse)) {
            System.out.println("plindrome");
        } else {
            System.out.println("Not Plindrome");
        }

    }
}
