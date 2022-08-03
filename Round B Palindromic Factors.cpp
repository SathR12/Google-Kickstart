

#include <stdio.h>
#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>

typedef long long ll;

using namespace std;

bool isPalindrome(string num) {
    string palin = num;
    reverse(palin.begin(), palin.end());
    
    //cout << palin << " " << num << endl;
    return palin == num;
    
}

int solve(ll num) {

    int count = 1;
    
    for (int i = 2; i <= num; i++) {
        
        if (num % i == 0) {
           
            if (i < 10) {
                count++;
                continue;
            }
        
            else if (isPalindrome(to_string(i))) {
                count++;
                continue;
            }
        }
    }
    
    return count;
}




int main() {
    ios::sync_with_stdio(0);
    cin.tie();
    
    int t; cin >> t;
    for (int i = 0; i < t; ++i) {
        ll a; cin >> a;
        cout << "Case #" << i + 1 << ": " << solve(a) << endl;
    }
    
    
    
    return 0;
}



