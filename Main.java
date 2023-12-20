import java.util.Scanner;
class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    System.out.println("Input the first number");
    int num1 = in.nextInt();
    System.out.println("Input the second number");
    int num2 = in.nextInt();
    int result = addNums(num1, num2);
    System.out.println("The result is " + result);
  }
public static int addNums(int num1, int num2) {
  int result = num1 + num2;
  return result;
}
}