# 🌍 Multi-Timezone Digital Clock

A modern, feature-rich digital clock application that displays the current time in multiple time zones simultaneously.

## ✨ Features

- 🕐 **Real-time display** - Updates every second
- 🌍 **15 pre-loaded timezones** - UTC, London, Paris, Tokyo, Sydney, New York, Los Angeles, Dubai, Singapore, Mumbai, Bangkok, Hong Kong, São Paulo, Moscow, Cairo
- ➕ **Add custom timezones** - Choose from all 400+ available timezones
- ✕ **Remove timezones** - Click the X button to remove any timezone
- ⏱️ **Compare timezones** - View all times side-by-side with their offsets
- 🔄 **Auto-refresh** - Continuous updates with manual refresh option
- 🎨 **Modern GUI** - Dark theme with green terminal-style display

## 🛠️ Requirements

- Python 3.7+
- tkinter (usually comes with Python)
- pytz
- Pillow

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/vinter85ztg-oss/multi-timezone-clock.git
cd multi-timezone-clock
```

### 2. Create virtual environment (optional but recommended)
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Run the application
```bash
python main.py
```

The clock window will open and display current time for all configured timezones.

## 📖 How to Use

### Main Features

1. **View Times** - The main window shows all timezones with:
   - City name
   - Current time (HH:MM:SS)
   - UTC offset

2. **Add Timezone**
   - Click the "➕ Add Timezone" button
   - Select from the dropdown list
   - Optionally enter a custom city name
   - Click "Add"

3. **Remove Timezone**
   - Click the "✕" button next to any timezone
   - It will be removed from the display

4. **Refresh**
   - Click "🔄 Refresh" to manually update the display
   - Times update automatically every second

5. **Compare Timezones**
   - Click "⏱️ Compare" button
   - View all times with their offsets in a comparison window

## 📁 Project Structure

```
multi-timezone-clock/
├── main.py                  # Main GUI application
├── timezone_clock.py        # Core clock logic
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── .gitignore             # Git ignore rules
```

## 🔧 Code Structure

### `timezone_clock.py`
- `TimeZoneClock` class:
  - `get_time_in_timezone()` - Get time for a specific timezone
  - `get_all_times()` - Get times for all configured timezones
  - `get_timezone_offset()` - Get UTC offset for a timezone
  - `add_custom_timezone()` - Add a new timezone
  - `remove_timezone()` - Remove a timezone
  - `get_time_difference()` - Calculate time difference between two zones

### `main.py`
- `ClockGUI` class:
  - `create_widgets()` - Build the GUI
  - `update_clock()` - Update time display
  - `add_timezone_window()` - Dialog for adding timezone
  - `compare_timezones()` - Show comparison window
  - `remove_timezone()` - Remove timezone from display

## 🎨 Customization

You can customize the appearance by modifying the colors in `main.py`:

```python
self.bg_color = "#1a1a1a"      # Background color
self.fg_color = "#00ff00"       # Foreground/text color
self.accent_color = "#00cc00"   # Accent color for buttons
```

## 📊 Pre-loaded Timezones

1. UTC - Coordinated Universal Time
2. London - Europe/London
3. Paris - Europe/Paris
4. Tokyo - Asia/Tokyo
5. Sydney - Australia/Sydney
6. New York - America/New_York
7. Los Angeles - America/Los_Angeles
8. Dubai - Asia/Dubai
9. Singapore - Asia/Singapore
10. Mumbai - Asia/Kolkata
11. Bangkok - Asia/Bangkok
12. Hong Kong - Asia/Hong_Kong
13. São Paulo - America/Sao_Paulo
14. Moscow - Europe/Moscow
15. Cairo - Africa/Cairo

## 💡 Tips & Tricks

- **Scroll** to see all timezones if the window is too small
- **Add multiple instances** of the same timezone with different names
- **Use for business** - Keep track of meeting times across different regions
- **Travel planning** - Add timezones before traveling to adjust to local time

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'tkinter'"
- Install tkinter: `pip install tk` or use your system package manager

### "No module named 'pytz'"
- Run: `pip install -r requirements.txt`

### Times not updating
- Click "🔄 Refresh" button
- Check that the application window is in focus

## 🔄 Update Frequency

- The clock updates automatically every 1 second
- Manual refresh is available via the "🔄 Refresh" button

## 📝 License

MIT License - Feel free to use and modify!

## 👨‍💻 Author

Created with ❤️ for global teams and travelers

---

**Enjoy keeping track of time across the world! 🌎⏰**
