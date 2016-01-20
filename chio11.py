def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if isinstance(v, dict) and  v:
                stack.append((path + (k,), v))
            else:
                result["/".join((path + (k,)))] = v if v else ""
    return result
    
print flatten({"key": "value"})
