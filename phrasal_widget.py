"""Phrasal Verb Widget - always-on-top desktop vocab badge."""
from __future__ import annotations

import json
import random
import sys
import tkinter as tk
from pathlib import Path

WINDOW_W = 260
WINDOW_H = 70
DEFAULT_INTERVAL_SECONDS = 15
BG_COLOR = "#1e1e2e"
EN_COLOR = "#e0e0ff"
TR_COLOR = "#a0a0c0"
CONTROL_COLOR = "#6c7086"
CONTROL_HOVER_COLOR = "#cdd6f4"

CONFIG_DIR = Path.home() / ".phrasal_widget"
CONFIG_FILE = CONFIG_DIR / "config.json"
DATA_FILE = Path(__file__).parent / "phrasal_verbs.json"

# Embedded fallback — used when phrasal_verbs.json is missing or malformed.
EMBEDDED_VERBS: list[dict[str, str]] = [
    {"en": "make up", "tr": "uydurmak; oluşturmak"},
    {"en": "bring about", "tr": "sebep olmak"},
    {"en": "deal with", "tr": "...ile ilgili olmak; başa çıkmak"},
    {"en": "rely on", "tr": "güvenmek; bel bağlamak"},
    {"en": "set up", "tr": "kurmak"},
    {"en": "keep up with", "tr": "ayak uydurmak"},
    {"en": "account for", "tr": "sebebi olmak; oluşturmak"},
    {"en": "come up with", "tr": "bulmak (çözüm yolu vb.)"},
    {"en": "carry out", "tr": "yapmak"},
    {"en": "take up", "tr": "başlamak; almak (zaman, yer)"},
    {"en": "break down", "tr": "parçalamak; bozulmak"},
    {"en": "work out", "tr": "anlamak"},
    {"en": "cope with", "tr": "başa çıkmak"},
    {"en": "cut off", "tr": "kesmek"},
    {"en": "figure out", "tr": "anlamak (düşünüp)"},
    {"en": "depend on", "tr": "bağlı olmak"},
    {"en": "lead to", "tr": "yol açmak"},
    {"en": "call for", "tr": "gerektirmek"},
    {"en": "give off", "tr": "yaymak"},
    {"en": "result in", "tr": "... ile sonuçlanmak"},
    {"en": "end up", "tr": "sonuçlanmak"},
    {"en": "go through", "tr": "göz atmak; geçirmek"},
    {"en": "make up for", "tr": "telafi etmek"},
    {"en": "hand down", "tr": "aktarmak"},
    {"en": "make out", "tr": "güçlükle anlamak"},
    {"en": "get rid of", "tr": "kurtulmak"},
    {"en": "bring up", "tr": "gündeme getirmek; yetiştirmek"},
    {"en": "give up", "tr": "bırakmak"},
    {"en": "put out", "tr": "can sıkmak; söndürmek"},
    {"en": "put up with", "tr": "katlanmak"},
    {"en": "turn out", "tr": "... olduğu ortaya çıkmak"},
    {"en": "draw on", "tr": "yararlanmak"},
    {"en": "break out", "tr": "patlak vermek"},
    {"en": "back up", "tr": "desteklemek"},
    {"en": "end up with", "tr": "... ile sonuçlanmak"},
    {"en": "wipe out", "tr": "yok etmek"},
    {"en": "take over", "tr": "devralmak"},
    {"en": "build up", "tr": "birikmek"},
    {"en": "set out", "tr": "yola çıkmak"},
    {"en": "divide into", "tr": "...ya bölmek"},
    {"en": "take on", "tr": "... hal almak"},
    {"en": "stem from", "tr": "...dan kaynaklanmak"},
    {"en": "try out", "tr": "sınamak"},
    {"en": "rest on", "tr": "...ya bağlı olmak"},
    {"en": "find out", "tr": "keşfetmek"},
    {"en": "draw up", "tr": "düzenlemek"},
    {"en": "come up", "tr": "çıkmak (fırsat, sorun); ele alınmak"},
    {"en": "derive from", "tr": "...dan türemek"},
    {"en": "break away", "tr": "ayrılmak"},
    {"en": "settle down", "tr": "alışmak"},
    {"en": "get over", "tr": "atlatmak"},
    {"en": "look to", "tr": "medet ummak"},
    {"en": "let off", "tr": "bu seferlik affetmek"},
    {"en": "throw away", "tr": "atmak"},
    {"en": "pass down", "tr": "geçmek (nesilden nesle)"},
    {"en": "take part in", "tr": "katılmak"},
    {"en": "auction off", "tr": "açık arttırma ile satmak"},
    {"en": "fit in with", "tr": "uymak"},
    {"en": "do well", "tr": "iyi gitmek"},
    {"en": "watch over", "tr": "göz kulak olmak"},
    {"en": "pass into", "tr": "...ya geçmek"},
    {"en": "centre on", "tr": "bir konuya odaklanmak"},
    {"en": "come down with", "tr": "...dan hasta olmak"},
    {"en": "leave behind", "tr": "arkada bırakmak"},
    {"en": "run into", "tr": "rastlamak"},
    {"en": "refer to", "tr": "ifade etmek"},
    {"en": "adhere to", "tr": "bağlı kalmak"},
    {"en": "fall into", "tr": "bölünmek"},
    {"en": "switch on", "tr": "açmak (elektrikli aleti)"},
    {"en": "bring out", "tr": "öne çıkarmak"},
    {"en": "run out", "tr": "tükenmek"},
    {"en": "lay down", "tr": "yasa çıkarmak"},
    {"en": "pick up", "tr": "öğrenmek"},
    {"en": "substitute for", "tr": "yerini almak"},
    {"en": "put forth", "tr": "ileri sürmek"},
    {"en": "be faced with", "tr": "karşı karşıya kalmak"},
    {"en": "break up", "tr": "sona ermek"},
    {"en": "go down", "tr": "düşmek"},
    {"en": "go on", "tr": "devam etmek"},
    {"en": "pass through", "tr": "içinden geçmek"},
    {"en": "turn to", "tr": "...ya yönelmek"},
    {"en": "rule out", "tr": "ihtimalini ortadan kaldırmak"},
    {"en": "go against", "tr": "karşı çıkmak"},
    {"en": "interfere with", "tr": "burnunu sokmak"},
    {"en": "come under", "tr": "...nın altına girmek"},
    {"en": "strive for", "tr": "çabalamak"},
    {"en": "convert into", "tr": "...ya dönüştürmek"},
    {"en": "set aside", "tr": "bir kenara koymak"},
    {"en": "root out", "tr": "kökünü kazımak"},
    {"en": "expose to", "tr": "maruz bırakmak"},
    {"en": "delve into", "tr": "derinlemesine incelemek"},
    {"en": "conjure up", "tr": "hayal etmek"},
]


def load_verbs(path: Path = DATA_FILE) -> list[dict[str, str]]:
    """Load verb list from JSON, falling back to embedded list on error."""
    try:
        with path.open(encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list) and all(
            isinstance(item, dict) and "en" in item and "tr" in item
            for item in data
        ):
            return data
        print(f"warning: {path} is not a valid verb list; using embedded", file=sys.stderr)
        return EMBEDDED_VERBS
    except (OSError, json.JSONDecodeError) as e:
        print(f"warning: could not load {path} ({e}); using embedded", file=sys.stderr)
        return EMBEDDED_VERBS


class ShuffleCycle:
    """Iterates through items in shuffled order, reshuffling at boundaries.

    Ensures the last item of one pass isn't the first item of the next pass.
    Supports stepping back through the current order via prev().
    """

    def __init__(
        self,
        items: list[dict[str, str]],
        rng: random.Random | None = None,
    ) -> None:
        if not items:
            raise ValueError("ShuffleCycle requires at least one item")
        self._items = items
        self._rng = rng or random.Random()
        self._order: list[dict[str, str]] = []
        self._index = -1  # -1 means "before first next()"
        self._last_emitted: dict[str, str] | None = None
        self._reshuffle()

    def _reshuffle(self) -> None:
        new_order = list(self._items)
        self._rng.shuffle(new_order)
        # Boundary smoothing: if first of new order equals last emitted,
        # swap it with another position (and re-pick if list has >1 item).
        if (
            self._last_emitted is not None
            and len(new_order) > 1
            and new_order[0] == self._last_emitted
        ):
            # Swap index 0 with a random other index
            swap_with = self._rng.randint(1, len(new_order) - 1)
            new_order[0], new_order[swap_with] = new_order[swap_with], new_order[0]
        self._order = new_order
        self._index = -1

    def next(self) -> dict[str, str]:
        self._index += 1
        if self._index >= len(self._order):
            self._reshuffle()
            self._index = 0
        item = self._order[self._index]
        self._last_emitted = item
        return item

    def prev(self) -> dict[str, str]:
        if self._index <= 0:
            # At or before start — return current item without moving
            return self._order[0] if self._index < 0 else self._order[self._index]
        self._index -= 1
        item = self._order[self._index]
        self._last_emitted = item
        return item


DEFAULT_CONFIG: dict = {
    "x": -1,  # -1 sentinel → use default top-right placement
    "y": -1,
    "interval_seconds": DEFAULT_INTERVAL_SECONDS,
    "paused": False,
}


def load_config(path: Path = CONFIG_FILE) -> dict:
    """Load config JSON, returning defaults for missing/malformed."""
    try:
        with path.open(encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            return dict(DEFAULT_CONFIG)
        # Merge with defaults so missing keys are filled in
        merged = dict(DEFAULT_CONFIG)
        merged.update(data)
        return merged
    except (OSError, json.JSONDecodeError):
        return dict(DEFAULT_CONFIG)


def save_config(path: Path, cfg: dict) -> None:
    """Write config JSON, creating parent dirs as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)


POSITION_TOLERANCE = 20


def is_position_visible(
    x: int, y: int, w: int, h: int, screen_w: int, screen_h: int
) -> bool:
    """Return True if the window at (x, y) is within `screen` with tolerance."""
    return (
        x >= -POSITION_TOLERANCE
        and y >= -POSITION_TOLERANCE
        and x + w <= screen_w + POSITION_TOLERANCE
        and y + h <= screen_h + POSITION_TOLERANCE
    )


class PhrasalWidget:
    def __init__(self, root: tk.Tk, verbs: list[dict[str, str]], config: dict) -> None:
        self.root = root
        self.config = config
        self.cycle = ShuffleCycle(verbs)
        self.paused: bool = bool(config.get("paused", False))
        self._after_id: str | None = None
        self._drag_offset: tuple[int, int] | None = None

        self._setup_window()
        self._build_ui()
        self._show(self.cycle.next())
        if not self.paused:
            self._schedule_next()

    def _setup_window(self) -> None:
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg=BG_COLOR)

        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = self.config.get("x", -1)
        y = self.config.get("y", -1)
        if x < 0 or y < 0 or not is_position_visible(
            x, y, WINDOW_W, WINDOW_H, screen_w, screen_h
        ):
            x = screen_w - WINDOW_W - 20
            y = 40
        self.root.geometry(f"{WINDOW_W}x{WINDOW_H}+{x}+{y}")

    def _build_ui(self) -> None:
        self.en_label = tk.Label(
            self.root,
            text="",
            font=("Segoe UI", 12, "bold"),
            fg=EN_COLOR,
            bg=BG_COLOR,
            anchor="w",
            padx=10,
        )
        self.en_label.place(x=0, y=4, width=WINDOW_W, height=24)

        self.tr_label = tk.Label(
            self.root,
            text="",
            font=("Segoe UI", 10),
            fg=TR_COLOR,
            bg=BG_COLOR,
            anchor="w",
            padx=10,
            wraplength=WINDOW_W - 12,
            justify="left",
        )
        self.tr_label.place(x=0, y=28, width=WINDOW_W, height=38)

        # Hover controls — hidden by default, shown on mouse-enter
        self.controls = tk.Frame(self.root, bg=BG_COLOR)
        self.btn_prev = tk.Label(
            self.controls, text="◀", fg=CONTROL_COLOR, bg=BG_COLOR,
            font=("Segoe UI", 9), cursor="hand2", padx=4,
        )
        self.btn_pause = tk.Label(
            self.controls, text="⏸", fg=CONTROL_COLOR, bg=BG_COLOR,
            font=("Segoe UI", 9), cursor="hand2", padx=4,
        )
        self.btn_next = tk.Label(
            self.controls, text="▶", fg=CONTROL_COLOR, bg=BG_COLOR,
            font=("Segoe UI", 9), cursor="hand2", padx=4,
        )
        self.btn_close = tk.Label(
            self.controls, text="✕", fg=CONTROL_COLOR, bg=BG_COLOR,
            font=("Segoe UI", 9), cursor="hand2", padx=4,
        )
        for i, btn in enumerate((self.btn_prev, self.btn_pause, self.btn_next)):
            btn.grid(row=0, column=i, padx=1)
        self.btn_close.grid(row=0, column=4, padx=(8, 2))
        # Place at bottom-right; hidden initially
        self.controls.place_forget()

        self.btn_prev.bind("<Button-1>", lambda _e: self._manual_prev())
        self.btn_pause.bind("<Button-1>", lambda _e: self._toggle_pause())
        self.btn_next.bind("<Button-1>", lambda _e: self._manual_next())
        self.btn_close.bind("<Button-1>", lambda _e: self._close())

        # Hover highlight per button
        for btn in (self.btn_prev, self.btn_pause, self.btn_next, self.btn_close):
            btn.bind("<Enter>", lambda _e, b=btn: b.config(fg=CONTROL_HOVER_COLOR))
            btn.bind("<Leave>", lambda _e, b=btn: b.config(fg=CONTROL_COLOR))

        # Show/hide controls on window-level enter/leave
        self.root.bind("<Enter>", self._on_window_enter, add="+")
        self.root.bind("<Leave>", self._on_window_leave, add="+")

        # Drag bindings on labels and root
        for widget in (self.root, self.en_label, self.tr_label):
            widget.bind("<ButtonPress-1>", self._on_drag_start)
            widget.bind("<B1-Motion>", self._on_drag_motion)
            widget.bind("<ButtonRelease-1>", self._on_drag_end)

        # Keyboard
        self.root.bind("<space>", lambda _e: self._toggle_pause())
        self.root.bind("<Left>", lambda _e: self._manual_prev())
        self.root.bind("<Right>", lambda _e: self._manual_next())
        self.root.bind("<Escape>", lambda _e: self._close())
        self.root.focus_force()

    def _show(self, verb: dict[str, str]) -> None:
        self.en_label.config(text=verb["en"])
        self.tr_label.config(text=verb["tr"])

    def _schedule_next(self) -> None:
        interval_ms = int(self.config.get("interval_seconds", DEFAULT_INTERVAL_SECONDS)) * 1000
        self._after_id = self.root.after(interval_ms, self._auto_advance)

    def _cancel_scheduled(self) -> None:
        if self._after_id is not None:
            self.root.after_cancel(self._after_id)
            self._after_id = None

    def _auto_advance(self) -> None:
        self._show(self.cycle.next())
        self._schedule_next()

    def _manual_next(self) -> None:
        self._show(self.cycle.next())
        # Manual nav does NOT reset the timer cadence

    def _manual_prev(self) -> None:
        self._show(self.cycle.prev())

    def _toggle_pause(self) -> None:
        self.paused = not self.paused
        if self.paused:
            self._cancel_scheduled()
            self.btn_pause.config(text="▶")
        else:
            self._schedule_next()
            self.btn_pause.config(text="⏸")
        self.config["paused"] = self.paused

    def _on_drag_start(self, event: tk.Event) -> None:
        self._drag_offset = (event.x_root - self.root.winfo_x(), event.y_root - self.root.winfo_y())

    def _on_drag_motion(self, event: tk.Event) -> None:
        if self._drag_offset is None:
            return
        new_x = event.x_root - self._drag_offset[0]
        new_y = event.y_root - self._drag_offset[1]
        self.root.geometry(f"+{new_x}+{new_y}")

    def _on_drag_end(self, _event: tk.Event) -> None:
        self._drag_offset = None
        self.config["x"] = self.root.winfo_x()
        self.config["y"] = self.root.winfo_y()
        save_config(CONFIG_FILE, self.config)

    def _close(self) -> None:
        self.config["x"] = self.root.winfo_x()
        self.config["y"] = self.root.winfo_y()
        save_config(CONFIG_FILE, self.config)
        self._cancel_scheduled()
        self.root.destroy()

    def _on_window_enter(self, _event: tk.Event) -> None:
        self.controls.place(relx=1.0, rely=1.0, anchor="se", x=-4, y=-2)

    def _on_window_leave(self, event: tk.Event) -> None:
        # Tkinter fires <Leave> on child enter; check pointer is really outside.
        x = self.root.winfo_pointerx() - self.root.winfo_rootx()
        y = self.root.winfo_pointery() - self.root.winfo_rooty()
        if 0 <= x < WINDOW_W and 0 <= y < WINDOW_H:
            return
        self.controls.place_forget()


if __name__ == "__main__":
    verbs = load_verbs()
    if not verbs:
        verbs = [{"en": "(no data)", "tr": "(veri yok)"}]
    cfg = load_config()
    root = tk.Tk()
    app = PhrasalWidget(root, verbs, cfg)
    root.mainloop()
