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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* a=l1;
      ListNode* b=l2;
      ListNode* dummy=new ListNode(-1);
      ListNode* prev=dummy;
      while(a && b){
        if(a->val>=b->val){
          prev->next=b;
          b=b->next;
          prev=prev->next;
        }
        else{
          prev->next=a;
          a=a->next;
          prev=prev->next;
        }
      }
      if(a) prev->next=a;
      if(b) prev->next=b;
      return dummy->next;
    }
};