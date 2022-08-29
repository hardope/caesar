#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

int main(int argc, char *argv[])
{
    if (argc == 2) //checks if argument count is correct
    {
        int a = atoi(argv[1]); //changes string to integer
    
        if (a > 0)
        {
            int i = 0;
            int n = 0;
            printf("Plaintext: ");
            char text[100];
            fgets(text, sizeof(text), stdin); //prompts user for plaintext
            printf("ciphertext: "); //prompt user for ciphertext
            for (i = 0, n = strlen(text); i < n; i++) //iterates over all character in plaintext
            {
                if (text[i] >= 65 && text[i] <= 90) //checks if character is uppercase
                {
                    int c = text[i] + a;
                    if (c < 90)
                    {
                        printf("%c", c);
                    }
                    else
                    {
                        printf("%c", c - 26);
                    }
                }
                else if (text[i] >= 97 && text[i] <= 122) //checks if character is lowercase
                {
                    int c = text[i] + a;
                    if (c < 122)
                    {
                        printf("%c", c);
                    }
                    else if (c >= 122 && c < 148)
                    {
                        printf("%c", c - 26);
                    }
                    else if (c >= 148 && c < 174)
                    {
                        printf("%c", c - 52);
                    }
                    else if (c >= 174 && c < 200)
                    {
                        printf("%c", c - 78);
                    }
                }
                else //checks if character is a space, period etc.
                {
                    printf("%c", text[i]);
                }
            }
            printf("\n");
            return 0;
        }
        else
        {
            printf("Usage: ./caesar key\n"); //prints wrong usage
            return 1;
        }
    }
    else if (argc > 2)
    {
        printf("Usage: ./caesar key\n");  //prints wrong usage
        return 1;
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}