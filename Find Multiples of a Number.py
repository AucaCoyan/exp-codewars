def find_multiples(integrer, limit):
    multiples = []
    multiple = integrer
    while multiple <= limit and integrer != 0:
        multiples.append(multiple)
        multiple = multiple + integrer

    print(multiples)
    return


find_multiples(2, 8)
