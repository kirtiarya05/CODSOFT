import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors - Tournament Pro")
        self.root.geometry("500x780")
        self.root.resizable(False, False)
        
        # Modern Dark Theme Colors
        self.bg_color = "#0F172A"      # Deep Navy
        self.card_bg = "#1E293B"       # Lighter Navy
        self.accent_color = "#9333EA"  # Purple
        self.user_color = "#3B82F6"    # Blue
        self.comp_color = "#F43F5E"    # Rose/Red
        self.text_color = "#FFFFFF"
        self.text_dim = "#94A3B8"
        self.success_color = "#10B981" # Green
        self.warning_color = "#F59E0B" # Amber
        
        self.root.configure(bg=self.bg_color)
        
        # Game State
        self.user_score = 0
        self.comp_score = 0
        self.streak = 0
        self.history = []
        self.is_playing = False
        
        self._setup_ui()

    def _setup_ui(self):
        # Title Header
        header_frame = tk.Frame(self.root, bg=self.bg_color, pady=25)
        header_frame.pack(fill="x")
        
        tk.Label(
            header_frame, text="TOURNAMENT PRO", 
            bg=self.bg_color, fg=self.accent_color,
            font=("Outfit", 24, "bold")
        ).pack()
        
        tk.Label(
            header_frame, text="Beat the AI 10 times to become Legend!", 
            bg=self.bg_color, fg=self.text_dim,
            font=("Outfit", 10)
        ).pack()

        # Score Board + Streak
        status_frame = tk.Frame(self.root, bg=self.card_bg, padx=20, pady=15)
        status_frame.pack(fill="x", padx=40, pady=10)
        
        self.user_score_label = tk.Label(
            status_frame, text=f"YOU: {self.user_score}", 
            bg=self.card_bg, fg=self.user_color, font=("Outfit", 16, "bold")
        )
        self.user_score_label.grid(row=0, column=0, sticky="w")
        
        tk.Label(status_frame, text="VS", bg=self.card_bg, fg=self.text_dim, font=("Outfit", 12, "bold")).grid(row=0, column=1)
        
        self.comp_score_label = tk.Label(
            status_frame, text=f"CPU: {self.comp_score}", 
            bg=self.card_bg, fg=self.comp_color, font=("Outfit", 16, "bold")
        )
        self.comp_score_label.grid(row=0, column=2, sticky="e")
        
        status_frame.grid_columnconfigure(1, weight=1)

        # Streak Indicator
        self.streak_label = tk.Label(
            self.root, text="⚡ Win Streak: 0", 
            bg=self.bg_color, fg=self.warning_color, font=("Outfit", 11, "bold")
        )
        self.streak_label.pack(pady=5)

        # Battle Arena
        battle_frame = tk.Frame(self.root, bg=self.bg_color, pady=30)
        battle_frame.pack(fill="x")

        self.user_choice_label = tk.Label(
            battle_frame, text="?", bg=self.bg_color, fg=self.user_color, font=("Outfit", 60)
        )
        self.user_choice_label.pack(side="left", expand=True)

        self.vs_anim_label = tk.Label(
            battle_frame, text="VS", bg=self.bg_color, fg=self.text_dim, font=("Outfit", 20, "italic")
        )
        self.vs_anim_label.pack(side="left")

        self.comp_choice_label = tk.Label(
            battle_frame, text="?", bg=self.bg_color, fg=self.comp_color, font=("Outfit", 60)
        )
        self.comp_choice_label.pack(side="left", expand=True)

        # Result Banner
        self.result_var = tk.StringVar(value="Choose your weapon!")
        self.result_label = tk.Label(
            self.root, textvariable=self.result_var, 
            bg=self.bg_color, fg=self.text_color, font=("Outfit", 18, "bold")
        )
        self.result_label.pack(pady=10)

        # Action Buttons
        btn_container = tk.Frame(self.root, bg=self.bg_color, pady=20)
        btn_container.pack(fill="x", padx=50)

        choices = [
            ("🪨 ROCK", "rock", self.user_color),
            ("📄 PAPER", "paper", self.accent_color),
            ("✂️ SCISSORS", "scissors", self.warning_color)
        ]

        for text, choice, color in choices:
            btn = tk.Button(
                btn_container, text=text, bg=color, fg=self.text_color,
                font=("Outfit", 12, "bold"), borderwidth=0, cursor="hand2",
                activebackground=color, activeforeground=self.text_color,
                padx=20, pady=12, command=lambda c=choice: self._handle_click(c)
            )
            btn.pack(fill="x", pady=4)

        # History Tracker
        history_title = tk.Label(self.root, text="RECENT LOGS", bg=self.bg_color, fg=self.text_dim, font=("Outfit", 8, "bold"))
        history_title.pack(pady=(20, 5))
        
        self.history_frame = tk.Frame(self.root, bg=self.bg_color)
        self.history_frame.pack(fill="x", padx=60)
        
        self.history_labels = []
        for _ in range(5):
            lbl = tk.Label(self.history_frame, text="", bg=self.bg_color, fg=self.text_dim, font=("Outfit", 9))
            lbl.pack()
            self.history_labels.append(lbl)

        # Reset Button (Corrected bg)
        tk.Button(
            self.root, text="RESET DATA", bg=self.bg_color, fg=self.text_dim,
            font=("Outfit", 9, "underline"), borderwidth=0, cursor="hand2",
            activebackground=self.bg_color, activeforeground=self.text_color,
            command=self._reset, highlightthickness=0
        ).pack(side="bottom", pady=15)

    def _handle_click(self, user_choice):
        if self.is_playing: return
        self.is_playing = True
        
        # Visual thinking effect
        self.result_var.set("AI is scanning pattern...")
        self.result_label.config(fg=self.text_dim)
        self.comp_choice_label.config(text="🎲")
        
        self.root.after(600, lambda: self._play(user_choice))

    def _play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        comp_choice = random.choice(choices)
        
        icons = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
        self.user_choice_label.config(text=icons[user_choice])
        self.comp_choice_label.config(text=icons[comp_choice])
        
        win_txt = ""
        if user_choice == comp_choice:
            result = "STANDOFF! (TIE)"
            color = self.text_dim
            self.streak = 0
            win_txt = "Tie"
        elif (user_choice == "rock" and comp_choice == "scissors") or \
             (user_choice == "paper" and comp_choice == "rock") or \
             (user_choice == "scissors" and comp_choice == "paper"):
            result = "DOMINATED! (+1)"
            color = self.success_color
            self.user_score += 1
            self.streak += 1
            win_txt = "Win"
        else:
            result = "OUTSMARTED! (-1)"
            color = self.comp_color
            self.comp_score += 1
            self.streak = 0
            win_txt = "Loss"
            
        # Update History
        log_entry = f"You {icons[user_choice]} vs AI {icons[comp_choice]} -> {win_txt}"
        self.history.insert(0, log_entry)
        self.history = self.history[:5]
        self._update_history_ui()
        
        # Update UI score labels
        self.result_var.set(result)
        self.result_label.config(fg=color)
        self.user_score_label.config(text=f"YOU: {self.user_score}")
        self.comp_score_label.config(text=f"CPU: {self.comp_score}")
        
        # Update Streak Label (Corrected f-string usage for compatibility)
        streak_icon = "🔥" if self.streak > 2 else "⚡"
        self.streak_label.config(text=f"{streak_icon} Win Streak: {self.streak}")
        
        self.is_playing = False
        
        # Check Win Condition
        if self.user_score >= 10:
            messagebox.showinfo("LEGENDARY STATUS", f"You crushed the AI {self.user_score}-{self.comp_score}!")
            self._reset()
        elif self.comp_score >= 10:
            messagebox.showinfo("DEFEAT", f"The machine has learned your ways. Final score: {self.user_score}-{self.comp_score}")
            self._reset()

    def _update_history_ui(self):
        for i, text in enumerate(self.history):
            if i < len(self.history_labels):
                self.history_labels[i].config(text=text)

    def _reset(self):
        self.user_score = 0
        self.comp_score = 0
        self.streak = 0
        self.history = []
        self.user_score_label.config(text="YOU: 0")
        self.comp_score_label.config(text="CPU: 0")
        self.streak_label.config(text="⚡ Win Streak: 0")
        self.user_choice_label.config(text="?")
        self.comp_choice_label.config(text="?")
        self.result_var.set("New Tournament Started")
        self.result_label.config(fg=self.text_color)
        for lbl in self.history_labels: lbl.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
