# problems-deletestring

Question:

You are given two strings a and k. Write a program to perfrom following task:
You can delete string k from string s any number of times. It is also given that the string k appears only once at a time in the dires+ct way. The task is to find if the string s can become empty by removing string k again and again. Print "YES" if the string s is empty after consequent deletion of string k, else print "NO".

Input Description:

The first line contains string s. The second line contains string k.

Output Description:

Print "YES" if the string s is empty after consequent deletion of string k, else print "NO".

Sample Input:

GUVGUVGUVIII\n
GUVI

Sample Output:

YES

Explanantion:

We can make the string guvguvii empty by deleting guvi 2 times, so the output is "YES"

Testcase 1:

Input:

GUGUVGGGUVGUVIIUVIVUVIIVI\n
GUVI

Ouput:

NO

Testcase 2:

Input:

GGUGUVGGUGUVIVIUVIIVIUVI\n
GUVI

Output:

YES

Testcase 3:

GUGGUGUVGGUGGUGUVGGUGUVIVIUVIIVIUVIVIUVIIVIUVIVI\n
GUVI

Output:

YES

Testcase 4:

Input:

GUVGUGUVGGUGUVGUGUVGGUGUVIVIUVIIVIUVIVIUVIIVIUVI\n
GUVI

Output:

NO

Testcase 5:

GUVGUGGUGUVGGUGGUGUVGGUGUGGUGUVGGUGGUGUVGGUGUVIVIUVIIVIUVIVIUVIIVIUVIVIVIUVIIVIUVIVIUVIIVIUVIVII\n
GUVI

Output:

YES

