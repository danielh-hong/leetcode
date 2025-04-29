#include <stdlib.h>
#include <string.h>

void set_even_to_zero(int *block, int size) {
  int i = 0;
  while (i < size) {
    if (i % 2 == 0) {
      block[i] = 0;
      i++;
    }
  }
}

void set_even_to_zero_2(int *block, int size) {
  for (int i = 0; i < size; i++) {
    if (i % 2 == 0) {
      block[i] = 0;
    }
  }
}

int betweenX(char *s) {
  int sz = strlen(s);
  int l = 0;
  int r = sz - 1;
  while (l < r && (s[l] != 'X' || s[r] != 'X')) {
    if (s[l] != 'X') {
      l++;
    }

    if (s[r] != 'X') {
      r--;
    }
  }

  if (s[l] == 'X' && s[r] == 'X') {
    return (l + sz - r - 1);
  }
  else {
    return sz;
  }
}

int betweenX(char *s) {
  int sz = strlen(s);
  int l = 0;
  int r = sz - 1;
  while (l < r) {
    if (s[l] != 'X') {
      l++;
    }

    if (s[r] != 'X') {
      r--;
    }

    if (s[l] == 'X' && s[r] == 'X') {
      return (l + sz - r - 1);
    }
  }

  return sz;
}

/*
1 2
1 2 3 4
1 X 3 X

1 2 3 X 5 7 8 9 X

1 X 2 3 4 5 x 7 8
*/
