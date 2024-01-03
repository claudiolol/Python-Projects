class Main {
  public static void main(String[] args) {
    int[] numbers = new int[] {7, 4, 6, 2, 8, 6};
    double result = average(numbers);
    System.out.println("Results: " + result);
  }
  public static double average(int[] nums) {
    double sum = 0;
    for(int i = 0; i < nums.length; i++){
      sum += nums[i];
    }
    double avg = sum / nums.length;
    return avg;

  }
  
}
