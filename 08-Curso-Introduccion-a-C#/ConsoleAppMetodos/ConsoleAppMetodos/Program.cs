// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

float[] curso;

curso = new float[10];
curso[0] = 1.5f;
curso[1] = 2.5f;
curso[2] = 3f;
curso[3] = 5f;

Random rnd = new Random();
Console.WriteLine("Random number: ");
Console.WriteLine($"{rnd.Next(1, 10)}");

