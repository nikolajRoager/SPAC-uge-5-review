The given installation instructions did not work.

Firstly, running pipenv install is not valid, there is no such command.

Instead run python -m pipenv install (optionally run pip install pipenv first, it is also required to upgrade to python 3.12 manually first)

The given virtual environment also doesn't include enough packages, we are missing numpy, required by pandas.

After manually installing.

The virtual environment need to be completely cleaned, and we need to test this on a freshly installed VM.

The programs runs fine, but eventually halts (or it is unclear if it is still waiting, or just taking a very long time)

To debug this, I have created a list of ongoing processes, after several hours, it is stuck on this:

Evidently, the program is stuck waiting for responses which never come. The program does not have any sort of time-out.

Conclusion: The program does not function. 

After some looking through the files, I found DownloadTimeout in config.py, it was set to 0, I do not know for certain what that means, though I assume it actually means infinite timeout. I set it to 60, expecting that to be 60 seconds.


The config file includes a FileLimit, but it is not in use, I modified this by including it


Tests