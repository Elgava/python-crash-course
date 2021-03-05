from random import choice

questions = ["why is teh sky blue?: ", "why do dogs have such shap teeth?: ", "why are you so mean?: "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()
    
    
print("OH, Okay...")
