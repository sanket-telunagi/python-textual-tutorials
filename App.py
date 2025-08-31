from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual.containers import VerticalScroll
from assets.mywidgets.stopwatch import Stopwatch


class StopwatchApp(App):
    """A Textual app to manage stopwatches."""

    CSS_PATH = "assets/styles/stopwatch.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("a", "add_stopwatch", "Add Stopwatch"),
        ("r", "remove_stopwatch", "Remove Stopwatch"),
    ]

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Header()
        yield Footer()
        yield VerticalScroll(Stopwatch(), Stopwatch(), Stopwatch())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def action_add_stopwatch(self) -> None:
        """An action to add a new stopwatch."""
        scroll = self.query_one(VerticalScroll)
        scroll.mount(Stopwatch())

    def action_remove_stopwatch(self) -> None:
        """An action to remove the last stopwatch."""
        scroll = self.query_one(VerticalScroll)
        stopwatches = scroll.query(Stopwatch)
        if stopwatches:
            stopwatches.last().remove()
