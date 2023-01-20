//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

// } Driver Code Ends
class Solution {
  public:
    void printTriangle(int n) {
        // code here
        for(int i=0;i<n;i++){
            for(int j=0;j<(n*2);j++){
                if(j<=i){
                    cout<<j+1;
                }
                else{
                    cout<<" ";
                }
                if(j>=(n*2)-(i+1)){
                    cout<<n*2-(j);
                }
                else{
                    cout<<" ";
                }
            }
            cout<<"\n";
        }
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;

        Solution ob;
        ob.printTriangle(n);
    }
    return 0;
}
// } Driver Code Ends
