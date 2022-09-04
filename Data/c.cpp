
// C++ implementation of the approach
#include <cmath>
#include <iostream>
using namespace std;
 
#define ull unsigned long long int

int decimalToBinary(int N)
{
 
    // To store the binary number
    ull B_Number = 0;
    int cnt = 0;
    while (N != 0) {
        int rem = N % 2;
        ull c = pow(10, cnt);
        B_Number += rem * c;
        N /= 2;
 
        // Count used to store exponent value
        cnt++;
    }
 
    return B_Number;
}

int main(){
    int a,b ;
    cin >> a>> b;
    a = decimalToBinary(a);
    b = decimalToBinary(b);
    int diff =0 ;
    while(a>0 || b>0){
        if((a&1)!=(b&1))
        diff++ ;
        a>>=1;
        b>>=1;
        if(diff==1)
        cout << 1;
        else
        cout << 0 ;
    }
    
}