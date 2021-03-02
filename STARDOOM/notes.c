//                      array of pointers and how to use

// const int MAX = 3;
 
// int main () {

//    int  var[] = {10, 100, 200};
//    int i, *ptr[MAX];
 
//    for ( i = 0; i < MAX; i++) {
//       ptr[i] = &var[i]; /* assign the address of integer. */
//    }
   
//    for ( i = 0; i < MAX; i++) {
//       printf("Value of var[%d] = %d\n", i, *ptr[i] );
//    }
   
//    return 0;
// }




//                      simple program to open, read, and close files
// int main()
// {
//      /* Pointer to the file */
//      FILE *fp1;
//      /* Character variable to read the content of file */
//      char c;

//      /* Opening a file in r mode*/
//      fp1= fopen ("C:\\myfiles\\newfile.txt", "r");

//      /* Infinite loop –I have used break to come out of the loop*/
//      while(1)
//      {
//         c = fgetc(fp1);
//         if(c==EOF)
//             break;
//         else
//             printf("%c", c);
//      }
//      fclose(fp1);
//      return 0;
// }


// types out one character at a time
void type_text(char *s, unsigned ms_delay)
{
   unsigned usecs = ms_delay * 1000; /* 1000 microseconds per ms */

   for (; *s; s++) {
      putchar(*s);
      fflush(stdout); /* alternatively, do once: setbuf(stdout, NULL); */
      usleep(usecs);
   }
}

int main(void)
{
   type_text("hello world\n", 100);
   return 0;
}