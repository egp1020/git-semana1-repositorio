// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");


// &&, ||, !
bool value1 = true;
bool value2 = false;
bool value3 = false;
bool value4 = true;

bool result1 = value1 && value2;
bool result2 = value2 && value3;
bool result3 = value1 && value4 && value3;

bool result4 = value1 || value4;
bool result5 = value2 || value4;
bool result6 = (value4 || value1) && value2;

bool result7 = !value1;
bool result8 = !value2;


Console.WriteLine("The result of the logical AND is: " + result1);
Console.WriteLine("The result of the logical AND is: " + result2);
Console.WriteLine("The result of the logical AND is: " + result3);
Console.WriteLine("The result of the logical OR is: " + result4);
Console.WriteLine("The result of the logical OR is: " + result5);
Console.WriteLine("The result of the logical AND/OR is: " + result6);
Console.WriteLine("The result of the logical NOT is: " + result7);
Console.WriteLine("The result of the logical NOT is: " + result8);