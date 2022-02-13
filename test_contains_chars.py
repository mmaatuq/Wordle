def contains_chars_exact_loc(word, chars_loc):
    chars = [chars_loc[c] for c in range(0, len(chars_loc), 2)]
    locs = [int(chars_loc[c + 1]) for c in range(0, len(chars_loc), 2)]
    for c, l in zip(chars, locs):
        if word[l] != c:
            return False
    return True


a = contains_chars_exact_loc("ulcer", "l1u0")
