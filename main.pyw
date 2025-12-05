import customtkinter as ctk
import requests
import json
from datetime import date
from tkinter import filedialog
import re

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class StoryGenerator:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Story Generator")
        self.root.geometry("800x700")
        self.root.minsize(800, 700)

        self.genres = ["Horror", "Thriller", "Mystery", "Detective/Noir", "Fantasy", "Science Fiction",
                       "Romance", "Historical Fiction", "Western", "Adventure", "Comedy", "Drama",
                       "Fables", "Nursery Rhymes", "Fairy Tales", "Mythology", "Folklore", 
                       "Satire", "Gothic", "Dystopian", "Utopian", "Steampunk", "Cyberpunk",
                       "Urban Fantasy", "Dark Fantasy", "Epic Fantasy", "Paranormal", "Supernatural",
                       "Crime", "Suspense", "Action", "War", "Espionage", "Literary Fiction", "Vampires","Historical","Medieval","Pirates","Space Opera","Time Travel","Post-Apocalyptic","Magical Realism"]

        # Main container
        main = ctk.CTkFrame(self.root)
        main.pack(fill="both", expand=True, padx=30, pady=30)

        # Title
        ctk.CTkLabel(main, text="Story Generator", font=ctk.CTkFont(size=36, weight="bold")).pack(pady=(0, 40))

        # Genre
        ctk.CTkLabel(main, text="Select Genre", font=ctk.CTkFont(size=14)).pack(anchor="w", padx=100)
        self.genre_var = ctk.StringVar(value=self.genres[0])
        ctk.CTkComboBox(main, values=self.genres, variable=self.genre_var, width=350, height=35,
                        font=ctk.CTkFont(size=12)).pack(pady=(8, 20))

        # Word count
        ctk.CTkLabel(main, text="Word Count", font=ctk.CTkFont(size=14)).pack(anchor="w", padx=100)
        self.slider_var = ctk.DoubleVar(value=500)
        slider = ctk.CTkSlider(main, from_=100, to=1500, number_of_steps=140, variable=self.slider_var, width=450)
        slider.pack(pady=(10, 15))
        self.word_label = ctk.CTkLabel(main, text="500 words", font=ctk.CTkFont(size=16, weight="bold"))
        self.word_label.pack(pady=(0, 20))
        slider.configure(command=lambda v: self.word_label.configure(text=f"{int(float(v))} words"))

        # Buttons
        btn_frame = ctk.CTkFrame(main, fg_color="transparent")
        btn_frame.pack(pady=15)
        ctk.CTkButton(btn_frame, text="Generate Story", command=self.generate_story,
                      fg_color="#EF233C", hover_color="#D90429", width=200, height=45,
                      font=ctk.CTkFont(size=14, weight="bold")).pack(side="left", padx=30)
        self.save_btn = ctk.CTkButton(btn_frame, text="Save as Markdown", command=self.save_as_markdown,
                                      fg_color="#2D936C", hover_color="#34B679", width=200, height=45,
                                      font=ctk.CTkFont(size=14, weight="bold"), state="disabled")
        self.save_btn.pack(side="left", padx=30)

        # Story display
        self.story_text = ctk.CTkTextbox(main, wrap="word", font=ctk.CTkFont(size=14), padx=20, pady=20)
        self.story_text.pack(fill="both", expand=True, padx=60, pady=(10, 20))

        # Tag configs removed as customtkinter forbids font option in tag_config

    def generate_story(self):
        genre = self.genre_var.get()
        words = int(self.slider_var.get())

        prompt = (f"Write a complete {genre.lower()} story that is up to {words} words long (count carefully). "
                  "CRITICAL: The story MUST have a proper ending - do not stop mid-sentence or mid-thought. "
                  "Format with multiple paragraphs separated by blank lines (double newlines). "
                  "Start new paragraphs at natural breaks: scene changes, dialogue, shifts in time/location. "
                  "Use **bold** for strong emphasis and *italics* for thoughts or sounds. "
                  "Strong plot, vivid characters, satisfying twist ending. Add a fitting title.")

        self.story_text.delete("1.0", "end")
        self.story_text.insert("1.0", "Generating your story...")
        self.root.update()

        try:
            with open("api_key.json", "r") as f:
                data = json.load(f)
                api_key = data["api_key"]
            
            # Use Groq's free API (llama-3.3-70b-versatile model)
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                json={
                    "model": "llama-3.3-70b-versatile",
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": words * 5,
                    "temperature": 0.7
                },
                headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
                timeout=60
            )
            response.raise_for_status()
            raw = response.json()["choices"][0]["message"]["content"].strip()
            story = raw  # Use the complete story as generated by the LLM

            self.story_text.delete("1.0", "end")
            self.display_formatted(story)

            self.current_story = story
            self.current_genre = genre
            self.current_words = words
            self.save_btn.configure(state="normal")

        except Exception as e:
            self.story_text.delete("1.0", "end")
            self.story_text.insert("1.0", f"Failed to generate:\n\n{str(e)}")

    def display_formatted(self, text):
        # Split by double newlines (paragraph breaks)
        paragraphs = text.split('\n\n')
        
        for i, paragraph in enumerate(paragraphs):
            paragraph = paragraph.strip()
            if not paragraph:
                continue
                
            # Split paragraph by markdown formatting
            parts = re.split(r'(\*\*.*?\*\*|\*.*?\*)', paragraph)
            for part in parts:
                if part.startswith("**") and part.endswith("**"):
                    self.story_text.insert("end", part[2:-2], "bold")
                elif part.startswith("*") and part.endswith("*") and not part.startswith("**"):
                    self.story_text.insert("end", part[1:-1], "italic")
                else:
                    self.story_text.insert("end", part)
            
            # Add double newline after paragraph for spacing
            if i < len(paragraphs) - 1:
                self.story_text.insert("end", "\n\n")

    def save_as_markdown(self):
        today = date.today().strftime("%Y-%m-%d")
        filename = f"{self.current_genre}_{self.current_words}w_{today}.md"

        path = filedialog.asksaveasfilename(
            initialfile=filename,
            defaultextension=".md",
            filetypes=[("Markdown", "*.md"), ("Text", "*.txt")],
            title="Save Story as Markdown"
        )
        if not path:
            return

        title = f"# {self.current_genre} Story\n\n**{self.current_words} words**\n\n---\n\n"
        content = title + self.current_story

        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            self.save_btn.configure(text="Saved!")
            self.root.after(2000, lambda: self.save_btn.configure(text="Save as Markdown"))
        except Exception as e:
            self.story_text.insert("end", f"\n\nSave failed: {e}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = StoryGenerator()
    app.run()