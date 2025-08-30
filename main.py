from time import monotonic
from textual.app import App
from textual import on
from textual.reactive import reactive

# from textual.events import Callback
from textual.widgets import Header, Footer, Button, Static
# from textual.containers import ScrollableContainer


class TimeDisplay(Static):
    """A widget to display the stopwatch time."""

    time_elapsed = reactive(0)

    def watch_time(self) -> None:
        """Called when the time changes."""
        curr_time = self.time_elapsed
        hours = curr_time // 3600
        minutes = (curr_time % 3600) // 60
        seconds = curr_time % 60
        milliseconds = (curr_time * 100) % 100
        self.time = f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"
        self.update(self.time)
        print(f"Time updated to {self.time}")

    def start(self) -> None:
        """Start the stopwatch."""
        self.time_elapsed = monotonic()

    def stop(self) -> None:
        """Stop the stopwatch."""
        self.time_elapsed = monotonic() - self.time_elapsed


class Stopwatch(Static):
    """A widget to display the stopwatch time."""

    @on(Button.Pressed, "#start_stop")
    def start_stop(self) -> None:
        button = self.query_one("#start_stop", Button)
        if "started" in button.classes:
            button.remove_class("started")
            button.add_class("stopped")
            button.label = "Stop"
            button.variant = "error"
            button.query_one(TimeDisplay).start()
            print(button)
        else:
            button.remove_class("stopped")
            button.add_class("started")
            button.label = "Start"
            button.variant = "success"
            button.query_one(TimeDisplay).stop()

    def compose(self):
        yield Button("Start", variant="success", id="start_stop", classes="started")

        yield Button("Reset", id="reset")

        yield TimeDisplay("00:00:00", id="time_display")


class StopwatchApp(App):
    """A simple stopwatch app to demonstrate Textual basics."""

    BINDINGS = [
        ("s", "start_stop", "Start/Stop"),
        ("r", "reset", "Reset"),
        ("d", "action_toggle_dark_mode", "Toggle Dark Mode"),
        ("q", "quit", "Quit"),
    ]

    CSS_PATH = "assets/styles/stopwatch.css"

    # def __init__(self):
    #     super().__init__()

    def compose(self):
        """Create child widgets for the app."""
        # Use a more standard time format for the clock
        yield Header(name="Hello App", show_clock=True, time_format="%H:%M:%S")
        yield Stopwatch()  # stopwatch display widget
        yield Footer()
        # You will add your main stopwatch display widget here later

    def action_toggle_dark_mode(self) -> None:
        """An action to toggle dark mode.

        This works because the 'dark' property is built into the base App class.
        """

        print("Hello dark ")


def main():
    """The main function to run the app."""
    app = StopwatchApp()
    app.run()


if __name__ == "__main__":
    main()
