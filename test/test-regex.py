import re

inp = "<!-- svg-source:excalidraw --> fjdsk \n fds <!-- payload-end -->\n<defs> fsjdf \n fjds </defs> hi\nhi"
  
pattern = re.compile(r"" + re.escape("<defs>(.*)</defs>|\\n"))
pattern = "(?s)<!-- svg-source:excalidraw -->.*<!-- payload-end -->|<defs>.*</defs>|\n"
print(re.escape(pattern))
pattern = re.compile(pattern)
out = re.sub(pattern,'',inp)

print(out)
