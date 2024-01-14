#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char sign_calcu(int month_num,int date_num){

     if ((month_num == 1 && date_num > 19) || (month_num == 2 && date_num < 19)) {
         return 'A';
     } else if ((month_num == 2 && date_num > 18) || (month_num == 3 && date_num < 21)) {
         return 'P';
     } else if ((month_num == 3 && date_num > 20) || (month_num == 4 && date_num < 20)) {
         return 'A';
     } else if ((month_num == 4 && date_num > 19) || (month_num == 5 && date_num < 21)) {
         return 'T';
     } else if ((month_num == 5 && date_num > 20) || (month_num == 6 && date_num < 22)) {
         return 'G';
     } else if ((month_num == 6 && date_num > 21) || (month_num == 7 && date_num < 23)) {
         return 'C';
     } else if ((month_num == 7 && date_num > 22) || (month_num == 8 && date_num < 23)) {
         return 'L';
     } else if ((month_num == 8 && date_num > 22) || (month_num == 9 && date_num < 23)) {
         return 'V';
     } else if ((month_num == 9 && date_num > 22) || (month_num == 10 && date_num < 23)) {
         return 'L';
     } else if ((month_num == 10 && date_num > 22) || (month_num == 11 && date_num < 23)) {
         return 'S';
     } else if ((month_num == 11 && date_num > 22) || (month_num == 12 && date_num < 22)) {
         return 'S';
     } else if ((month_num == 12 && date_num > 21) || (month_num == 1 && date_num < 20)) {
         return 'C';
     }
     return ' ';
}

void famous_actor(char sign, char *actor) {


    switch (sign) {
	case 'A':
		strcpy(actor, "Jennifer Aniston");
		break;
	case 'P':
		strcpy(actor, "Javier Bardem");
		break;
	case 'T':
		strcpy(actor, "Dwayne 'The Rock' Johnson");
		break;
	case 'G':
		strcpy(actor, "Johnny Depp");
		break;
	case 'C':
		strcpy(actor, "Tom Hanks");
		break;
	case 'L':
		strcpy(actor, "Hugh Jackman");
		break;
	case 'V':
		strcpy(actor, "Blake Lively");
		break;
	case 'S':
		strcpy(actor, "Ryan Gosling");
		break;
	default:
		strcpy(actor, "Unknown");
		break;
    }

}

int main(void) {

	printf("Hi,this is a Zodiac sign calculator.");

	printf("What month were you born in? Please type a number:\n");
	int month_num;
	scanf("%d",&month_num);


	printf("What date were you born on? Please type a number:\n");
    int date_num;
    scanf("%d", &date_num);

    char sign = sign_calcu(month_num,date_num);
    char actor[50]; famous_actor(sign, actor);

    if (sign == ' ') {
        printf("Invalid input.\n");

      }
    else {
    	 printf("Your sign is ");
    	   switch (sign) {
    	    case 'A': printf("Aquarius ♒︎\n"); break;
			case 'P': printf("Pisces ♓︎\n"); break;
			case 'T': printf("Taurus ♉︎\n"); break;
			case 'G': printf("Gemini ♊︎\n"); break;
			case 'C': printf("Cancer ♋︎\n"); break;
			case 'L': printf("Libra ♎︎\n"); break;
			case 'V': printf("Virgo ♍︎\n"); break;
			case 'S': printf("Scorpio ♏︎\n"); break;
    	   }

    	   printf("\nFamous actor born under the same sign: %s\n", actor);
   }
    while(1){};
}
