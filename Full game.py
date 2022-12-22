class game():
    def __init__(self):
        print('''Welcome To The Full Game

                Choose Your Game From Our Collection:
                ''')

        self.choices()
        
    def choices(self):
        press = input('''
                         Press [1]: Play the even-odd game
                         Press [2]: Play sum average game
                         Press [3]: Play the multiplication table game: ''')
        try:
            press = int(press)
            if press ==1:
                self.odd_even()
            
            elif press==2:
                self.sum_avg()
                
            elif press==3:
                self.multiplication_game()
            else:
                print('Please choose from 1 to 3')

        except ValueError:
            print('Please enter a valid number')
        replay = input('play game? [Y/N]: ')
        if replay == 'Y' or replay == 'y':
            self = game()
        elif replay == 'N' or replay == 'n':
            print('GoodBye')
        else:
            print('please choose either Y or N')
            self = game()

            

    ##odd and even game        
    def odd_even(self):
        print('--Welcome in the even-odd game--\n')
        print('To play: choose a number, To exit game: press x')
        while True:
            Guess = input('>> Guess a number: ')
            if Guess == 'x':
                print("Exit game, bye :)")
                break
            try:
                Guess = int(Guess)
                
                if Guess%2 ==0:
                    print('This is an even number')
                else:
                    print('This is an odd number')
                    
            except ValueError:
                print('Invalid value, please enter a number')

            print('-----------------------')
            print('Play again?')

    ##sum and average game 
    def sum_avg(self):
        print('This program takes numbers and return the sum\n')
        numbers = int(input('How many numbers you want to calculate the sum? '))

        count = 0
        summ = 0
        while count<numbers:
            number = float(input("Enter a number: "))
            count += 1
            summ +=number
        print("The sum is: ", summ)
        print("The average is: ", summ/numbers)

    ##multiplication game 
    def multiplication_game(self):
        print('This program takes two numbers and print their multiplication table\n')
        start = int(input('Enter the first number: '))
        end = int(input('Enter the second number: '))
        for x in range(start,end+1):
            for m in range(1,13):
                print(x, "*", m, "=", x*m)
            print('-------------')

game1 = game()
