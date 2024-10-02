

def binary_label_encoding(X):
    return X.map(lambda x: 1 if x in ['Yes', 'Urban', True] else 0)
