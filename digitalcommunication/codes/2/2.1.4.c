#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <float.h>

int main()
{
    FILE *file = fopen("uni.dat", "r");
    if (file == NULL)
    {
        printf("Error: unable to open file 'uni.dat'\n");
        return 1;
    }

    int n = 0; // number of samples
    double u, sum = 0, sum_squared = 0;

    while (fscanf(file, "%lf", &u) != EOF)
    {
        n++;
        sum += u;
        sum_squared += u * u;
    }

    fclose(file);

    double mean = sum / n;
    double variance = (sum_squared / n) - (mean * mean);

    printf("Mean of U: %f\n", mean);
    printf("Variance of U: %f\n", variance);

    return 0;
}
