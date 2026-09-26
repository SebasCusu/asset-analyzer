
import random

def verify(player_num, secret_num):
        if player_num > secret_num:
            print("Too High")
            
            
        if player_num < secret_num:
            print("Too Low")

            
        if player_num == secret_num:
            print(f"\nNumber Guessed:\nThe Secret Number Was: {secret_num}")
            return True
        

        
        return False

def show_menu():
    print("\nGuess The Number")
    print("1-100")
    

def main():
    show_menu()
    random_num = random.randint(1, 100)
    
    while True:
        try:
            player_num = int(input("Guess the number: "))
        
            if verify(player_num, random_num):
                break
                
        except ValueError:
            print("Invalid Number")
            
            
            
if __name__ == "__main__":
    main()