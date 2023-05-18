import sys

from .views import MainWindow, App

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    app = App(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    sys.exit(main())