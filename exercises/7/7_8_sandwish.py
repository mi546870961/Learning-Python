sandwish_orders=['pastrami','tuna','ham','egg']
finished_sandwishes=[]

while sandwish_orders:
	current_sandwish=sandwish_orders.pop()
	finished_sandwishes.append(current_sandwish)
	print("I made your "+current_sandwish+"sandwish")
print("\nThese sandwishes have been made.")
for sandwish in finished_sandwishes:
	print(sandwish)
