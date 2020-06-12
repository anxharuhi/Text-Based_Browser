def heading(header, level = 1):
    if level < 1:
        return '# ' + header
    elif level > 6:
        return '###### ' + header
    else:
        return '#' * level + ' ' + header

