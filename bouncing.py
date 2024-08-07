from itertools import cycle

from textual.app import App, ComposeResult
from textual.widgets import Static

WIDGET_COLORS = [
    "cyan",
    "orange",
    "blue",
    "yellow",
    "red",
    "violet",
    "green",
    "fuchsia",
]


class BouncingApp(App):
    CSS = """
    Static {
        width: 20;
        height: 10;
    }
    """

    dx = 2
    dy = 1

    colors_cycle = cycle(WIDGET_COLORS)

    def compose(self) -> ComposeResult:
        yield Static()

    def on_mount(self) -> None:
        widget = self.query_one(Static)
        widget.styles.background = next(self.colors_cycle)
        widget.offset += (self.dx, self.dy)

        self.set_interval(1 / 10, self.update)

    def update(self) -> None:
        widget = self.query_one(Static)
        if (
            widget.offset.x <= 0
            or widget.offset.x + widget.size.width >= self.size.width
        ):
            self.dx *= -1
            widget.styles.background = next(self.colors_cycle)

        if (
            widget.offset.y <= 0
            or widget.offset.y + widget.size.height >= self.size.height
        ):
            self.dy *= -1
            widget.styles.background = next(self.colors_cycle)

        widget.offset += (self.dx, self.dy)


if __name__ == "__main__":
    app = BouncingApp()
    app.run()
