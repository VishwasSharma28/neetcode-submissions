
from typing import List

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: Create an empty dictionary to store the frequency
        # of every unique number present in the input list.
        frequency_dictionary = {}

        # Step 2: Iterate through every number in the given list.
        for current_number in nums:

            # Step 3: Check whether the current number is already
            # present in our frequency dictionary.
            if current_number in frequency_dictionary:

                # If it already exists, increase its frequency by one.
                frequency_dictionary[current_number] = (
                    frequency_dictionary[current_number] + 1
                )

            else:

                # If it does not exist, insert it into the dictionary
                # and initialize its frequency to one.
                frequency_dictionary[current_number] = 1

        # Step 4: Create a separate list containing all unique numbers.
        unique_numbers = []

        # Step 5: Iterate through every key in the frequency dictionary.
        for current_number in frequency_dictionary:

            # Add each unique number to the list.
            unique_numbers.append(current_number)

        # Step 6: Sort the unique numbers according to their frequencies.
        # The sorting function uses the frequency dictionary to determine
        # the frequency associated with each number.
        unique_numbers.sort(
            key=lambda number: frequency_dictionary[number],
            reverse=True
        )

        # Step 7: Create an empty list to store the final answer.
        result = []

        # Step 8: Start an index at zero.
        current_index = 0

        # Step 9: Continue until we have collected k elements
        # or have exhausted all unique numbers.
        while current_index < k and current_index < len(unique_numbers):

            # Retrieve the number at the current sorted position.
            current_number = unique_numbers[current_index]

            # Add that number to the answer.
            result.append(current_number)

            # Move to the next position.
            current_index += 1

        # Step 10: Return the k most frequent numbers.
        return result
