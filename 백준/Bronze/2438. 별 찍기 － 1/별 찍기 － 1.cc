#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int a;
	int i = 0;
	int j = 0;
	scanf("%d", &a);
	while (i < a) {
		j = 0;
		while (j<= i) {
			printf("*");
			j++;
		}
		i++;
		printf("\n");
	}
}