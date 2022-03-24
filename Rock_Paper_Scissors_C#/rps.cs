using System;

namespace RPS

{
    class Program
{
    static void Main(string[] args)

    {
        string userInput, systemInput;

        int randomNum;

        Console.WriteLine("Give an input from Rock/ Paper/ Scissors");

        userInput = Console.ReadLine();

        Random rnd = new Random();

        randomNum = rnd.Next(1,4);

        switch (randomNum)
        {
            case 1: 
                   
                   systemInput = "Rock";
                   Console.WriteLine("Computer chose rock");

                   if (userInput == "Rock")

                   {
                       Console.WriteLine("It is a draw!");

                   } else if(userInput == "Paper")

                   {
                       Console.WriteLine("You loose");
                   }
                   else
                   {
                       Console.WriteLine("You win");
                   }
                   break;
            

            case 2: 
                   
                   systemInput = "Paper";

                   Console.WriteLine("Computer chose paper");

                   if (userInput == "Rock")
                   {
                       Console.WriteLine("You lose!");
                   }
                   else if (userInput == "Paper")
                   {
                       Console.WriteLine("It is a draw");
                   }
                   else
                   {
                       Console.WriteLine("You win");
                   }
                   break;

            case 3: 
                   
                   systemInput = "Scissors";

                   Console.WriteLine("Computer chose Scissors");

                   if (userInput == "Rock")
                   {
                       Console.WriteLine("You Win");
                   }
                   else if (userInput == "Paper")
                   {
                       Console.WriteLine("You lose");
                   }
                   else

                   { 
                       Console.WriteLine("It is a draw");
                   }
                   break;
                
                default:
                        Console.WriteLine("Invalid Entry!");

                        break;  
                   }
                }
        
}
}

