# SplitFile-Python

A small Python script that splits a media file (video/audio) into two pieces, using [ffmpeg-python](https://github.com/kkroening/ffmpeg-python).

## Requirements

- Python 3.8+
- [`ffmpeg-python`](https://pypi.org/project/ffmpeg-python/) library
- **FFmpeg** program installed and added to `PATH`
- [Download Windows builds](https://www.gyan.dev/ffmpeg/builds/)
- After installation, verify by running in Command Prompt:
  ```sh
  ffmpeg -version
  ```

## Installation

Clone or download the project, then install the dependency:

```sh
pip install ffmpeg-python
```

Make sure you also have `ffmpeg` installed (not just the Python wrapper).

## Usage

Running the script:

```sh
python SplitFile-Python.py <inputfile> <starttime> <endtime> <outputfile1> <outputfile2>
```

### Arguments:

- `inputfile` → source file (ex: `video.mp4`)
- `starttime` → start time of the first piece (in seconds)
- `endtime` → end time of the first piece (in seconds) and start of the second
- `outputfile1` → file for the first piece
- `outputfile2` → file for the second piece

### Example:

```sh
python SplitFile-Python.py video.mp4 5 10 part1.mp4 part2.mp4
```

- `part1.mp4` → contains the part between seconds 5 and 10
- `part2.mp4` → contains the rest, from second 10 to the end

## Notes

- The script works on any media file supported by FFmpeg.
- The time (`starttime`, `endtime`) is given in seconds (you can also use decimal values, e.g. `5.5`).
- If you get the error `[WinError 2]`, it means that `ffmpeg.exe` is not in PATH`.

---

## Authon Name:

[Raul Dumitrele](https://github.com/Raul-Dumitrele)
