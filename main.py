"""
Top-level module to expose functions for tests.

This file exists so tests that import `main` (from project root)
can find the `bfs_shortest_path` implementation located in `hw01/main.py`.
"""

from hw01.main import bfs_shortest_path

__all__ = ["bfs_shortest_path"]
