def count_un_an_patterns(text):
    """
    Counts the number of occurrences of a pattern that starts with "un", has unlimited number of letters and ends with "an"

    Args:
        text: The text to search.

    Returns:
        The number of occurrences of the pattern.
    """
    count = 0
    i = 0  # Initialize an index to track our position in the text

    while i < len(text):
        # Check if we find the start of the pattern ("un")
        if text[i:i + 2] == "un":
            j = i + 2  # Move the index past the "un"

            # Keep moving until we find "an" or the end of the text
            while j < len(text) and text[j:j + 2] != "an":
                j += 1

            # Check if we found the "an" ending
            if j < len(text) and text[j:j + 2] == "an":
                count += 1
                i = j + 2  # Move past the completed pattern to find the next one
            else:
                i += 1  # If "an" wasn't found, move on in the text

        else:
            i += 1  # No "un" found, move to the next character

    return count


# Example usage:
text = "The uncompleted unfinished unanswerable unbreakable unchangeable unnoticeable unpredicted unpreventable unquantifiable unquantifiable unquantifiable unquantifiable unquantifiable unquantifiable unapproachable unapproachable unapproachable unapproachable unapproachable unapproachable unapproachable unapproachable unapproachable unapproachable"
pattern_count = count_un_an_patterns(text)

print(f"The text contains {pattern_count} occurrences of the 'un...an' pattern.")
