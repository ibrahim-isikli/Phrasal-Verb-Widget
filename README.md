# Phrasal Verb Widget

A tiny always-on-top desktop widget that cycles through English phrasal verbs with Turkish meanings. Sits in the corner of your screen while you work.

## Running

```
pythonw phrasal_widget.py
```

`pythonw` (with the `w`) runs without a console window on Windows. For debugging, use `python phrasal_widget.py` instead — `print(...)` warnings show up in the terminal.

Requires Python 3.12+. No pip packages needed (uses stdlib `tkinter` only).

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
