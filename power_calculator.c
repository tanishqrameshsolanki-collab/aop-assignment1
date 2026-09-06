#include <stdio.h>

long int power(int base, int exp) {
    long int result = 1;
    int i;
    for (i = 0; i < exp; i++) {
        result = result * base;
    }
    return result;
}

int main() {
    int base, exp;
    long int ans;
    
    printf("Enter Base : ");
    scanf("%d", &base);
    
    printf("Enter Exponent : ");
    scanf("%d", &exp);
    
    ans = power(base, exp);
    
    printf("\n%d^%d = %ld\n", base, exp, ans);
    
    return 0;
}
