class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
        string s="";
        int min=strs[0].size();
        int flag=1;
        for(int i=0;i<min;i++){
            char ele=strs[0][i];
            
            for(int j=1;j<strs.size();j++){
                if (ele!=strs[j][i]){
                    flag=0;
                    break;
                }
                
            }
            if(flag==0)
                break;
         s+=ele;
        }
    return s;
    }
};
