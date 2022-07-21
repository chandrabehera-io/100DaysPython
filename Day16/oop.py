from prettytable import PrettyTable
my_table = PrettyTable()
my_table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squirtle"])
my_table.add_column("Type", ["Electric", "Fire", "Water"])
my_table.align="l"
print(my_table)
