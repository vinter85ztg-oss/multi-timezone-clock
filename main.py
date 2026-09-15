#!/usr/bin/env python3
"""
Digital Clock Application - Displays time in multiple time zones
"""

import tkinter as tk
from tkinter import font, messagebox, ttk
from datetime import datetime
import pytz
from timezone_clock import TimeZoneClock
import threading
import time

class ClockGUI:
    """
    Graficzny interfejs użytkownika dla zegara wielostrefowego
    """
    
    def __init__(self, root):
        """
        Inicjalizacja GUI
        
        Args:
            root: główne okno Tkinter
        """
        self.root = root
        self.root.title("🌍 Multi-Timezone Digital Clock")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Kolory
        self.bg_color = "#1a1a1a"
        self.fg_color = "#00ff00"
        self.accent_color = "#00cc00"
        self.root.configure(bg=self.bg_color)
        
        # Zegar
        self.clock = TimeZoneClock()
        self.running = True
        self.selected_cities = list(self.clock.get_available_timezones())
        
        # Tworzenie UI
        self.create_widgets()
        
        # Uruchamianie aktualizacji
        self.update_clock()
        
        # Obsługa zamknięcia okna
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def create_widgets(self):
        """
        Tworzenie wszystkich elementów UI
        """
        # Nagłówek
        header_frame = tk.Frame(self.root, bg=self.bg_color)
        header_frame.pack(pady=10)
        
        title_label = tk.Label(
            header_frame,
            text="🌍 MULTI-TIMEZONE CLOCK",
            font=("Arial", 24, "bold"),
            fg=self.fg_color,
            bg=self.bg_color
        )
        title_label.pack()
        
        # Panel sterowania
        control_frame = tk.Frame(self.root, bg="#2a2a2a", relief=tk.RAISED, bd=2)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Przycisk odświeżania
        refresh_btn = tk.Button(
            control_frame,
            text="🔄 Refresh",
            command=self.refresh_clock,
            bg=self.accent_color,
            fg="#000",
            font=("Arial", 10, "bold"),
            padx=10
        )
        refresh_btn.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Przycisk dodawania strefy
        add_btn = tk.Button(
            control_frame,
            text="➕ Add Timezone",
            command=self.add_timezone_window,
            bg="#0099cc",
            fg="#fff",
            font=("Arial", 10, "bold"),
            padx=10
        )
        add_btn.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Przycisk porównania
        compare_btn = tk.Button(
            control_frame,
            text="⏱️ Compare",
            command=self.compare_timezones,
            bg="#cc6600",
            fg="#fff",
            font=("Arial", 10, "bold"),
            padx=10
        )
        compare_btn.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Główna ramka dla zegarów
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Canvas ze scrollingiem
        canvas = tk.Canvas(
            main_frame,
            bg=self.bg_color,
            highlightthickness=0
        )
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        
        self.scrollable_frame = tk.Frame(canvas, bg=self.bg_color)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Przechowywanie etykiet do aktualizacji
        self.time_labels = {}
        self.create_clock_widgets()
        
        # Stopka
        footer_frame = tk.Frame(self.root, bg="#2a2a2a", relief=tk.RAISED, bd=2)
        footer_frame.pack(fill=tk.X, padx=10, pady=5)
        
        footer_label = tk.Label(
            footer_frame,
            text="⏰ Updating every second | Click to remove a timezone",
            font=("Arial", 9),
            fg="#888",
            bg="#2a2a2a"
        )
        footer_label.pack(pady=5)
    
    def create_clock_widgets(self):
        """
        Tworzenie widżetów zegarów dla każdej strefy
        """
        # Czyszczenie poprzednich widżetów
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.time_labels = {}
        
        # Tworzenie zegarów
        for i, city in enumerate(self.selected_cities):
            # Ramka dla miasta
            city_frame = tk.Frame(
                self.scrollable_frame,
                bg="#2a2a2a",
                relief=tk.RIDGE,
                bd=2
            )
            city_frame.pack(fill=tk.X, padx=5, pady=5)
            
            # Nazwa miasta
            city_label = tk.Label(
                city_frame,
                text=city,
                font=("Arial", 14, "bold"),
                fg=self.accent_color,
                bg="#2a2a2a"
            )
            city_label.pack(side=tk.LEFT, padx=10, pady=8)
            
            # Separator
            separator = tk.Frame(city_frame, bg="#444", height=1)
            separator.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=8)
            
            # Godzina
            time_label = tk.Label(
                city_frame,
                text="00:00:00",
                font=("Courier", 24, "bold"),
                fg=self.fg_color,
                bg="#2a2a2a"
            )
            time_label.pack(side=tk.LEFT, padx=10, pady=8)
            
            # Offset
            offset_label = tk.Label(
                city_frame,
                text="+00:00",
                font=("Arial", 10),
                fg="#888",
                bg="#2a2a2a"
            )
            offset_label.pack(side=tk.LEFT, padx=5, pady=8)
            
            # Przycisk usuwania
            remove_btn = tk.Button(
                city_frame,
                text="✕",
                command=lambda c=city: self.remove_timezone(c),
                bg="#cc3333",
                fg="#fff",
                font=("Arial", 12, "bold"),
                width=2,
                relief=tk.FLAT
            )
            remove_btn.pack(side=tk.RIGHT, padx=10, pady=5)
            
            self.time_labels[city] = (time_label, offset_label)
    
    def update_clock(self):
        """
        Aktualizuje wyświetlany czas
        """
        if self.running:
            # Pobieranie czasów
            times = self.clock.get_all_times()
            
            # Aktualizacja etykiet
            for city, (time_label, offset_label) in self.time_labels.items():
                if city in times:
                    time_label.config(text=times[city])
                    offset = self.clock.get_timezone_offset(city)
                    offset_label.config(text=offset)
            
            # Kolejna aktualizacja za 1 sekundę
            self.root.after(1000, self.update_clock)
    
    def refresh_clock(self):
        """
        Ręczne odświeżenie zegara
        """
        self.create_clock_widgets()
        self.update_clock()
    
    def remove_timezone(self, city):
        """
        Usuwa strefę czasową z listy
        
        Args:
            city: nazwa miasta do usunięcia
        """
        if city in self.selected_cities:
            self.selected_cities.remove(city)
            self.create_clock_widgets()
            self.update_clock()
    
    def add_timezone_window(self):
        """
        Otwiera okno do dodania nowej strefy czasowej
        """
        # Pobieranie listy dostępnych stref
        available_tz = []
        for tz in pytz.all_timezones:
            available_tz.append(tz)
        
        # Nowe okno
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Timezone")
        add_window.geometry("400x300")
        add_window.configure(bg=self.bg_color)
        
        # Etykieta
        label = tk.Label(
            add_window,
            text="Select timezone:",
            font=("Arial", 12),
            fg=self.fg_color,
            bg=self.bg_color
        )
        label.pack(pady=10)
        
        # Combobox
        tz_var = tk.StringVar()
        tz_combo = ttk.Combobox(
            add_window,
            textvariable=tz_var,
            values=available_tz,
            width=40,
            state="readonly"
        )
        tz_combo.pack(pady=10, padx=10)
        
        # Etykieta dla nazwy miasta
        name_label = tk.Label(
            add_window,
            text="City name (optional):",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color
        )
        name_label.pack(pady=5)
        
        # Pole tekstowe
        name_entry = tk.Entry(
            add_window,
            font=("Arial", 10),
            width=40
        )
        name_entry.pack(pady=5, padx=10)
        
        def add_tz():
            tz = tz_var.get()
            name = name_entry.get() or tz.split('/')[-1]
            
            if tz:
                self.selected_cities.append(name)
                self.clock.add_custom_timezone(name, tz)
                self.create_clock_widgets()
                self.update_clock()
                add_window.destroy()
                messagebox.showinfo("Success", f"Added {name}!")
            else:
                messagebox.showerror("Error", "Please select a timezone")
        
        # Przycisk potwierdzenia
        add_btn = tk.Button(
            add_window,
            text="✓ Add",
            command=add_tz,
            bg=self.accent_color,
            fg="#000",
            font=("Arial", 12, "bold"),
            padx=20
        )
        add_btn.pack(pady=20)
    
    def compare_timezones(self):
        """
        Porównuje czasy między wybranymi strefami
        """
        if len(self.selected_cities) < 2:
            messagebox.showwarning("Warning", "Select at least 2 timezones to compare")
            return
        
        # Nowe okno
        compare_window = tk.Toplevel(self.root)
        compare_window.title("Compare Timezones")
        compare_window.geometry("500x400")
        compare_window.configure(bg=self.bg_color)
        
        # Pobieranie pełnych czasów
        times = self.clock.get_all_times_full()
        
        # Wyświetlanie czasów
        text_widget = tk.Text(
            compare_window,
            font=("Courier", 11),
            bg="#2a2a2a",
            fg=self.fg_color,
            height=20,
            width=50
        )
        text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        content = "📊 TIMEZONE COMPARISON\n\n"
        for city in self.selected_cities:
            if city in times:
                offset = self.clock.get_timezone_offset(city)
                content += f"{city:20} | {times[city]} | {offset}\n"
        
        text_widget.insert(1.0, content)
        text_widget.config(state=tk.DISABLED)
    
    def on_close(self):
        """
        Obsługa zamknięcia okna
        """
        self.running = False
        self.root.destroy()

def main():
    """
    Główna funkcja aplikacji
    """
    root = tk.Tk()
    app = ClockGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
