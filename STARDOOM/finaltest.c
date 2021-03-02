#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <unistd.h>
#include <direct.h>
#include <time.h>


struct player
{
    char name[20];
    char race[10];
    char profession[20];
    #define HP 100
    #define ENERGY 100
};

// function prototype
void display_stats(struct player input);

void loading_animation() {
                // https://codereview.stackexchange.com/questions/139440/loading-animating-dots-in-c
    int load_counter = 1;

    const int trigger = 500; // ms
    const int numDots = 4;
    const char prompt[] = "Loading";

    while (load_counter < 3) {
        // Return and clear with spaces, then return and print prompt.
        printf("\r%*s\r%s", sizeof(prompt) - 1 + numDots, "", prompt);
        fflush(stdout);

        // Print numDots number of dots, one every trigger milliseconds.
        for (int i = 0; i < numDots; i++) {
            usleep(trigger * 1000);
            fputc('.', stdout);
            fflush(stdout);
        }
        load_counter++;
    }
}

void inventory() {
        // ARRAY OF STRINGS - inventory for player
    char inventory[5][50] = {"Phaser", "Crowbar", "Med Kit", "Small Torch", "50 credits"};
    printf("Inventory: ");
    for (int i = 0; i < 5; i++){
        printf("[%s] ", inventory[i]);
    }
    printf("\n");
}

int* engineer_stats() {
                // ARRAY OF POINTERS - stat modifiers. melee, range
    static int engineer[2];

    engineer[0] = 15  + (rand() % (6 + 1 - 0) + 0);         // phaser
    engineer[1] = 20 + (rand() % (9 + 1 - 0) + 0);          // crowbar

    return engineer;
}

int* gunslinger_stats() {
    static int gunslinger[2];

    gunslinger[0] = 20 + (rand() % (9 + 1 - 0) + 0);         // phaser
    gunslinger[1] = 15 + (rand() % (6 + 1 - 0) + 0);          // crowbar

    return gunslinger;
}


void engineer_combat() {

    int* eng_arr = engineer_stats();
    int attack_move;
    int alien_attk;
    int big_ass_alien;
    int player_hp;

    alien_attk = rand() % (16 + 1 - 0) + 0;

    big_ass_alien = 50;
    player_hp = 100;

    do {
    printf("\nHealth Points: %i\n What do you want to attack with?\n 1:Phaser\n 2:Crowbar\n\n", player_hp);
    scanf("%i", &attack_move);

    if(attack_move == 1) {
        
        big_ass_alien = big_ass_alien - eng_arr[0];
        printf("\nPEW PEW PEW! Damage >>> %i\n\n", eng_arr[0]);
        if(big_ass_alien < 0) {
            printf("You have killed the Big Ass Alien!\n\n");
            break;
        }
        printf("Big Ass Alien's HP >> %i\n\n", big_ass_alien);
        
        player_hp = player_hp - alien_attk;
        printf("The Big Ass Alien attacks! Damage >>> %i\n", alien_attk);
        if(player_hp < 0) {
            printf("You have been killed you lose\n\n");
            break;
        }
    }
    else if(attack_move == 2) {
        
        big_ass_alien = big_ass_alien - eng_arr[1];
        printf("\nYou swing your crowbar! Damage >>> %i\n\n", eng_arr[1]);
        if(big_ass_alien < 0) {
            printf("The alien implodes!\n\n");
            break;
        }
        printf("Big Ass Alien's HP >>>  %i\n\n", big_ass_alien);

        
        player_hp = player_hp - alien_attk;
        printf("The Big Ass Alien attacks! Damage >> %i!\n", alien_attk);
        if(player_hp < 0) {
            printf("You have been killed.\n");
            break;
        }
    }
    } while(player_hp > 0 && big_ass_alien > 0);
    
}


void gunslinger_combat() {

    int* gun_arr = gunslinger_stats();
    int attack_move;
    int alien_attk;
    int big_ass_alien;
    int player_hp;

    alien_attk = rand() % (16 + 1 - 0) + 0;

    big_ass_alien = 50;
    player_hp = 100;

    do {
    printf("\nHealth Points: %i\n What do you want to attack with?\n 1:Phaser\n 2:Crowbar\n\n", player_hp);
    scanf("%i", &attack_move);

    if(attack_move == 1) {
        
        big_ass_alien = big_ass_alien - gun_arr[0];
        printf("\nPEW PEW PEW! Damage >>> %i\n\n", gun_arr[0]);
        if(big_ass_alien < 0) {
            printf("You have killed the Big Ass Alien!\n\n");
            break;
        }
        printf("Big Ass Alien's HP >> %i\n\n", big_ass_alien);
        
        player_hp = player_hp - alien_attk;
        printf("The Big Ass Alien attacks! Damage >>> %i\n", alien_attk);
        if(player_hp < 0) {
            printf("You have been killed you lose\n\n");
            break;
        }
    }
    else if(attack_move == 2) {
        
        big_ass_alien = big_ass_alien - gun_arr[1];
        printf("\nYou swing your crowbar! Damage >>> %i\n\n", gun_arr[1]);
        if(big_ass_alien < 0) {
            printf("The alien implodes!\n\n");
            break;
        }
        printf("Big Ass Alien's HP >>  %i\n\n", big_ass_alien);

        
        player_hp = player_hp - alien_attk;
        printf("The Big Ass Alien attacks! Damage >>> %i!\n", alien_attk);
        if(player_hp < 0) {
            printf("You have been killed.\n");
            break;
        }
    }
    } while(player_hp > 0 && big_ass_alien > 0);
    
}

void location() {
    int loc_num;
    do {
    printf("Enter your location >>> ");
    scanf("%d", &loc_num);

    if (loc_num != 126 && loc_num != 436 && loc_num != 231){
            printf("Not a valid location.\n\n");
        }
    } while (loc_num != 126 && loc_num != 436 && loc_num != 231);

    printf(">>> Entering engine bay %d.\n", loc_num);
}

            // 2D ARRY - MAP
void create_map() {
    char* map[19][22] = 
        {{"O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", " ", " ", " ", "O", "O", "O", "O", "O", "O\n"},
        {"O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", " ", " ", " ", "O", "O", "O", "O", "O", "O\n"},
        {"O", "O", " ", " ", " ", " ", "1", "2", "6", " ", ">", ">", " ", " ", " ", " ", "O", "O", "O", "O", "O", "O\n"},
        {"O", "O", " ", " ", " ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O\n"},
        {"O", "O", " ", " ", " ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O\n"},
        {"O", "O", " ", " ", " ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O\n"},
        {"O", "O", " ", " ", " ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O\n"},
        {"O", "O", " ", " ", " ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O\n"},
        {"O", "O", " ", " ", " ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O\n"},
        {"O", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O\n"},
        {"O", "O", "O", "O", "O", "O", "O", "O", " ", " ", " ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O\n"},
        {"O", "O", "O", "O", "O", "O", "O", "O", " ", " ", " ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O\n"},
        {"O", "O", "O", "O", "O", "O", "O", "O", " ", " ", " ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O\n"},
        {"O", "O", "O", "O", "O", "O", "O", "O", " ", " ", " ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O\n"},
        {"<", "<", " ", "4", "3", "6", " ", " ", " ", " ", " ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O\n"},
        {"O", "O", "O", "O", "O", "O", "O", "O", " ", " ", " ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O\n"},
        {"O", "O", "O", "O", "O", "O", "O", "O", " ", " ", " ", " ", " ", " ", " ", "2", "3", "1", " ", ">", ">", " \n"},
        {"O", "O", "O", "O", "O", "O", "O", "O", " ", " ", " ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O\n"},
        {"O", "O", "O", "O", "O", "O", "O", "O", " ", " ", " ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O\n"}
        
        };

    FILE *fptr;
    fptr = fopen("blueprints.txt", "w");

    int i, j;
    for (i=0; i < 19; i++){
        for (j=0; j < 22; j++){
            fprintf(fptr, map[i][j]);
            printf(map[i][j]);
            
        }
    }
    printf("\n\n");
    fclose(fptr);
}

            // https://stackoverflow.com/questions/10923287/output-text-one-letter-at-a-time-in-c
void type_text(char *s, unsigned ms_delay){
   unsigned usecs = ms_delay * 1000; /* 1000 microseconds per ms */

   for (; *s; s++) {
      putchar(*s);
      fflush(stdout);
      usleep(usecs);
   }
}


int main() {
    printf("\n");

    printf("############# STARDOOM #############\n");

    loading_animation();

    printf("\n");
    printf("\n");
    type_text("Stardate: 2231\n", 35);
    type_text("Location: Xehrus 437\n", 35);
    type_text("Sector: Vega Constellation\n", 35);
    type_text("Right Ascension: 18h 36m 56.3s\n"
           "Declination: 38 degrees 47 minutes 01 second\n", 35);
    type_text("Security Level: Low\n", 35);
    type_text("Destination: Corvus Sector\n\n", 35);

    loading_animation();
    printf("\n\n");

    type_text("This is Captain S. Blue speaking, welcome aboard the USS Ozark. Right now you may be feeling "
    "a bit disoriented. Don't worry, it is normal after waking up from cryostasis. "
    "You have been awoken 73 years ahead of your schedule... The ship has been hit by an anomaly located "
    "near the edge of Nebulus Sector. The ship has been compromised by hostile terrestrial beings. "
    "Identification and origin is still unknown.\n\n", 15);

                // https://www.mkyong.com/c/how-to-handle-unknow-size-user-input-in-c/
    unsigned int len_max = 20;
    unsigned int current_size = 0;

    char *user_name = malloc(len_max);
    current_size = len_max;

    struct player input;

    printf("Who am I speaking to? ");
    scanf("%s", input.name);

    if(user_name != NULL){
	int c = EOF;        // marker to indicate end of input
	unsigned int i =0;
        //accept user input until hit enter
	while (( c = getchar() ) != '\n' && c != EOF){
		user_name[i++]=(char)c;

		if(i == current_size){
            current_size = i+len_max;
			user_name = realloc(user_name, current_size);
		}
	}

	user_name[i] = '\0';

    printf("\n");
    printf("Okay %s, ", input.name);
    type_text("the starship is running on our backup generators, so the systems are running at low efficient levels. "
                "I am not able to identify who you are. First I need to know your planet of origin and profession.\n\n", 40);

        // free memory
    free(user_name);
    user_name = NULL;
    }

    do {
        printf("Are you Human or Velkin? ");
        scanf("%s", input.race);

        if (strcmp(input.race, "Human") != 0 && strcmp(input.race, "human") != 0
        && strcmp(input.race, "Velkin") != 0 && strcmp(input.race, "velkin") != 0) {
            printf("\nNot a valid origin.\n\n");
        }
    } while (strcmp(input.race, "Human") != 0 && strcmp(input.race, "human") != 0 
    && strcmp(input.race, "Velkin") != 0 && strcmp(input.race, "velkin") != 0);

    do {
        printf("Is your profession an Engineer or Gunslinger? ");
        scanf("%s", input.profession);

        if (strcmp(input.profession, "Engineer") != 0 && strcmp(input.profession, "engineer") != 0
        && strcmp(input.profession, "Gunslinger") != 0 && strcmp(input.profession, "gunslinger") != 0) {
            printf("\nNot a valid profession.\n\n");
        }
    } while (strcmp(input.profession, "Engineer") != 0 && strcmp(input.profession, "engineer") != 0
    && strcmp(input.profession, "Gunslinger") != 0 && strcmp(input.profession, "gunslinger") != 0);

    loading_animation();
    printf("\n");

    display_stats(input);
    printf("\n");

    inventory();
    printf("\n");

    printf("Uploading USS Ozark blueprints into your neural database."
            "Give me a moment...\n");
    
    loading_animation();
    printf("\n\n");

    create_map();

    printf("Complete...\n");
    type_text("You should have the blueprints downloaded into your directory. Filename >>> blueprints.txt\n", 30);
    printf("\n");
    type_text("I need you to locate the engine bay and place the fusion cores into the main nuclear reactors. "
                "Once that is complete, I will be able to power our defense systems and locate unknown "
                "terrestrials aboard this fleet.\n", 30);
    printf("\n\n");

    location();

    printf("Down the corridor you see a shadown lurking underneath the flickering lights.\n");
    printf("It's a Big Ass Alien!\n");

    if (input.profession == "Engineer" || input.profession == "engineer") {
        engineer_combat();
    }
    else {
        gunslinger_combat();
    }

    printf("You continue down the corridor and finally reach the engine bay. On your right, you see the fusion cores."
            "You reach down and pick them up and one by one, inserting them into the reactors.\n\n");
    type_text("This is Captain S. Blue. Defense systems is online and terrestrials have been identified. "
                "All personel report to the armory.\n", 30);
    printf("\n\n\nEND OF CHAPTER 1");

    return 0;
}

void display_stats(struct player input){
    printf("Name: %s\n", input.name);
    printf("Origin: %s\n", input.race);
    printf("Profession: %s\n", input.profession);
    printf("Health Points: %d\n", HP);
    printf("Energy: %d\n", ENERGY);
}