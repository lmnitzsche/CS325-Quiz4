from yoda.yoda_fact import yoda_fun_fact
from anakin.anakin_fact import anakin_fun_fact
from luke.luke_fact import luke_fun_fact

def main():
    yodaFact = yoda_fun_fact()
    anakinFact = anakin_fun_fact()
    lukeFact = luke_fun_fact()

    print(f"Fun Fact about Yoda: {yodaFact}")
    print(f"Fun Fact about Anakin: {anakinFact}")
    print(f"Fun Fact about Luke: {lukeFact}")

if __name__ == "__main__":
    main()
