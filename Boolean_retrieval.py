# Define the documents
documents = {
    1: "apple banana orange",
    2: "apple banana",
    3: "banana orange",
    4: "apple"
}

# Function to build an inverted index
def build_index(docs):
    index = {}  # empty dictionary

    for doc_id, text in docs.items():
        terms = set(text.split())  # split words

        for term in terms:
            if term not in index:
                index[term] = {doc_id}
            else:
                index[term].add(doc_id)

    return index


# Build inverted index
inverted_index = build_index(documents)


# Boolean AND operation
def boolean_and(operands, index):
    if not operands:
        return list(range(1, len(documents) + 1))

    result = index.get(operands[0], set())

    for term in operands[1:]:
        result = result.intersection(index.get(term, set()))

    return list(result)


# Boolean OR operation
def boolean_or(operands, index):
    result = set()

    for term in operands:
        result = result.union(index.get(term, set()))

    return list(result)


# Boolean NOT operation
def boolean_not(operand, index, total_docs):
    operand_set = set(index.get(operand, set()))
    all_docs_set = set(range(1, total_docs + 1))

    return list(all_docs_set.difference(operand_set))


# Example queries
query1 = ["apple", "orange"]
query2 = ["apple", "orange"]


# Perform Boolean queries
result1 = boolean_and(query1, inverted_index)
result2 = boolean_or(query2, inverted_index)
result3 = boolean_not("orange", inverted_index, len(documents))


# Print results
print("Documents containing 'apple' and 'banana':", result1)
print("Documents containing 'apple' or 'orange':", result2)
print("Documents not containing 'orange':", result3)
