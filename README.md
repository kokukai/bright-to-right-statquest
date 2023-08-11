# Bright-to-Right-StatQuest

## Overview
Bright-to-Right is a project designed to address an issue with StatQuest videos: excessively bright backgrounds. By inverting the colors, this tool enhances the viewing experience, allowing for more comfortable learning.

![Flowchart](https://showme.redstarplugin.com/d/MGQLkO4a)

## Usage
To explore the functionality of this project, clone the repository and follow the instructions detailed in `main.ipynb`.

## Technologies Utilized
- **Selenium**: Web scraping to obtain relevant YouTube titles.
- **yt-dlp & youtube-search-python**: Downloading video files.
- **moviepy**: Color inversion processing for the videos.

## Functionality
- **Scraper.py**: Extracts specific StatQuest titles using Selenium.
- **Downloader.py**: Downloads the corresponding videos.
- **Inverter.py**: Inverts the colors to reduce brightness.
- **main.ipynb**: An interactive notebook detailing the entire process.

## Motivation
The project was conceived due to personal discomfort with the brightness levels in StatQuest videos. It serves as a practical demonstration of using various tools and libraries to solve a real-world problem.
