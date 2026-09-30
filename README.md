# Foshan WeChat Bingo

A small bingo-card generator made for our Foshan WeChat group.

The idea is simple: our group has recurring chat events and familiar
patterns — the same questions being asked again and again, people
sharing or advertising places, and users repeating their usual routines.
These bingo canvases are just for fun: generate a board, keep it handy,
and strike off a square whenever something familiar happens.

It's a light-hearted way for active group members to enjoy the chat's
recurring "classics." It's all meant in good humor.

## Available versions

The project includes four Windows executables:

| Executable    | Card layout       | Background                      |
| ------------- | ----------------- | ------------------------------- |
| `bingo3.exe`  | 3 × 3             | Default black                   |
| `bingo3c.exe` | 3 × 3             | Random colorful background      |
| `bingo5.exe`  | 5 × 5             | Default black                   |
| `bingo5c.exe` | 5 × 5             | Random colorful background      |

The `c` suffix means **colorful background**. The default black
background is intended to keep the canvas easy to read; the colorful
versions choose a background color at random.

## How to play

1.  Run the executable for the layout and background style you want.
2.  Open the generated bingo canvas image.
3.  Keep the image available while chatting in the group.
4.  Strike out a square whenever the corresponding familiar event
    happens.
5.  Enjoy the bingo — and keep it friendly.

The boards combine random options with permanent options. The exact
squares depend on the options configured in the project.

## Generated images

The generator saves the canvas as a PNG image. The filename includes a
timestamp, so separate runs produce distinct filenames rather than
continually overwriting the same output (unless the project settings are
changed).

## Building from source

The project is written in Python and uses Pillow for image creation. The
build script uses PyInstaller to package `run.py` into a single
executable.

A typical setup requires Python, Pillow, and PyInstaller. From the
project environment, install the dependencies and run the build script:

``` bash
pip install -r requirements.txt
python build.py
```

The build script is configured to create a single-file executable
without a console window and to use `bingo.ico` as its icon when that
file is present. It writes build artifacts to `dist/` and clears the
existing `build/` and `dist/` directories before building.

> Note: The commands above assume the build script is named `build.py`
> and that the project's other modules and settings files are present.
> If your local filenames differ, adjust the command accordingly.

## Project notes

-   Bingo options are drawn from the project's random and permanent
    option lists.
-   Options are shuffled before being placed on the board.
-   Canvas dimensions, card dimensions, spacing, colors, and output
    naming are controlled by the project settings.
-   This project is intended for informal entertainment in the Foshan
    WeChat group.
