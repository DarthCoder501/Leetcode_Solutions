class Solution:
    # Define a method to determine if ransomNote can be constructed from magazine
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Initialize dictionaries to count the frequency of characters in ransomNote and magazine
        note_count = {}
        mag_count = {}

        # Populate the note_count dictionary with the frequency of each character in ransomNote
        for x in ransomNote:
            if x in note_count:
                note_count[x] += 1
            else:
                note_count[x] = 1

        # Populate the mag_count dictionary with the frequency of each character in magazine
        for x in magazine:
            if x in mag_count:
                mag_count[x] += 1
            else:
                mag_count[x] = 1

        # Compare the character counts in ransomNote against those in magazine
        for key, value in note_count.items():
            # If the character is not in magazine or not enough occurrences are present, return False
            if key not in mag_count or mag_count[key] < value:
                return False
        
        # If all characters in ransomNote can be constructed from magazine, return True
        return True
