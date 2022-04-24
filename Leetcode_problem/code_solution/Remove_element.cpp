class Solution {
public:
    int removeElement(vector<int>& myvector, int val) {
        int s=myvector.size();
        int x=0;
        for (auto i = myvector.begin(); i != myvector.end(); ++i) {
        if (*i == val) {
            myvector.erase(i);
            i--;
            x++;
        }
    }
        
  
        return s-x;
    }
};
