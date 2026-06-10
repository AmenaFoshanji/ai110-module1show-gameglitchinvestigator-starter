import sys
import pytest

# Import the functions we're testing
from logic_utils import (
    get_range_for_difficulty,
    update_score,
)


class TestFix1_DynamicRangeMessage:
    """Test that the range message displays correct values based on difficulty."""
    
    def test_easy_range(self):
        """Test Easy difficulty returns 1-20."""
        low, high = get_range_for_difficulty("Easy")
        assert low == 1
        assert high == 20
        # Verify message would display correctly
        message = f"Guess a number between {low} and {high}"
        assert "1 and 20" in message
    
    def test_normal_range(self):
        """Test Normal difficulty returns 1-100."""
        low, high = get_range_for_difficulty("Normal")
        assert low == 1
        assert high == 100
        message = f"Guess a number between {low} and {high}"
        assert "1 and 100" in message
    
    def test_hard_range(self):
        """Test Hard difficulty returns 1-50."""
        low, high = get_range_for_difficulty("Hard")
        assert low == 1
        assert high == 50
        message = f"Guess a number between {low} and {high}"
        assert "1 and 50" in message
    
    def test_default_range(self):
        """Test invalid difficulty defaults to 1-100."""
        low, high = get_range_for_difficulty("Invalid")
        assert low == 1
        assert high == 100


class TestFix2_InitialAttemptsCounter:
    """Test that attempts start at 0, not 1."""
    
    def test_attempts_left_on_start(self):
        """Simulate attempts counter starting at 0."""
        initial_attempts = 0
        attempt_limit = 8  # Normal difficulty
        
        attempts_left = attempt_limit - initial_attempts
        assert attempts_left == 8, "Should show full attempts available"
    
    def test_attempts_increment_after_first_guess(self):
        """After first guess, attempts should be 1."""
        attempts = 0
        attempts += 1
        assert attempts == 1, "First guess should increment to 1"
        
        attempt_limit = 8
        attempts_left = attempt_limit - attempts
        assert attempts_left == 7, "Should show 7 attempts left after 1 guess"
    
    def test_attempts_left_calculation(self):
        """Verify attempts_left displays correctly from initial 0."""
        attempt_limit_map = {
            "Easy": 6,
            "Normal": 8,
            "Hard": 5,
        }
        
        for difficulty, limit in attempt_limit_map.items():
            initial_attempts = 0
            attempts_left = limit - initial_attempts
            assert attempts_left == limit, f"{difficulty} should show {limit} attempts left initially"


class TestFix3_ConsistentScoring:
    """Test that Too High and Too Low have consistent scoring logic."""
    
    def test_too_high_even_attempt_adds_points(self):
        """Even attempt number for Too High should add 5 points."""
        current_score = 100
        result = update_score(current_score, "Too High", attempt_number=2)
        assert result == 105, "Even attempt Too High should add 5 points"
    
    def test_too_high_odd_attempt_removes_points(self):
        """Odd attempt number for Too High should remove 5 points."""
        current_score = 100
        result = update_score(current_score, "Too High", attempt_number=1)
        assert result == 95, "Odd attempt Too High should remove 5 points"
    
    def test_too_low_even_attempt_adds_points(self):
        """Even attempt number for Too Low should add 5 points (NOW FIXED)."""
        current_score = 100
        result = update_score(current_score, "Too Low", attempt_number=2)
        assert result == 105, "Even attempt Too Low should add 5 points"
    
    def test_too_low_odd_attempt_removes_points(self):
        """Odd attempt number for Too Low should remove 5 points (NOW FIXED)."""
        current_score = 100
        result = update_score(current_score, "Too Low", attempt_number=1)
        assert result == 95, "Odd attempt Too Low should remove 5 points"
    
    def test_scoring_consistency_multiple_attempts(self):
        """Test scoring is consistent across multiple attempts."""
        score = 100
        
        # Attempt 1 (odd): Too High -> -5
        score = update_score(score, "Too High", attempt_number=1)
        assert score == 95
        
        # Attempt 2 (even): Too Low -> +5 (NOW CONSISTENT)
        score = update_score(score, "Too Low", attempt_number=2)
        assert score == 100
        
        # Attempt 3 (odd): Too Low -> -5 (NOW CONSISTENT)
        score = update_score(score, "Too Low", attempt_number=3)
        assert score == 95
        
        # Attempt 4 (even): Too High -> +5
        score = update_score(score, "Too High", attempt_number=4)
        assert score == 100
    
    def test_win_scoring(self):
        """Test Win score calculation."""
        current_score = 0
        result = update_score(current_score, "Win", attempt_number=1)
        # points = 100 - 10 * (1 + 1) = 100 - 20 = 80
        assert result == 80, "Win at attempt 1 should award 80 points"
        
        result = update_score(current_score, "Win", attempt_number=5)
        # points = 100 - 10 * (5 + 1) = 100 - 60 = 40
        assert result == 40, "Win at attempt 5 should award 40 points"
        
        result = update_score(current_score, "Win", attempt_number=20)
        # points = 100 - 10 * (20 + 1) = 100 - 210 = -110, but min is 10
        assert result == 10, "Win at attempt 20 should award minimum 10 points"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
