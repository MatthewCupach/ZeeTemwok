print("Welcome to Rock-Paper-Scissors!")

#Player input
playerChoice = input("Enter your pick: Rock, Paper, or Scissors ")

#Computer Output


#Victory
playerChoice = playerChoice.lower()
match playerChoice:
    case "rock":
        match comp_choice:
            case "Rock":
                print("It's a tie!")
            case "Scissors":
                print("You win!")
            case "Paper":
                print("You lose.")
    case "paper":
        match comp_choice:
            case "Rock":
                print("You win!")
            case "Scissors":
                print("You lose.")
            case "Paper":
                print("It's a tie!")
    case "scissors":
        match comp_choice:
            case "Rock":
                print("You lose.")
            case "Scissors":
                print("It's a tie!")
            case "Paper":
                print("You win!")
    case _:
        print("Uh... That's... not an option.")