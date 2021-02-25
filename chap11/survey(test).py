class anonymousSurvey:

	def __init__(self, question):
		self.question = question
		self.response = []

	def show_question(self):
		print(self.question)

	def store_results(self, new_response):
		self.responses.append(new_responses)

	def show_results(self):
		print("survey results:")
		for response in self.responses:
			print(f"- {response}")