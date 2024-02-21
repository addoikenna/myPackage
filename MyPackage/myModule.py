def top_n(items, n):
    """
        Return the top n items in an array, in descending order.

        Args:
            items(array): List or array like objects
            n(int) : Number of items to return

        Return:
            array : top n items in descending order
        
        Eg:
            >>>top_n([8, 3, 2, 7, 4], 3)
            [8, 7, 4]
    """
    for i in range(n):
        for j in range(len(items) - 1 - i):

            if items[j] > items[j+1]: # if the item is bigger than gthe next
                items[j], items[j+1] = items[j+1], items[j] # Swap the two

    top_n = items[-n:]

    return top_n[::-1]
