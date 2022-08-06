class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        priority_queue<int>mx;
        priority_queue<int,vector<int>,greater<int>>mi;
      int m=nums1.size();
      int n=nums2.size();
        vector<int>ans;
      int i=0;
      int j=0;
      while(i<m && j<n){
        if(nums1[i]<=nums2[j]){
          ans.push_back(nums1[i]);
          i++;
        }else{
          ans.push_back(nums2[j]);
          j++;
        }
      }
      while(i<m){
        ans.push_back(nums1[i]);
        i++;
      }
      while(j<n){
        ans.push_back(nums2[j]);
        j++;
      }
      i=0;
      for(i=0;i<m+n;i++){
           if(mx.size()==mi.size()){
             mx.push(ans[i]);
             if(mi.size() && mi.top()<mx.top()){
               int x=mi.top();
               int y=mx.top();
               mi.pop();
               mx.pop();
               mx.push(x);
               mi.push(y);
             }
           }else{
             mi.push(ans[i]);
             if(mi.top()<mx.top()){
               int x=mi.top();
               int y=mx.top();
               mi.pop();
               mx.pop();
               mx.push(x);
               mi.push(y);
             }
           }
        }
      if(mx.size()==mi.size()){
        double l=(double)(mi.top()+mx.top())/2;
        return l;
      }
      else{
        return (double)(mx.top());
      }
    }
};