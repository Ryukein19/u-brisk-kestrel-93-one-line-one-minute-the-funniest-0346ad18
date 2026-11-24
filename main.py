import os
# One-liner entry (139 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "I finished the work on time, but then I spent six hours double-checking it, because I was afraid you would notice I had nothing else to do."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
