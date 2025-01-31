public class fact {

        static int factorial(int n){
            if ( n == 0)
            return 1;
            else
            return (n * factorial(n-1));
        }
    public static void main(String[]args){
        int number = 4;
        int facto = factorial(number);
        System.out.println("factorial of "+number+ " is " + facto);
        }
    }
    
