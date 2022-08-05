

#include <stdio.h>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

typedef long long ll;
typedef vector<int> vt;
typedef unordered_map<int, int> umap;
typedef unsigned ud;

int n, b, arr[100000];


int solve() {
    int ans = 0;
    cin >> n >> b;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    sort(arr, arr + n);
    
    for (int j = 0; j < n; j++) {
        if (b >= arr[j]) {
            b -= arr[j];
            ans++;
        }
        
        else {
            break;
        }
    }
    
    return ans;
    
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        cout << "Case #" << i + 1 << ": " << solve() << endl;
    }
  
    
    return 0;
}


