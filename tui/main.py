from textual.app import App, ComposeResult
from textual import events
from textual.widgets import Footer, Header, Static


class PyTeleTui(App):
    CSS_PATH = "dock_layout1_sidebar.tcss"
    COLORS = [
        "white",
        "maroon",
        "red",
        "purple",
        "fuchsia",
        "olive",
        "yellow",
        "navy",
        "teal",
        "aqua",
    ]
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:

        """Create child widgets for the app."""
        # yield Header()
        # yield Footer()
        yield Static("Sidebar", id="sidebar")


    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def on_mount(self) -> None:
        pass

    def on_key(self, event: events.Key) -> None:
        pass


if __name__ == "__main__":
    app = PyTeleTui()
    app.run()
