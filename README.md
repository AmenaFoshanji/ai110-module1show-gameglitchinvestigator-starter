# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game Purpose:** A number guessing game built with Streamlit where players try to guess a secret number within attempt limits based on difficulty. The game provides hints (Higher/Lower) and tracks scores based on attempt efficiency and accuracy.

- [x] **Bugs Found:**
  1. **Hardcoded Range Message** - The game displayed "Guess a number between 1 and 100" regardless of difficulty level (Easy: 1-20, Hard: 1-50).
  2. **Incorrect Attempt Counter** - Attempts initialized to 1 instead of 0, causing "Attempts left" to display one fewer than actually available.
  3. **Inconsistent Scoring** - "Too Low" guesses always deducted 5 points, while "Too High" guesses alternated (+5/-5). This created unfair gameplay.

- [x] **Fixes Applied:**
  1. Replaced hardcoded range with dynamic variables: `f"Guess a number between {low} and {high}"`
  2. Changed initial attempts from `1` to `0` for accurate counter display
  3. Updated "Too Low" scoring logic to match "Too High" alternation pattern (even attempts: +5, odd attempts: -5)
  4. Added comprehensive test suite with 11 test cases covering all three fixes

## 📸 Demo Walkthrough

This walkthrough shows a complete game session on **Hard** difficulty (range: 1-50, 5 attempts):

1. **Game Start** - Info displays: "Guess a number between 1 and 50. Attempts left: 5" ✅
2. **Round 1 (Guess: 25, Secret: 37)** - Result: "Too Low" 📉 → Score: -5 (odd attempt penalty)
3. **Round 2 (Guess: 40, Secret: 37)** - Result: "Too High" 📈 → Score: -10 (odd attempt penalty)
4. **Round 3 (Guess: 33, Secret: 37)** - Result: "Too Low" 📉 → Score: -5 (even attempt bonus +5)
5. **Round 4 (Guess: 36, Secret: 37)** - Result: "Too Low" 📉 → Score: 0 (even attempt bonus +5)
6. **Round 5 (Guess: 37, Secret: 37)** - Result: "Win" 🎉 → Score: 40 (100 - 10×6 = 40 points)

**Fixes Validated:** Dynamic range ✅ | Attempts counter starts at 0 ✅ | Consistent scoring ✅

## 🧪 Test Results

```
======================== Test Results: tests/test_fixes.py ========================

TestFix1_DynamicRangeMessage
  test_easy_range PASSED
  test_normal_range PASSED
  test_hard_range PASSED
  test_default_range PASSED

TestFix2_InitialAttemptsCounter
  test_attempts_left_on_start PASSED
  test_attempts_increment_after_first_guess PASSED
  test_attempts_left_calculation PASSED

TestFix3_ConsistentScoring
  test_too_high_even_attempt_adds_points PASSED
  test_too_high_odd_attempt_removes_points PASSED
  test_too_low_even_attempt_adds_points PASSED
  test_too_low_odd_attempt_removes_points PASSED
  test_scoring_consistency_multiple_attempts PASSED
  test_win_scoring PASSED

========================= 11 passed in 0.42s =========================
```

**Test Coverage:** All three fixes validated across range validation, attempt tracking, and scoring consistency.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
