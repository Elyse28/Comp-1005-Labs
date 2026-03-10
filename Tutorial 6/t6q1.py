def add_dr_prefix_copied(name_list):
    return ["Dr. " + name for name in name_list]

def add_dr_prefix_inplace(name_list):
    scs_profs = name_list
    return None

def main():
	scs_profs = ["Michel Barbeau","Olga Baysal","Ava McKenney","Robert Collier"]
	doctors = ["Dr. Barbeau", "Dr. Baysal", "Dr. McKenney", "Dr. Collier"]
	copied = add_dr_prefix_copied(scs_profs)

	unchanged = (scs_profs==["Michel Barbeau","Olga Baysal","Ava McKenney","Robert Collier"])
	correctly_titled_copy = (copied == doctors)

	add_dr_prefix_inplace(scs_profs)
	correctly_titled_inplace = unchanged and (scs_profs == doctors)

	print("Didn't modify the original list: ", unchanged)
	print("Correctly titled copy: ", correctly_titled_copy)
	print("Correctly titled in-place: ", correctly_titled_inplace)

main()