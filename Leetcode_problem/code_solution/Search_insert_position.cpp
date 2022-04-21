class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
     int si=0;
     int ei=(nums.size()-1);
    int index=0;
        while(si<=ei){
            int mid=(si+ei)/2;
            if (nums[mid]==target){
                index+=mid;
                
                break;
            }
            else if (nums[mid]>target){
                ei=mid-1;
                if (nums[si]>target){
                    index+=si;
                    break;
                }
                else if (nums[ei]<target){
                    index+=(++ei);
                    break;
                }
            }
            else if(nums[mid]<target){
                si=mid+1;
                if (nums[ei]<target){
                    index+=(++ei);
                    break;
                }
                else if (nums[si]>target){
                    index+=(si);
                    break;
                }
                    
                }
            }
    
    return index;  
    }
};
