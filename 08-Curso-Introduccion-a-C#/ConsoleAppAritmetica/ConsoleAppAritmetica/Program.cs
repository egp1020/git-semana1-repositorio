// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
// This program calculate rectangle area.


float number1;
int number2;

Console.WriteLine("Input the rectangle base: ");
number1 = float.Parse(Console.ReadLine());

Console.WriteLine("Input the rectangle height: ");
number2 = Convert.ToInt32(Console.ReadLine());


float area = number1 * number2;

Console.WriteLine("The area is: "+area);
