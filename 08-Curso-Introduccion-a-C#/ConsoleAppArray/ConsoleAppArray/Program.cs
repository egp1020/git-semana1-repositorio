// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

string[] coffeeTypes;
float[] coffeeValues;

coffeeTypes = new string[] { "Express", "Latte", "Capuccino", "Tinto" };
coffeeValues = new float[] { 1.2f, 2.5f, 3.5f, 6.5f };

coffeeTypes[3] = "Té chai";

for (int i = 0; i < coffeeTypes.Length; i++)
    Console.WriteLine(coffeeTypes[i]+": $"+coffeeValues[i]);

