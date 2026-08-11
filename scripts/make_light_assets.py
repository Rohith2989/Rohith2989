#!/usr/bin/env python3
"""Generate light-theme SVG variants from the dark ones via palette swap."""
import pathlib

ASSETS = pathlib.Path(__file__).resolve().parent.parent / "assets"

PALETTE = {
    "#0d1117": "#ffffff",  # window bg
    "#161b22": "#f6f8fa",  # titlebar bg
    "#30363d": "#d0d7de",  # borders
    "#e6edf3": "#1f2328",  # foreground
    "#7d8590": "#656d76",  # dim
    "#3fb950": "#1a7f37",  # green
    "#4dd0ff": "#0969da",  # cyan/accent
    "#bc8cff": "#8250df",  # purple
    "#e3b341": "#9a6700",  # yellow
    "#ffa657": "#bc4c00",  # orange
}


def to_light(svg: str) -> str:
    for dark, light in PALETTE.items():
        svg = svg.replace(dark, light)
    return svg


for name in ["agent-trace", "chip-linkedin", "chip-mail", "chip-leetcode", "chip-codeforces"]:
    dark_path = ASSETS / f"{name}-dark.svg"
    if dark_path.exists():
        light_path = ASSETS / f"{name}-light.svg"
        light_path.write_text(to_light(dark_path.read_text()))
        print(f"wrote {light_path.name}")
