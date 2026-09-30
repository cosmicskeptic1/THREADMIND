
import tkinter as tk
from tkinter import messagebox

from wardrobe import Wardrobe
from outfit_engine import OutfitEngine
from history import OutfitHistory
from scoring import explain_outfit


class ThreadMindApp:

    def __init__(self, root):
        self.root = root

        self.root.title("THREADMIND | Intelligent Wardrobe")
        self.root.geometry("1000x800")
        self.root.minsize(800, 600)
        self.root.configure(bg="#111111")

        self.wardrobe = Wardrobe()
        self.history = OutfitHistory()
        self.engine = OutfitEngine(self.wardrobe)

        self.occasion_var = tk.StringVar(value="College")
        self.season_var = tk.StringVar(value="Summer")

        self.create_header()
        self.create_preferences()
        self.create_outfit_area()
        self.create_buttons()

    # ---------------------------------------------------------
    # HEADER
    # ---------------------------------------------------------

    def create_header(self):

        header = tk.Frame(
            self.root,
            bg="#111111",
            padx=30,
            pady=25
        )

        header.pack(fill="x")

        title = tk.Label(
            header,
            text="THREADMIND",
            font=("Segoe UI", 30, "bold"),
            fg="#ffffff",
            bg="#111111"
        )

        title.pack()

        subtitle = tk.Label(
            header,
            text="INTELLIGENT WARDROBE DECISION ENGINE",
            font=("Segoe UI", 11),
            fg="#aaaaaa",
            bg="#111111"
        )

        subtitle.pack(pady=(4, 0))

    # ---------------------------------------------------------
    # PREFERENCES
    # ---------------------------------------------------------

    def create_preferences(self):

        preferences = tk.Frame(
            self.root,
            bg="#1b1b1b",
            padx=25,
            pady=18
        )

        preferences.pack(
            fill="x",
            padx=30,
            pady=(0, 20)
        )

        # OCCASION

        occasion_label = tk.Label(
            preferences,
            text="OCCASION",
            font=("Segoe UI", 10, "bold"),
            fg="#cccccc",
            bg="#1b1b1b"
        )

        occasion_label.grid(
            row=0,
            column=0,
            padx=(0, 10),
            sticky="w"
        )

        occasion_menu = tk.OptionMenu(
            preferences,
            self.occasion_var,
            "College",
            "Casual",
            "Formal"
        )

        occasion_menu.config(
            font=("Segoe UI", 11),
            bg="#292929",
            fg="#ffffff",
            activebackground="#333333",
            activeforeground="#ffffff",
            highlightthickness=0,
            width=12
        )

        occasion_menu["menu"].config(
            bg="#292929",
            fg="#ffffff",
            activebackground="#444444",
            activeforeground="#ffffff"
        )

        occasion_menu.grid(
            row=0,
            column=1,
            padx=(0, 30)
        )

        # SEASON

        season_label = tk.Label(
            preferences,
            text="SEASON",
            font=("Segoe UI", 10, "bold"),
            fg="#cccccc",
            bg="#1b1b1b"
        )

        season_label.grid(
            row=0,
            column=2,
            padx=(0, 10),
            sticky="w"
        )

        season_menu = tk.OptionMenu(
            preferences,
            self.season_var,
            "Summer",
            "Winter",
            "Spring",
            "Autumn"
        )

        season_menu.config(
            font=("Segoe UI", 11),
            bg="#292929",
            fg="#ffffff",
            activebackground="#333333",
            activeforeground="#ffffff",
            highlightthickness=0,
            width=12
        )

        season_menu["menu"].config(
            bg="#292929",
            fg="#ffffff",
            activebackground="#444444",
            activeforeground="#ffffff"
        )

        season_menu.grid(
            row=0,
            column=3
        )

    # ---------------------------------------------------------
    # OUTFIT AREA
    # ---------------------------------------------------------

    def create_outfit_area(self):

        self.outfit_frame = tk.Frame(
            self.root,
            bg="#181818",
            padx=30,
            pady=25
        )

        self.outfit_frame.pack(
            fill="both",
            expand=True,
            padx=30
        )

        self.status_label = tk.Label(
            self.outfit_frame,
            text="Ready to generate your outfit.",
            font=("Segoe UI", 13),
            fg="#bbbbbb",
            bg="#181818"
        )

        self.status_label.pack(
            pady=(5, 15)
        )

        self.outfit_title = tk.Label(
            self.outfit_frame,
            text="YOUR OUTFIT",
            font=("Segoe UI", 18, "bold"),
            fg="#ffffff",
            bg="#181818"
        )

        self.outfit_title.pack()

        # TOP

        self.top_label = tk.Label(
            self.outfit_frame,
            text="TOP\n—",
            font=("Segoe UI", 14),
            fg="#dddddd",
            bg="#181818",
            justify="center"
        )

        self.top_label.pack(
            pady=(15, 5)
        )

        # BOTTOM

        self.bottom_label = tk.Label(
            self.outfit_frame,
            text="BOTTOM\n—",
            font=("Segoe UI", 14),
            fg="#dddddd",
            bg="#181818",
            justify="center"
        )

        self.bottom_label.pack(
            pady=5
        )

        # SHOES

        self.shoes_label = tk.Label(
            self.outfit_frame,
            text="SHOES\n—",
            font=("Segoe UI", 14),
            fg="#dddddd",
            bg="#181818",
            justify="center"
        )

        self.shoes_label.pack(
            pady=5
        )

        # SCORE

        self.score_label = tk.Label(
            self.outfit_frame,
            text="Compatibility Score: —",
            font=("Segoe UI", 12, "bold"),
            fg="#ffffff",
            bg="#181818"
        )

        self.score_label.pack(
            pady=(12, 5)
        )

        # WHY THIS OUTFIT

        self.reason_title = tk.Label(
            self.outfit_frame,
            text="WHY THIS OUTFIT?",
            font=("Segoe UI", 13, "bold"),
            fg="#ffffff",
            bg="#181818"
        )

        self.reason_title.pack(
            pady=(12, 5)
        )

        self.reason_label = tk.Label(
            self.outfit_frame,
            text="Generate an outfit to see the reasoning.",
            font=("Segoe UI", 10),
            fg="#aaaaaa",
            bg="#181818",
            justify="left",
            wraplength=700
        )

        self.reason_label.pack()

    # ---------------------------------------------------------
    # BUTTON
    # ---------------------------------------------------------

    def create_buttons(self):

        button_frame = tk.Frame(
            self.root,
            bg="#111111",
            pady=18
        )

        button_frame.pack(
            fill="x"
        )

        generate_button = tk.Button(
            button_frame,
            text="GENERATE OUTFIT",
            command=self.generate_outfit,
            font=("Segoe UI", 12, "bold"),
            bg="#ffffff",
            fg="#111111",
            activebackground="#dddddd",
            activeforeground="#111111",
            relief="flat",
            padx=25,
            pady=12,
            cursor="hand2"
        )

        generate_button.pack()
        self.root.update_idletasks()

    # ---------------------------------------------------------
    # GENERATE OUTFIT
    # ---------------------------------------------------------

    def generate_outfit(self):

        occasion = self.occasion_var.get()
        season = self.season_var.get()

        # Give the engine the user's preferences

        self.engine.set_preferences(
            occasion,
            season
        )

        # Generate all possible combinations

        outfits = self.engine.get_best_outfits(18)

        # Handle an empty wardrobe or preferences with no valid combinations.

        if not outfits:

            self.status_label.config(
                text="No compatible outfits are available."
            )

            messagebox.showinfo(
                "THREADMIND",
                "No compatible outfits are available for these preferences."
            )

            return

        # Remove outfits already worn

        unworn_outfits = [
            outfit
            for outfit in outfits
            if not self.history.was_worn(outfit)
        ]

        # If every combination has already been worn

        if not unworn_outfits:

            messagebox.showinfo(
                "THREADMIND",
                "You have already worn every available combination.\n\n"
                "Your wardrobe needs some new combinations!"
            )

            return

        # Select the highest-scoring unworn outfit

        outfit = unworn_outfits[0]

        # Save it to history

        self.history.add_outfit(outfit)

        # Display TOP

        self.top_label.config(
            text=f"TOP\n{outfit['top']['name']}"
        )

        # Display BOTTOM

        self.bottom_label.config(
            text=f"BOTTOM\n{outfit['bottom']['name']}"
        )

        # Display SHOES

        self.shoes_label.config(
            text=f"SHOES\n{outfit['shoes']['name']}"
        )

        # Display SCORE

        self.score_label.config(
            text=f"Compatibility Score: {outfit['score']}"
        )

        # Generate explanation

        reasons = explain_outfit(
            outfit["top"],
            outfit["bottom"],
            outfit["shoes"],
            occasion,
            season
        )

        explanation = "\n".join(
            "• " + reason
            for reason in reasons
        )

        self.reason_label.config(
            text=explanation
        )

        # Update status

        self.status_label.config(
            text=f"Generated for {occasion} • {season}"
        )


# -------------------------------------------------------------
# APPLICATION ENTRY POINT
# -------------------------------------------------------------

def run_app():

    root = tk.Tk()

    app = ThreadMindApp(root)

    root.mainloop()
