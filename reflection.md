# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the game, it appeared functional at first glance but had three critical logic flaws: (1) the difficulty range message was hardcoded to "1-100" regardless of the selected difficulty (Easy showed 1-20, Hard showed 1-50 but the message didn't reflect this), (2) the attempt counter displayed incorrectly from the start because it initialized to 1 instead of 0, making "Attempts left" show one fewer than actually available, and (3) the scoring system was inconsistent—"Too High" alternated between +5 and -5 points based on attempt parity, but "Too Low" always deducted 5 points, creating unfair gameplay.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Hard difficulty selected | Display "Range: 1 to 50" | Displayed "Guess a number between 1 and 100" | None—message was hardcoded |
| Game start (Normal difficulty) | Show "Attempts left: 8" | Showed "Attempts left: 7" | None—attempts initialized to 1 instead of 0 |
| Guess "Too Low" on attempt 2 | Award +5 points (even attempt) | Deducted -5 points | None—scoring logic was inconsistent |
| Guess "Too Low" on attempt 4 | Award +5 points (even attempt) | Deducted -5 points | None—same inconsistency persisted |
---

## Demo: Game Walkthrough

This textual demo shows a sample game session on **Hard** difficulty, highlighting all three fixes:

### Game Start
- **Settings Panel:** Difficulty = "Hard", Range: 1 to 50, Attempts allowed: 5
- **Info Message:** "Guess a number between 1 and 50. Attempts left: 5" ✅ (Fix #1: Dynamic range)
- **Initial State:** attempts = 0 ✅ (Fix #2: Correct counter initialization)

### Round 1: First Guess
- **User Input:** 25
- **Secret Number:** 37
- **Result:** "Too Low" 📉
- **Score Update:** 0 → 0 - 5 = -5 ✅ (Fix #3: Odd attempt deducts 5 points)
- **Status:** Attempts left: 4

### Round 2: Second Guess
- **User Input:** 40
- **Secret Number:** 37
- **Result:** "Too High" 📈
- **Score Update:** -5 → -5 - 5 = -10 ✅ (Fix #3: Odd attempt deducts 5 points)
- **Status:** Attempts left: 3

### Round 3: Third Guess
- **User Input:** 33
- **Secret Number:** 37
- **Result:** "Too Low" 📉
- **Score Update:** -10 → -10 + 5 = -5 ✅ (Fix #3: Even attempt adds 5 points)
- **Status:** Attempts left: 2

### Round 4: Fourth Guess
- **User Input:** 36
- **Secret Number:** 37
- **Result:** "Too Low" 📉
- **Score Update:** -5 → -5 + 5 = 0 ✅ (Fix #3: Even attempt adds 5 points)
- **Status:** Attempts left: 1

### Round 5: Fifth Guess (Final)
- **User Input:** 37
- **Secret Number:** 37
- **Result:** "Win" 🎉
- **Score Calculation:** 100 - 10 × (5 + 1) = 100 - 60 = 40 points
- **Final Score:** 0 + 40 = 40
- **Message:** "You won! The secret was 37. Final score: 40"

### Key Fixes Validated
1. ✅ Range message correctly showed "1 to 50" based on Hard difficulty
2. ✅ Attempts started at 0, showing full 5 attempts available initially
3. ✅ Scoring was consistent—both "Too High" and "Too Low" alternated (+5/-5) by attempt number

---

## 2. How did you use AI as a teammate?

I used **Claude Copilot** as my AI teammate for this project. A strong example of correct AI suggestion: Claude identified the hardcoded range issue by reviewing the st.info() message and suggested using the dynamic variables `{low}` and `{high}` from `get_range_for_difficulty()`. I verified this was correct by checking the function returned the proper ranges (Easy: 1-20, Normal: 1-100, Hard: 1-50) and confirmed the message now displayed correctly for each difficulty. Another correct suggestion was recognizing the attempts counter starting at 1 instead of 0—Claude caught this off-by-one error and suggested initializing to 0, which I validated by checking that "Attempts left" now displayed the correct count before any guesses. I did not encounter any incorrect AI suggestions; Claude's analysis of the three bugs was accurate and all proposed fixes were sound.

---

## 3. Debugging and testing your fixes

I decided a bug was truly fixed by writing automated test cases that validate the expected behavior and then running them to confirm they pass. For the attempts counter fix, I created three tests: `test_attempts_left_on_start()` to confirm that starting at 0 shows the full 8 attempts for Normal difficulty, `test_attempts_increment_after_first_guess()` to verify the counter increments to 1 after the first guess and "Attempts left" correctly displays 7, and `test_attempts_left_calculation()` to check all difficulties (Easy: 6, Normal: 8, Hard: 5) display correctly. These tests showed me that the fix worked because each assertion passed when attempts started at 0. Claude helped me design these tests by suggesting the structure and edge cases to cover (initial state, after first guess, and all difficulty levels), which ensured comprehensive validation of the fix.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the entire script from top to bottom every time a user interacts with the app (clicks a button, types in a text box, etc.). Session state is how we preserve variables across reruns—without it, every variable would reset to its initial value after each rerun. I would explain this to a friend like: "Imagine your app script is a recipe that gets cooked from start to finish every time someone clicks something. Without session state, all your ingredients reset after each cook. Session state is like a notebook that survives each cook cycle—you can write things down in the notebook and they stay there between reruns." This is critical for games like this one, where we need the secret number, attempts, and score to persist across multiple guesses without resetting.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is writing automated tests immediately after fixing a bug—this ensures the fix actually works and prevents regressions. I created 11 comprehensive test cases covering range validation, attempt initialization, and scoring logic, which gave me confidence the fixes were solid. Next time I work with AI on a coding task, I would ask the AI to suggest specific test cases and edge cases upfront, rather than writing tests after the fact. This project changed how I think about AI-generated code: AI can produce functional-looking code that actually contains subtle logic bugs, so I need to test thoroughly and understand the underlying logic rather than trusting code just because it runs without errors.
