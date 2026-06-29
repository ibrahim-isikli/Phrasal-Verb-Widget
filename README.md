# Phrasal Verb Widget

A tiny always-on-top desktop widget that cycles through English phrasal verbs with Turkish meanings. Sits in the corner of your screen while you work.

## Running

```
pythonw phrasal_widget.py
```

`pythonw` (with the `w`) runs without a console window on Windows. For debugging, use `python phrasal_widget.py` instead — `print(...)` warnings show up in the terminal.

Requires Python 3.12+. No pip packages needed (uses stdlib `tkinter` only).


<img width="268" height="82" alt="image" src="https://github.com/user-attachments/assets/06afde8a-6994-4547-8e10-9a67606ff6de" />


<img width="274" height="84" alt="image" src="https://github.com/user-attachments/assets/07372513-bd0a-4c44-ba57-c323bf77a33d" />


<img width="269" height="85" alt="image" src="https://github.com/user-attachments/assets/495374db-f9f6-4ef1-9a78-50464b54c8d3" />


## Controls

| Action | How |
|---|---|
| Move window | Drag with mouse anywhere on the body |
| Next verb | `→` or click `▶` (hover to reveal) |
| Previous verb | `←` or click `◀` |
| Pause/resume auto-advance | `Space` or click `⏸` / `▶` |
| Close | `Esc` or click `✕` |

Window position is remembered across launches.

## Editing the verb list

Edit `phrasal_verbs.json` — the format is a JSON array of `{"en": "...", "tr": "..."}` objects. Changes load on next launch.

If `phrasal_verbs.json` is missing or invalid, the app falls back to a built-in copy of the list.

## Changing the interval

Edit `~/.phrasal_widget/config.json` and set `"interval_seconds"` to whatever you like (in seconds). Restart the app.

## Start on Windows boot (optional)

1. Press `Win + R`, type `shell:startup`, press Enter.
2. Create a new shortcut in the folder that opens. Target:
   ```
   pythonw.exe "C:\full\path\to\phrasal_widget.py"
   ```
3. Save. The widget will launch every time you log in.
<img width="551" height="600" alt="image" src="https://github.com/user-attachments/assets/0f8be085-0ceb-414d-ba20-c60e0504bd23" />

## Example View
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/dd7c1bb7-1cda-4377-b835-ea2235cf4293" />


