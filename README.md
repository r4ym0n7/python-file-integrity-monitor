# Python File Integrity Monitor

A simple Python security automation tool that detects changes to files by comparing SHA-256 hashes against a trusted baseline.
File integrity monitoring is a common security control used to detect unauthorized or unexpected changes to files.

This project creates a baseline of file hashes and compares future scans against that baseline to identify modified, new, or deleted files.

## Features

- Creates a SHA-256 hash baseline
- Detects modified files
- Detects new files
- Detects deleted files
- Uses Python standard libraries only
- Provides simple command-line output
- Demonstrates basic security monitoring and automation

## Technologies

- Python 3
- SHA-256
- JSON
- Linux
- Git
- GitHub

## Requirements

- Python 3
- Linux, macOS, or another operating system supporting Python 3

No external Python packages are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/r4ym0n7/python-file-integrity-monitor.git
