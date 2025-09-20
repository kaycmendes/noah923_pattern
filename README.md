# Noah 9:23 Pattern Analysis

A comprehensive Bible analytics tool that analyzes specific chapter and verse patterns across the entire Bible, with special focus on numerical patterns related to the number 7.

## Overview

This project provides interactive Bible verse analytics that allows users to specify any chapter and verse combination and provides comprehensive statistics focused only on those matching passages across the entire Bible.

## Features

- **Interactive Analysis**: Specify any chapter and verse to analyze across all books
- **Comprehensive Statistics**: Detailed analysis of matching passages including:
  - Character and word counts
  - Text complexity analysis
  - Word frequency analysis
  - Book distribution analysis
  - Length distribution with percentiles

- **Number 7 Pattern Analysis**: Special focus on patterns related to the number 7:
  - Explicit seven mentions
  - Numbers divisible by 7
  - Biblical seven terms
  - Ordinal numbers related to seven
  - Mathematical patterns
  - Character/word count analysis
  - Position-based analysis

- **Report Generation**: Saves detailed analysis reports in multiple formats:
  - JSON files with raw data
  - Text summaries
  - Comprehensive analytics

## Files

- `bible.json`: Complete Bible text data in JSON format
- `countverse.py`: Interactive analytics script

## Usage

```bash
python countverse.py [path_to_bible.json]
```

If no path is provided, the script will look for `bible.json` in the default location.

## Example Output

The script provides comprehensive analysis including:
- Basic statistics (character count, word count, etc.)
- Average statistics
- Extreme values (longest/shortest passages)
- Length distribution
- Book analysis
- Word frequency analysis
- Character analysis
- Number 7 pattern analysis
- All matching passages

## Requirements

- Python 3.6+
- Standard library modules: json, sys, pathlib, collections, re, datetime

## Installation

1. Clone this repository
2. Ensure you have Python 3.6+ installed
3. Run the script with your Bible JSON file

## License

This project is open source and available under the MIT License.