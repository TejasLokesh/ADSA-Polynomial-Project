# ADSA-Polynomial-Project
Write a program that adds and subtracts polynomials. Each polynomial should be represented as a  list with linked list implementation. The first node in the list represents the first term in the  polynomial, the second node represents the second term, and so forth. Each node contains three  fields. The first field is the term’s coefficient. The second field is the term’s power, and the third  field is a pointer to the next term. For example, consider the polynomials shown in Figure 5-34.  The first term in the first polynomial has a coefficient of 5 and an exponent of 4, which is then  interpreted as 5x4. 

The rules for the addition of polynomials are as follows: 
a. If the powers are equal, the coefficients are algebraically added. 
b. If the powers are unequal, the term with the higher power is inserted in the new polynomial. c. If the exponent is 0, it represents x0, which is 1. The value of the term is therefore the value of  the coefficient. 
d. If the result of adding the coefficients results in 0, the term is dropped (0 times anything is 0). 

A polynomial is represented by a series of lines, each of which has two integers. The first integer  represents the coefficient; the second integer represents the exponent. Thus, the first polynomial  in Figure above is 

5 4 
6 3 
7 0 
To add two polynomials, the program reads the coefficients and exponents for each polynomial  and places them into a linked list. The input can be read from separate files or entered from the  keyboard with appropriate user prompts. After the polynomials have been stored, they are added  and the results are placed in a third linked list. The polynomials are added using an operational  merge process.  
An operational merge combines the two lists while performing one or more operations—in our  case, addition. To add we take one term from each of the polynomials and compare the exponents. If the two exponents are equal, the coefficients are added to create a new coefficient. If the new coefficient is 0, the term is dropped; if it is not 0, it is appended to the linked list for the resulting 
polynomial. If one of the exponents is larger than the other, the corresponding term is immediately  placed into the new linked list, and the term with the smaller exponent is held to be compared with  the next term from the other list. If one list ends before the other, the rest of the longer list is simply  appended to the list for the new polynomial.
Print the two input polynomials and their sum by traversing the linked lists and displaying them  as sets of numbers. Be sure to label each polynomial. 
