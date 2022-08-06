/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
      ListNode* a=l1;
      ListNode* b=l2;
      int carry=0;
      ListNode* ans=new ListNode(-1);
      ListNode* prev=ans;
      while(a || b){
        int x=a==NULL?0:a->val;
        int y=b==NULL?0:b->val;
        int sum=x+y+carry;
        prev->next=new ListNode(sum%10);
        carry=sum/10;
        prev=prev->next;
        if(a)a=a->next;
        if(b)b=b->next;
      }
      if(carry) prev->next=new ListNode(carry);
      return ans->next;
    }
};