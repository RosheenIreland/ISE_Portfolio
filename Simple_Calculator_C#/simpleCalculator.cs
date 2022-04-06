// Converting Calculator to C#

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CalculatorApp {
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Enter Your Choice: ");
            Console.WriteLine("1: Addition ");
            Console.WriteLine("2. Subtraction ");
            Console.WriteLine("3. Multiplication ");
            Console.WriteLine("4. Divison ");

            int action = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter 1st Number:");

            int input_1 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter 2nd Number:");

            int input_2 = Convert.ToInt32(Console.ReadLine());
            int result = 0;
            switch (action) {

                case 1: {
                    result = Addition(input_1, input_2);
                    break;
                }
                case 2: {
                    result = Subtraction(input_1, input_2);
                    break;
                }
                case 3: {
                    result = Multiplication(input_1, input_2);
                    break;
                }
                case 4: {
                    result = Division(input_1, input_2);
                    break;
                }
                default: 
                    Console.WriteLine("Wrong Input! Try again.");
                    break;
            }
            Console.WriteLine("The result is {0}", result);
            Console.ReadKey();            
        }
         //Additon
        public static int Addition(int input_1, int input_2) {
        int result = input_1 + input_2;
        return result;
        }
         //Subtraction
        public static int Subtraction(int input_1, int input_2) {
        int result = input_1 - input_2;
        return result; 
        }
         //Multiplication
        public static int Multiplication(int input_1, int input_2) {
        int result = input_1 * input_2;
        return result;
        }
        //Division
        public static int Division(int input_1, int input_2) {
        int result = input_1 / input_2;
        return result;
        }
    }
}