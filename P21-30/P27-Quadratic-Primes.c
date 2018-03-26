// Compile with gcc -O3 -lm -Wall -o out P27-Quadratic-Primes.c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NUMS 5000000
#define Q(n,a,b) (n)*(n) + (a)*(n) + (b)
typedef unsigned int U;

U sieve[NUMS] = {1, 1, 0 }; // Initial to 0s

void pop_sieve() {
    int s = (int)(sqrt(NUMS) + 1);
    for (int n = 2; n < s; n++) {
        if (sieve[n] == 0) 
            for (int i = n*n; i < NUMS; i += n) 
                sieve[i] = 1;
    }
}

U count_primes() {
    U c = 0;
    for (int i = 0; i < NUMS; i++)
        if (sieve[i] == 0) c++;
    return c;
}

void pop_primes(U *ptr) {
    int j = 0;
    for (U i = 0; i < NUMS; i++) {
        if (sieve[i] == 0) {
            ptr[j] = i;
            j++;
        }
    }
}

int is_prime(int n, U *primes) {
    if (n < 2) return 0;
    int i = 0;
    while (n >= primes[i]) {
        if (n == primes[i]) return 1;
        i++;
    }
    return 0;
}

U quad_prime_seq(int a, int b, U *primes) {
    U c = 0;
    for (U x = 0; x < 200; x++) {
        if (!is_prime(Q(x,a,b), primes)) break;
        c++;
    }
    return c;
}

U primes_less_than(U n, U *primes) {
    U i = 0;
    while (primes[i] < n) i++;
    return i;
}

int longest_quad_prime_seq(U *primes) {
   /*
     For all a, b between -1000 to 1000, find longest quadratic prime sequence s.t x*x + a*x + b must be prime for x > 0
     For x = 0 to be prime, b must be a prime. For x = 1 to be a prime, a > 1 - b
    */
    U pp = primes_less_than(1000, primes);
    U lc = 0;
    int ma = 0;
    int mb = 0;
    for (U i = 0; i <= pp; i++) {
        int b = primes[i];
        for (int a = -b; a < b; a++) {
            U qs = quad_prime_seq(a, b, primes);
            if (qs > lc) {
                lc = qs; ma = a; mb = b;
            }
        }
    }
    return ma * mb;
}

int main() {
    printf("Populating sieve\n");
    pop_sieve();
    U c = count_primes();
    U *ptr = (U*) malloc(c * sizeof(U));
    printf("Counting primes %u\n", c);
    pop_primes(ptr);
    printf("Seq Euler : %u\n", quad_prime_seq(1, 41, ptr));
    printf("%d\n", longest_quad_prime_seq(ptr));
}
