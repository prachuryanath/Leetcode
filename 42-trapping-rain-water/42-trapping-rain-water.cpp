class Solution {
public:
    int trap(vector<int>& A) {
      vector<int>left(A.size());
      vector<int>right(A.size());
      int n=A.size();
      left[0]=A[0];
      for(int i=1;i<n;i++){
        left[i]=max(left[i-1],A[i]);
      }
      right[n-1]=A[n-1];
      for(int i=n-2;i>=0;i--){
        right[i]=max(right[i+1],A[i]);
      }
      
      int sum=0;
      for(int i=0;i<n;i++){
        sum+= abs(A[i]-min(left[i],right[i]));
      }
      return sum;
      
    }
};