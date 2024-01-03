class Main {
  public static void main(String[] args) {
    tryNum(3);
  }
  public static void tryNum(int num){
    try{
      checkEven(num);
      System.out.println("This number is even");
    }
    catch(IllegalArgumentException e){
      System.out.println("Error: " + e.getMessage());
    }
  }
  public static void checkEven(int num){
    if(num %2 != 0){
      throw new IllegalArgumentException("Odd number");
    }
  }
}