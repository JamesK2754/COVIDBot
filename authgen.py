import random

def generate(name):
    auth = name
    greeklist = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa", "Lambda", "Mu", "Nu", "Xi", "Omicron", "Pi", "Rho", "Sigma", "Tau", "Opsilon", "Fie", "Chi", "Psi", "Omega"]
    greekno = random.randint(1, 24)
    random1 = random.randint(0, 9)
    random2 = random.randint(0, 9)
    random3 = random.randint(0, 9)
    
    auth = (f"{auth}-{greeklist[greekno]}-{random1}-{random2}-{random3}")
    return auth

print(generate("King"))