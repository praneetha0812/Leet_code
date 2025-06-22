class Solution {
    public int fib(int n) {
        if (n<=1){
            return n;
        }
           int last = 0;
        int secondlast =1; 
        int temp =0;
      for(int i=2; i<=n; i++){
     
        temp = last+ secondlast;
        last = secondlast;
        secondlast = temp;
      }
         return temp;
    }
}