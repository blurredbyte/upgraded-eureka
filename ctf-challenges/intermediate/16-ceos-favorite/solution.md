# Solution: The CEO's Favorite

This challenge is an Open Source Intelligence (OSINT) task that requires careful reading of a simulated social media profile to find a piece of personal information.

## Steps to Solve

1.  **Analyze the Profile:**
    The `social_media_profile.txt` file contains a series of posts from the CEO, John Smith. The goal is to find the name of his first pet.

2.  **Search for Clues:**
    You need to read through the posts, looking for any mention of pets, childhood, or family history. The posts are in reverse chronological order, so the relevant information is likely further down.

3.  **Find the Key Post:**
    After scrolling through several posts about business and recent events, you will find a "Throwback Thursday" post:
    ```
    John Smith - 15 hours ago
    #ThrowbackThursday to my childhood best friend! This is a picture of me and my first dog, Buddy, back in 1995. He was the best golden retriever a kid could ask for. Miss you, boy!
    [Image: A faded picture of a young boy with a golden retriever]
    ```

4.  **Identify the Flag:**
    This post explicitly states that the name of his first pet dog was "Buddy".

5.  **Format the Flag:**
    The flag format is `ICIMS{PetName}`. Applying leetspeak to "Buddy" gives "8UDDY". So, the flag is `ICIMS{8UDDY}`.

## Organizer Notes

*   **Hosting:** This is a static challenge. The `social_media_profile.txt` file should be provided to the participants.
*   **Flag:** `ICIMS{8UDDY}`
*   **Note:** This challenge is designed to teach participants how much personal information can be gleaned from social media profiles and how this information could be used to answer security questions or in social engineering attacks. The profile is simulated to avoid any issues with targeting real people.
