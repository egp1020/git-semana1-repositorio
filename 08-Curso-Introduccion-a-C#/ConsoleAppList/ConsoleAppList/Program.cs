// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

List<string> stocklistHardwareStore = new List<string>();

stocklistHardwareStore.Add("Screwdriver");
stocklistHardwareStore.Add("Hammer");
stocklistHardwareStore.Add("Wires");
stocklistHardwareStore.Add("Tape");
stocklistHardwareStore.Add("Nail");

foreach (string tool in stocklistHardwareStore) {
    Console.WriteLine(tool);
}

stocklistHardwareStore.Remove("Hammer");
stocklistHardwareStore.RemoveAt(2);

Console.WriteLine("----------------------------------");
for (int i = 0; i < stocklistHardwareStore.Count; i++) { // Count to List, Lenght to Arrays
    Console.WriteLine(stocklistHardwareStore[i]);
}
