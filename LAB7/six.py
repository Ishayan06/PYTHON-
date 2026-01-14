d = {"a": 30, "b": 10, "c": 20}

sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
print("Sorted Dictionary:", sorted_dict)
