#define CRT_NO_SECURE_WARNINGS
#include <stdio.h>
#include <stdlib.h>


int main(void) {
	int a;
	scanf("%d", &a);
	for (int j = 0; j < a; j++) {
		for (int i = 0; i <= j; i++) {
			printf("*");
		}
		printf("\n");
	}
	return 0;
}

