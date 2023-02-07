#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    FILE *fptr;
    fptr = fopen("v.dat", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        exit(1);
    }

    for (int i = 0; i < 100000; i++) {
        double U = (double)rand() / RAND_MAX;
        double V = -2 * log(1 - U);
        fprintf(fptr, "%lf\n", V);
    }

    fclose(fptr);
    return 0;
}
