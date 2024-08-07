from textual.app import App, ComposeResult
from textual.widgets import Static


class BouncingApp(App):
    CSS = """
    Static {
        width: 20;
        height: 10;
        background: red;
    }
    """

    dx = 2
    dy = 1

    def compose(self) -> ComposeResult:
        yield Static()

    def on_mount(self) -> None:
        widget = self.query_one(Static)
        widget.offset += (self.dx, self.dy)

        self.set_interval(1 / 10, self.update)

    def update(self) -> None:
        widget = self.query_one(Static)
        if (
            widget.offset.x <= 0
            or widget.offset.x + widget.size.width >= self.size.width
        ):
            self.dx *= -1

        if (
            widget.offset.y <= 0
            or widget.offset.y + widget.size.height >= self.size.height
        ):
            self.dy *= -1

        widget.offset += (self.dx, self.dy)


if __name__ == "__main__":
    app = BouncingApp()
    app.run()
