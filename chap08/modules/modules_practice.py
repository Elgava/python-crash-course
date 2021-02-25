def print_models(unprinted_models, completed_models):

	while unprinted_design:
		current_design = unprinted_models.pop()
		print(f"printing model:{current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print("\n the following models have been printed")
	for completed_model in completed_models:
		print(completed_model)