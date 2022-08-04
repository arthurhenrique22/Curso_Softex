#include <stdio.h>
#include <stdlib.h>

int main(void) {
  float *vetor; 
  int i, num;
  
  printf("Informe o numero de componentes do vetor\n");
  scanf("%d", &num);

  vetor = (float *)malloc(num * sizeof(float));

  for (i = 0; i < num; i++) {
    printf("\nDigite o valor para a posicao %d do vetor: ", i + 1);
    scanf("%f", &vetor[i]);
  }

  printf("\nValores do vetor dinamico\n\n");

  for (i = 0; i < num; i++) {
    printf("%.2f\n", vetor[i]);
  }

  free(vetor);

  return 0;
}
