"""
Rock Paper Scissors Game
A GUI implementation of the classic game with score tracking and visual feedback
"""

import random
import tkinter as tk
from tkinter import ttk, messagebox

class RockPaperScissorsGame:
    def __init__(self, root):
        """Initialize the game window and main components"""
        self.root = root
        self.root.title("🎮 Rock Paper Scissors")
        self.root.geometry("1000x800")  # Initial window size
        self.root.minsize(900, 700)    # Minimum size to ensure all elements fit
        self.root.configure(bg="#f0f8ff")  # Light blue background
        
        # Create a main frame that contains all game elements
        self.main_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.main_frame.pack(fill="both", expand=True)
        
        # Game state variables
        self.player_score = 0      # Track player wins
        self.computer_score = 0    # Track computer wins
        self.round = 0            # Track total rounds played
        
        # Color scheme dictionary for consistent styling
        self.colors = {
            "background": "#f0f8ff",   # Main background
            "primary": "#4a6fa5",      # Header color
            "secondary": "#166088",    # Secondary text color
            "accent": "#4fc3f7",      # Button highlight color
            "text": "#333333",         # Main text color
            "player_bg": "#e6f7ff",    # Player choice background
            "computer_bg": "#ffe6e6",  # Computer choice background
            "vs_bg": "#f0f0f0",       # VS separator background
            "rock": "#ff6b6b",        # Red for Rock
            "paper": "#74b9ff",       # Blue for Paper
            "scissors": "#55efc4"     # Green for Scissors
        }
        
        # Initialize all game UI components
        self.create_header()          # Game title and rules
        self.create_choice_buttons()  # Player selection buttons
        self.create_game_display()    # Choice comparison area
        self.create_scoreboard()      # Score tracking
        self.create_bottom_buttons()  # Reset button
        
    def create_header(self):
        """Create the game title header and rules display"""
        header_frame = tk.Frame(self.main_frame, bg=self.colors["primary"])
        header_frame.pack(fill="x", padx=10, pady=10)  # Full width with padding
        
        # Main game title
        title = tk.Label(
            header_frame,
            text="🎮 ROCK - PAPER - SCISSORS 🎮",
            font=("Arial", 24, "bold"),
            fg="white",
            bg=self.colors["primary"],
            padx=20,
            pady=10
        )
        title.pack()
        
        # Game rules subtitle
        rules = tk.Label(
            header_frame,
            text="Rock beats Scissors | Paper beats Rock | Scissors beats Paper",
            font=("Arial", 10),
            fg="white",
            bg=self.colors["primary"],
            pady=5
        )
        rules.pack()
        
    def create_choice_buttons(self):
        """Create the three selection buttons for player choices"""
        button_frame = tk.Frame(self.main_frame, bg=self.colors["background"])
        button_frame.pack(pady=20)  # Add vertical padding
        
        # Rock button with red background
        self.rock_btn = tk.Button(
            button_frame,
            text="🪨 ROCK",
            font=("Arial", 14, "bold"),
            bg=self.colors["rock"],  # Red color
            fg="white",              # White text
            width=12,
            height=2,
            command=lambda: self.play_round("rock")  # Bind to play_round
        )
        self.rock_btn.grid(row=0, column=0, padx=10)  # Grid layout
        
        # Paper button with blue background
        self.paper_btn = tk.Button(
            button_frame,
            text="📄 PAPER",
            font=("Arial", 14, "bold"),
            bg=self.colors["paper"],  # Blue color
            fg="white",
            width=12,
            height=2,
            command=lambda: self.play_round("paper")
        )
        self.paper_btn.grid(row=0, column=1, padx=10)
        
        # Scissors button with green background
        self.scissors_btn = tk.Button(
            button_frame,
            text="✂️ SCISSORS",
            font=("Arial", 14, "bold"),
            bg=self.colors["scissors"],  # Green color
            fg="white",
            width=12,
            height=2,
            command=lambda: self.play_round("scissors")
        )
        self.scissors_btn.grid(row=0, column=2, padx=10)
        
    def create_game_display(self):
        """Create the area that shows player vs computer choices"""
        display_frame = tk.Frame(self.main_frame, bg=self.colors["background"])
        display_frame.pack(pady=20)
        
        # Player choice display (left side)
        self.player_display = tk.Label(
            display_frame,
            text=" Your choice ",
            font=("Arial", 14, "bold"),
            bg=self.colors["player_bg"],  # Light blue background
            fg="black",
            width=18,  # Fixed width for consistent sizing
            relief="ridge",  # 3D border effect
            padx=10,
            pady=10
        )
        self.player_display.grid(row=0, column=0, padx=5, sticky="e")  # Right-aligned
        
        # VS separator label
        vs_label = tk.Label(
            display_frame,
            text=" VS ",
            font=("Arial", 20, "bold"),
            bg=self.colors["vs_bg"],  # Neutral gray background
            fg=self.colors["primary"],
            relief="groove",  # Different border effect
            padx=10,
            pady=10
        )
        vs_label.grid(row=0, column=1, padx=5)
        
        # Computer choice display (right side)
        self.computer_display = tk.Label(
            display_frame,
            text=" Computer's choice ",
            font=("Arial", 14, "bold"),
            bg=self.colors["computer_bg"],  # Light red background
            fg="black",
            width=18,
            relief="ridge",
            padx=10,
            pady=10
        )
        self.computer_display.grid(row=0, column=2, padx=5, sticky="w")  # Left-aligned
        
        # Result announcement label
        self.result_display = tk.Label(
            self.main_frame,
            text="",
            font=("Arial", 20, "bold"),
            bg=self.colors["background"],
            pady=20  # Vertical padding
        )
        self.result_display.pack()
        
    def create_scoreboard(self):
        """Create the score tracking display"""
        score_frame = tk.Frame(self.main_frame, bg=self.colors["background"])
        score_frame.pack(pady=20)
        
        # Scoreboard title
        tk.Label(
            score_frame,
            text="SCOREBOARD",
            font=("Arial", 16, "bold"),
            bg=self.colors["background"],
            fg=self.colors["primary"]
        ).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Player score label
        tk.Label(
            score_frame,
            text="YOU",
            font=("Arial", 14, "bold"),
            bg=self.colors["background"],
            fg=self.colors["secondary"]
        ).grid(row=1, column=0, padx=20)
        
        # Computer score label
        tk.Label(
            score_frame,
            text="COMPUTER",
            font=("Arial", 14, "bold"),
            bg=self.colors["background"],
            fg=self.colors["secondary"]
        ).grid(row=1, column=1, padx=20)
        
        # Player score value display
        self.player_score_label = tk.Label(
            score_frame,
            text="0",
            font=("Arial", 24),  # Larger font for scores
            bg=self.colors["background"],
            fg=self.colors["text"]
        )
        self.player_score_label.grid(row=2, column=0, padx=20)
        
        # Computer score value display
        self.computer_score_label = tk.Label(
            score_frame,
            text="0",
            font=("Arial", 24),
            bg=self.colors["background"],
            fg=self.colors["text"]
        )
        self.computer_score_label.grid(row=2, column=1, padx=20)
        
        # Player progress bar (visual representation of score)
        self.player_progress = ttk.Progressbar(
            self.main_frame,
            orient="horizontal",
            length=400,  # Fixed width
            mode="determinate"  # Shows percentage
        )
        self.player_progress.pack(pady=10)
        
        # Computer progress bar
        self.computer_progress = ttk.Progressbar(
            self.main_frame,
            orient="horizontal",
            length=400,
            mode="determinate"
        )
        self.computer_progress.pack(pady=10)
        
    def create_bottom_buttons(self):
        """Create the bottom control buttons (currently just reset)"""
        # Frame to contain bottom buttons
        bottom_frame = tk.Frame(self.main_frame, bg=self.colors["background"])
        bottom_frame.pack(side="bottom", pady=20, fill="x")  # Anchor to bottom
        
        # Reset game button
        reset_btn = tk.Button(
            bottom_frame,
            text="🔄 Reset Game",
            font=("Arial", 12),
            bg=self.colors["accent"],  # Highlight color
            fg="white",
            command=self.reset_game
        )
        reset_btn.pack(pady=20)
        
    def play_round(self, player_choice):
        """Execute a game round with the player's selected choice"""
        self.round += 1  # Increment round counter
        computer_choice = random.choice(["rock", "paper", "scissors"])  # Random computer choice
        
        # Update the display with both choices
        self.update_choice_displays(player_choice, computer_choice)
        
        # Determine the winner and get result
        result = self.determine_winner(player_choice, computer_choice)
        
        # Update the scoreboard based on result
        self.update_scoreboard(result)
        
        # Calculate and update progress bars
        total = max(1, self.player_score + self.computer_score)  # Prevent division by zero
        player_percent = (self.player_score / total) * 100
        computer_percent = (self.computer_score / total) * 100
        self.player_progress["value"] = player_percent
        self.computer_progress["value"] = computer_percent
        
    def update_choice_displays(self, player_choice, computer_choice):
        """Update the choice displays with color-coded selections"""
        # Emoji mapping for each choice
        emoji_map = {
            "rock": "🪨",
            "paper": "📄",
            "scissors": "✂️"
        }
        
        # Color mapping for each choice
        color_map = {
            "rock": self.colors["rock"],
            "paper": self.colors["paper"],
            "scissors": self.colors["scissors"]
        }
        
        # Update player display with colored background and emoji
        self.player_display.config(
            text=f" YOU: {emoji_map[player_choice]} {player_choice.upper()} ",
            fg="white",  # White text for better contrast
            bg=color_map[player_choice]  # Color based on choice
        )
        
        # Update computer display similarly
        self.computer_display.config(
            text=f" COMP: {emoji_map[computer_choice]} {computer_choice.upper()} ",
            fg="white",
            bg=color_map[computer_choice]
        )
        
    def determine_winner(self, player, computer):
        """Determine the winner of a round based on game rules"""
        if player == computer:
            # Tie condition
            self.result_display.config(text="😐 It's a Tie! 😐", fg="orange")
            return "tie"
        elif ((player == "rock" and computer == "scissors") or
              (player == "paper" and computer == "rock") or
              (player == "scissors" and computer == "paper")):
            # Player win conditions
            self.result_display.config(text="🎉 You Win! 🎉", fg="green")
            return "player"
        else:
            # Computer win conditions
            self.result_display.config(text="😢 Computer Wins! 😢", fg="red")
            return "computer"
        
    def update_scoreboard(self, result):
        """Update the score based on the round result"""
        if result == "player":
            self.player_score += 1
            self.player_score_label.config(text=str(self.player_score))
        elif result == "computer":
            self.computer_score += 1
            self.computer_score_label.config(text=str(self.computer_score))
        # Note: Ties don't affect the score
        
    def reset_game(self):
        """Reset all game state and UI to initial conditions"""
        # Reset scores
        self.player_score = 0
        self.computer_score = 0
        self.round = 0
        
        # Update score displays
        self.player_score_label.config(text="0")
        self.computer_score_label.config(text="0")
        
        # Reset choice displays
        self.player_display.config(
            text=" Your choice ",
            fg="black",
            bg=self.colors["player_bg"]
        )
        self.computer_display.config(
            text=" Computer's choice ",
            fg="black",
            bg=self.colors["computer_bg"]
        )
        
        # Clear result message
        self.result_display.config(text="")
        
        # Reset progress bars
        self.player_progress["value"] = 0
        self.computer_progress["value"] = 0

def main():
    """Entry point for the application"""
    root = tk.Tk()  # Create main window
    game = RockPaperScissorsGame(root)  # Initialize game
    root.mainloop()  # Start the GUI event loop

if __name__ == "__main__":
    main()