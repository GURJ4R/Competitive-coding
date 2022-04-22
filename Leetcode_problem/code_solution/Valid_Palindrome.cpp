class Solution {
public:
    bool isPalindrome(string s) {
        string new_s="";
        for(auto i:s){
            if (i>=65 && i<=90)
            {
                new_s+=i+32;
                }
            else if (i>=97 && i<=122){
                new_s+=i;
                }
            else if(i>=48 &&i<=57){
                new_s+=i;
            }
            else{
                continue;
            }
        }
        int i=0;
        int j=new_s.size()-1;
        while(i<j){
            if (new_s[i]!=new_s[j]){
                
                return false;
            }
            i++;
            j--;
                
            }
        
        
        return true;
        
    }
};
