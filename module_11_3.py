def introspection_info(obj):
    obj_info = {
        'type': type(obj).__name__,
        'module': getattr(obj, '__module__', None),
        'attributes': [a for a in dir(obj) if not callable(getattr(obj, a, None))],
        'methods': [a for a in dir(obj) if callable(getattr(obj, a, None))]
    }

    if isinstance(obj, (list, tuple, set, frozenset, dict, str)):
        obj_info['length'] = len(obj)
    if isinstance(obj, (list, tuple, set, frozenset)):
        obj_info['sample_items'] = list(obj)[:5]
    elif isinstance(obj, dict):
        obj_info.update(sample_keys=list(obj)[:5], sample_values=list(obj.values())[:5])
    elif isinstance(obj, str):
        obj_info['sample'] = obj[:20]
    elif isinstance(obj, (int, float, complex)):
        obj_info['numeric_properties'] = {
            'is_integer': isinstance(obj, int),
            'is_finite': obj not in (float('inf'), float('-inf'))
        }

    return obj_info


if __name__ == "__main__":
    print(introspection_info([1, 2, 3, 4, 5]))