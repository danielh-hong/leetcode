// ================================================================
// C Pointer Exercises
// Comprehensive list of exercises to practice pointers in C.
// All exercises are included in this single file.
// Importing necessary headers only once.
// ================================================================

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ---------------------------------------------------------------
// Exercise 1: Basic Pointer Declaration and Dereferencing
//
// Declare an integer and a pointer to it. Assign the address
// to the pointer and print both value and address.
//
// Expected Output:
// Value of a: 10
// Address of a: 0x7ffee3bff58c
// Pointer p points to: 0x7ffee3bff58c
// Value via pointer p: 10
// ---------------------------------------------------------------
void exercise1() {
    int a = 10;
    int *p = &a;

    printf("Value of a: %d\n", a);
    printf("Address of a: %p\n", (void*)&a);
    printf("Pointer p points to: %p\n", (void*)p);
    printf("Value via pointer p: %d\n", *p);
}

// ---------------------------------------------------------------
// Exercise 2: Guess the Output: Pointer Increment
//
// Predict the output after modifying the value via pointer.
//
// Expected Output:
// a = 5
// *p = 5
// After modification:
// a = 10
// *p = 10
// ---------------------------------------------------------------
void exercise2() {
    int a = 5;
    int *p = &a;

    printf("a = %d\n", a);
    printf("*p = %d\n", *p);

    *p = 10;

    printf("After modification:\n");
    printf("a = %d\n", a);
    printf("*p = %d\n", *p);
}

// ---------------------------------------------------------------
// Exercise 3: Pointer Arithmetic: Incrementing a Pointer
//
// Use pointer arithmetic to traverse an integer array.
//
// Expected Output:
// Element 0: 1
// Element 1: 2
// Element 2: 3
// Element 3: 4
// Element 4: 5
// ---------------------------------------------------------------
void exercise3() {
    int arr[] = {1, 2, 3, 4, 5};
    int *p = arr; // Equivalent to &arr[0]
    int i;

    for(i = 0; i < 5; i++) {
        printf("Element %d: %d\n", i, *(p + i));
    }
}

// ---------------------------------------------------------------
// Exercise 4: Swapping Two Variables Using Pointers
//
// Write a function that swaps two integers using pointers.
//
// Expected Output:
// Before swap: a = 100, b = 200
// After swap: a = 200, b = 100
// ---------------------------------------------------------------
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

void exercise4() {
    int a = 100, b = 200;

    printf("Before swap: a = %d, b = %d\n", a, b);
    swap(&a, &b);
    printf("After swap: a = %d, b = %d\n", a, b);
}

// ---------------------------------------------------------------
// Exercise 5: Pointer to Pointer
//
// Demonstrate the use of a double pointer.
//
// Expected Output:
// Value of a: 50
// Value via *p: 50
// Value via **pp: 50
// ---------------------------------------------------------------
void exercise5() {
    int a = 50;
    int *p = &a;
    int **pp = &p;

    printf("Value of a: %d\n", a);
    printf("Value via *p: %d\n", *p);
    printf("Value via **pp: %d\n", **pp);
}

// ---------------------------------------------------------------
// Exercise 6: Pointer and Array Names
//
// Show that the array name is a pointer to its first element.
//
// Expected Output:
// First element: 10
// Second element: 20
// Third element: 30
// ---------------------------------------------------------------
void exercise6() {
    int arr[] = {10, 20, 30};
    int *p = arr; // or int *p = &arr[0];

    printf("First element: %d\n", *p);
    printf("Second element: %d\n", *(p + 1));
    printf("Third element: %d\n", *(p + 2));
}

// ---------------------------------------------------------------
// Exercise 7: Pointer Comparison
//
// Compare two pointers pointing to different variables.
//
// Expected Output:
// Pointers are not equal.
// ---------------------------------------------------------------
void exercise7() {
    int a = 5, b = 10;
    int *p1 = &a;
    int *p2 = &b;

    if(p1 == p2)
        printf("Pointers are equal.\n");
    else
        printf("Pointers are not equal.\n");
}

// ---------------------------------------------------------------
// Exercise 8: Null Pointer
//
// Initialize a pointer to NULL and check before dereferencing.
//
// Expected Output:
// Pointer is NULL.
// ---------------------------------------------------------------
void exercise8() {
    int *p = NULL;

    if(p != NULL)
        printf("Pointer points to: %d\n", *p);
    else
        printf("Pointer is NULL.\n");
}

// ---------------------------------------------------------------
// Exercise 9: Pointer to Array of Characters (Strings)
//
// Use pointers to traverse a string.
//
// Expected Output:
// H e l l o 
// ---------------------------------------------------------------
void exercise9() {
    char str[] = "Hello";
    char *p = str;
    int i;

    for(i = 0; *(p + i) != '\0'; i++) {
        printf("%c ", *(p + i));
    }
    printf("\n");
}

// ---------------------------------------------------------------
// Exercise 10: Function Returning Pointer
//
// Write a function that returns a pointer to an integer.
//
// Expected Output:
// Value of a: 25
// Value via ptr: 25
// ---------------------------------------------------------------
int* getPointer(int *p) {
    return p;
}

void exercise10() {
    int a = 25;
    int *ptr = getPointer(&a);

    printf("Value of a: %d\n", a);
    printf("Value via ptr: %d\n", *ptr);
}

// ---------------------------------------------------------------
// Exercise 11: Pointer to Structure
//
// Access structure members using pointers.
//
// Expected Output:
// Name: Alice
// Age: 30
// ---------------------------------------------------------------
struct Person {
    char name[20];
    int age;
};

void exercise11() {
    struct Person p1 = {"Alice", 30};
    struct Person *ptr = &p1;

    printf("Name: %s\n", ptr->name);
    printf("Age: %d\n", ptr->age);
}

// ---------------------------------------------------------------
// Exercise 12: Array of Pointers
//
// Create an array of pointers to integers.
//
// Expected Output:
// Value 0: 1
// Value 1: 2
// Value 2: 3
// ---------------------------------------------------------------
void exercise12() {
    int a = 1, b = 2, c = 3;
    int *arr[3] = {&a, &b, &c};
    int i;

    for(i = 0; i < 3; i++) {
        printf("Value %d: %d\n", i, *arr[i]);
    }
}

// ---------------------------------------------------------------
// Exercise 13: Pointer to Function
//
// Use a pointer to call a function.
//
// Expected Output:
// Result: 12
// ---------------------------------------------------------------
int add(int x, int y) {
    return x + y;
}

void exercise13() {
    int (*func_ptr)(int, int) = add;
    int result = func_ptr(5, 7);

    printf("Result: %d\n", result);
}

// ---------------------------------------------------------------
// Exercise 14: Dynamic Memory Allocation with Pointers
//
// Allocate memory for an array using pointers.
//
// Expected Output (if n=5):
// Enter number of elements: 5
// Array elements: 1 2 3 4 5 
// ---------------------------------------------------------------
void exercise14() {
    int *arr;
    int n, i;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    arr = (int*)malloc(n * sizeof(int));

    if(arr == NULL) {
        printf("Memory allocation failed.\n");
        return;
    }

    for(i = 0; i < n; i++) {
        arr[i] = i + 1;
    }

    printf("Array elements: ");
    for(i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    free(arr);
}

// ---------------------------------------------------------------
// Exercise 15: Pointer to Multi-dimensional Array
//
// Access elements in a 2D array using pointers.
//
// Expected Output:
// 1 2 3 
// 4 5 6 
// ---------------------------------------------------------------
void exercise15() {
    int matrix[2][3] = {{1,2,3}, {4,5,6}};
    int (*p)[3] = matrix;
    int i, j;

    for(i = 0; i < 2; i++) {
        for(j = 0; j < 3; j++) {
            printf("%d ", *(*(p + i) + j));
        }
        printf("\n");
    }
}

// ---------------------------------------------------------------
// Exercise 16: Pointer Type Casting
//
// Cast a void pointer to an integer pointer.
//
// Expected Output:
// Value via ip: 100
// ---------------------------------------------------------------
void exercise16() {
    int a = 100;
    void *vp = &a;
    int *ip = (int*)vp;

    printf("Value via ip: %d\n", *ip);
}

// ---------------------------------------------------------------
// Exercise 17: Pointers and Strings Manipulation
//
// Reverse a string using pointers.
//
// Expected Output:
// Reversed string: olleH
// ---------------------------------------------------------------
void reverseString(char *start, char *end) {
    char temp;
    while(start < end) {
        temp = *start;
        *start = *end;
        *end = temp;
        start++;
        end--;
    }
}

void exercise17() {
    char str[] = "Hello";
    int len = strlen(str);
    reverseString(str, str + len - 1);
    printf("Reversed string: %s\n", str);
}

// ---------------------------------------------------------------
// Exercise 18: Pointer to Const
//
// Use a pointer to a constant integer.
//
// Expected Output:
// Value of a: 50
// ---------------------------------------------------------------
void exercise18() {
    const int a = 50;
    const int *p = &a;

    printf("Value of a: %d\n", *p);
    // *p = 60; // Error: cannot modify through pointer
}

// ---------------------------------------------------------------
// Exercise 19: Const Pointer
//
// Use a constant pointer to an integer.
//
// Expected Output:
// Value via p: 20
// New value via p: 25
// ---------------------------------------------------------------
void exercise19() {
    int a = 20, b = 30;
    int * const p = &a;

    printf("Value via p: %d\n", *p);
    *p = 25; // Allowed
    printf("New value via p: %d\n", *p);
    // p = &b; // Error: cannot change address
}

// ---------------------------------------------------------------
// Exercise 20: Double Pointers and Dynamic Memory
//
// Allocate a 2D array using double pointers.
//
// Expected Output:
// 2D Array:
// 0 1 2 
// 1 2 3 
// ---------------------------------------------------------------
void exercise20() {
    int **arr;
    int rows = 2, cols = 3;
    int i, j;

    arr = (int**)malloc(rows * sizeof(int*));
    for(i = 0; i < rows; i++) {
        arr[i] = (int*)malloc(cols * sizeof(int));
    }

    for(i = 0; i < rows; i++) {
        for(j = 0; j < cols; j++) {
            arr[i][j] = i + j;
        }
    }

    printf("2D Array:\n");
    for(i = 0; i < rows; i++) {
        for(j = 0; j < cols; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }

    for(i = 0; i < rows; i++) {
        free(arr[i]);
    }
    free(arr);
}

// ---------------------------------------------------------------
// Exercise 21: Pointer to Pointer and Function Modification
//
// Modify a pointer in a function using a pointer to pointer.
//
// Expected Output:
// Value: 99
// ---------------------------------------------------------------
void allocate(int **p) {
    *p = (int*)malloc(sizeof(int));
    if(*p != NULL)
        **p = 99;
}

void exercise21() {
    int *ptr = NULL;

    allocate(&ptr);

    if(ptr != NULL)
        printf("Value: %d\n", *ptr);
    else
        printf("Memory not allocated.\n");

    free(ptr);
}

// ---------------------------------------------------------------
// Exercise 22: Function Pointers for Callbacks
//
// Use function pointers to implement a callback.
//
// Expected Output:
// Hello!
// Goodbye!
// ---------------------------------------------------------------
void greet() {
    printf("Hello!\n");
}

void farewell() {
    printf("Goodbye!\n");
}

void execute(void (*func)()) {
    func();
}

void exercise22() {
    execute(greet);
    execute(farewell);
}

// ---------------------------------------------------------------
// Exercise 23: Pointer to Function Returning Pointer
//
// Function returns a pointer to a static integer.
//
// Expected Output:
// Value: 500
// ---------------------------------------------------------------
int* getStatic() {
    static int a = 500;
    return &a;
}

void exercise23() {
    int *p = getStatic();
    printf("Value: %d\n", *p);
}

// ---------------------------------------------------------------
// Exercise 24: Pointer Casting and Arithmetic
//
// Perform pointer arithmetic with different types.
//
// Expected Output:
// Double value: 3.14
// ---------------------------------------------------------------
void exercise24() {
    char c = 'A';
    int a = 100;
    double d = 3.14;

    void *vp = &c;
    vp = &a;
    vp = &d;

    // Cast back to correct type before dereferencing
    printf("Double value: %.2f\n", *(double*)vp);
}

// ---------------------------------------------------------------
// Exercise 25: Implementing Linked List with Pointers
//
// Create a simple linked list and traverse it.
//
// Expected Output:
// 1 2 3 
// ---------------------------------------------------------------
struct Node {
    int data;
    struct Node *next;
};

void exercise25() {
    struct Node *head, *second, *third;

    head = (struct Node*)malloc(sizeof(struct Node));
    second = (struct Node*)malloc(sizeof(struct Node));
    third = (struct Node*)malloc(sizeof(struct Node));

    head->data = 1;
    head->next = second;

    second->data = 2;
    second->next = third;

    third->data = 3;
    third->next = NULL;

    struct Node *ptr = head;
    while(ptr != NULL) {
        printf("%d ", ptr->data);
        ptr = ptr->next;
    }
    printf("\n");

    // Free memory
    free(third);
    free(second);
    free(head);
}

// ---------------------------------------------------------------
// Exercise 26: Pointers and Bit Manipulation
//
// Toggle the least significant bit using pointers.
//
// Expected Output:
// After toggling LSB: 4
// ---------------------------------------------------------------
void exercise26() {
    int a = 5; // Binary: 0101
    int *p = &a;

    *p ^= 1; // Toggle LSB

    printf("After toggling LSB: %d\n", a);
}

// ---------------------------------------------------------------
// Exercise 27: Pointer Alignment and Padding
//
// Demonstrate structure padding using pointers.
//
// Expected Output:
// Size of struct Packed: 8
// ---------------------------------------------------------------
struct Packed {
    char a;
    int b;
};

void exercise27() {
    struct Packed p;
    printf("Size of struct Packed: %lu\n", sizeof(p));
}

// ---------------------------------------------------------------
// Exercise 28: Pointers and Memory Addresses
//
// Print memory addresses of variables and pointers.
//
// Expected Output:
// Address of a: 0x7ffee3bff58c
// Address of p: 0x7ffee3bff590
// Address of pp: 0x7ffee3bff598
// ---------------------------------------------------------------
void exercise28() {
    int a = 10;
    int *p = &a;
    int **pp = &p;

    printf("Address of a: %p\n", (void*)&a);
    printf("Address of p: %p\n", (void*)&p);
    printf("Address of pp: %p\n", (void*)&pp);
}

// ---------------------------------------------------------------
// Exercise 29: Pointer Dereferencing in Loops
//
// Sum elements of an array using pointer dereferencing.
//
// Expected Output:
// Sum: 30
// ---------------------------------------------------------------
void exercise29() {
    int arr[] = {2, 4, 6, 8, 10};
    int *p = arr;
    int sum = 0, i;

    for(i = 0; i < 5; i++) {
        sum += *(p + i);
    }

    printf("Sum: %d\n", sum);
}

// ---------------------------------------------------------------
// Exercise 30: Const Correctness with Pointers
//
// Use pointers with const correctness.
//
// Expected Output:
// a: 20
// ---------------------------------------------------------------
void exercise30() {
    int a = 10;
    const int *p1 = &a; // Pointer to const int
    int * const p2 = &a; // Const pointer to int

    // *p1 = 20; // Error
    *p2 = 20; // Allowed

    printf("a: %d\n", a);
}

// ---------------------------------------------------------------
// Exercise 31: Pointer to Array
//
// Access array elements using pointer to array.
//
// Expected Output:
// Element 0: 7
// Element 1: 14
// Element 2: 21
// ---------------------------------------------------------------
void exercise31() {
    int arr[3] = {7, 14, 21};
    int (*p)[3] = &arr;
    int i;

    for(i = 0; i < 3; i++) {
        printf("Element %d: %d\n", i, (*p)[i]);
    }
}

// ---------------------------------------------------------------
// Exercise 32: Pointer and Function Parameters
//
// Pass an array to a function using pointers.
//
// Expected Output:
// 3 6 9 12 
// ---------------------------------------------------------------
void printArray(int *p, int size) {
    int i;
    for(i = 0; i < size; i++) {
        printf("%d ", *(p + i));
    }
    printf("\n");
}

void exercise32() {
    int arr[] = {3, 6, 9, 12};
    printArray(arr, 4);
}

// ---------------------------------------------------------------
// Exercise 33: Pointer to Void
//
// Use void pointers to handle different data types.
//
// Expected Output:
// Integer value: 100
// Double value: 12.34
// ---------------------------------------------------------------
void exercise33() {
    int a = 100;
    double d = 12.34;
    void *vp;

    vp = &a;
    printf("Integer value: %d\n", *(int*)vp);

    vp = &d;
    printf("Double value: %.2f\n", *(double*)vp);
}

// ---------------------------------------------------------------
// Exercise 34: Pointer to Function with Parameters
//
// Use a pointer to a function that takes parameters.
//
// Expected Output:
// Result: 20
// ---------------------------------------------------------------
int multiply(int x, int y) {
    return x * y;
}

void exercise34() {
    int (*func_ptr)(int, int) = multiply;
    int result = func_ptr(4, 5);

    printf("Result: %d\n", result);
}

// ---------------------------------------------------------------
// Exercise 35: Dynamic Memory Allocation for Struct
//
// Allocate memory for a struct using pointers.
//
// Expected Output:
// Point: (10, 20)
// ---------------------------------------------------------------
struct Point {
    int x;
    int y;
};

void exercise35() {
    struct Point *p = (struct Point*)malloc(sizeof(struct Point));
    if(p == NULL) {
        printf("Memory allocation failed.\n");
        return;
    }

    p->x = 10;
    p->y = 20;

    printf("Point: (%d, %d)\n", p->x, p->y);

    free(p);
}

// ---------------------------------------------------------------
// Exercise 36: Pointer to Function Returning Function Pointer
//
// Function returns a pointer to another function.
//
// Expected Output:
// 5 + 3 = 8
// 5 - 3 = 2
// ---------------------------------------------------------------
int subtract(int a, int b) {
    return a - b;
}

int (*getOperation(char op))(int, int) {
    if(op == '+') return add;
    else return subtract;
}

void exercise36() {
    int (*op_func)(int, int);
    op_func = getOperation('+');
    printf("5 + 3 = %d\n", op_func(5, 3));

    op_func = getOperation('-');
    printf("5 - 3 = %d\n", op_func(5, 3));
}

// ---------------------------------------------------------------
// Exercise 37: Pointer to Constant Pointer
//
// Use a pointer to a constant pointer.
//
// Expected Output:
// Value: 10
// ---------------------------------------------------------------
void exercise37() {
    int a = 10;
    int b = 20;
    int * const p = &a;
    int * const *pp = &p;

    // *pp = &b; // Error: cannot change what pp points to
    // **pp = 30; // Allowed if p points to non-const

    printf("Value: %d\n", **pp);
}

// ---------------------------------------------------------------
// Exercise 38: Pointer to Array of Pointers
//
// Create and use an array of string literals.
//
// Expected Output:
// Apple
// Banana
// Cherry
// ---------------------------------------------------------------
void exercise38() {
    const char *fruits[] = {"Apple", "Banana", "Cherry"};
    int i;

    for(i = 0; i < 3; i++) {
        printf("%s\n", fruits[i]);
    }
}

// ---------------------------------------------------------------
// Exercise 39: Pointer and Recursion
//
// Use pointers in a recursive function to calculate factorial.
//
// Expected Output:
// Factorial of 5 is 120
// ---------------------------------------------------------------
int factorial(int n, int *result) {
    if(n == 0) {
        *result = 1;
        return 1;
    } else {
        int temp;
        factorial(n - 1, &temp);
        *result = n * temp;
        return *result;
    }
}

void exercise39() {
    int num = 5;
    int fact;

    factorial(num, &fact);
    printf("Factorial of %d is %d\n", num, fact);
}

// ---------------------------------------------------------------
// Exercise 40: Pointers and Enums
//
// Use pointers with enum types.
//
// Expected Output:
// Color value: 1
// New color value: 2
// ---------------------------------------------------------------
enum Color { RED, GREEN, BLUE };

void exercise40() {
    enum Color color = GREEN;
    enum Color *p = &color;

    printf("Color value: %d\n", *p);

    *p = BLUE;
    printf("New color value: %d\n", color);
}

// ---------------------------------------------------------------
// Main Function
//
// Uncomment the exercise you want to run.
//
// Example:
// exercise1();
// exercise2();
// ...
// exercise40();
// ---------------------------------------------------------------
int main() {
    // Uncomment the exercise you want to run by removing the '//' below.

    // exercise1();
    // exercise2();
    // exercise3();
    // exercise4();
    // exercise5();
    // exercise6();
    // exercise7();
    // exercise8();
    // exercise9();
    // exercise10();
    // exercise11();
    // exercise12();
    // exercise13();
    // exercise14();
    // exercise15();
    // exercise16();
    // exercise17();
    // exercise18();
    // exercise19();
    // exercise20();
    // exercise21();
    // exercise22();
    // exercise23();
    // exercise24();
    // exercise25();
    // exercise26();
    // exercise27();
    // exercise28();
    // exercise29();
    // exercise30();
    // exercise31();
    // exercise32();
    // exercise33();
    // exercise34();
    // exercise35();
    // exercise36();
    // exercise37();
    // exercise38();
    // exercise39();
    // exercise40();

    return 0;
}
