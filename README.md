# lldb.sh

Make your LLDB experience 26% better* with one weird trick: pipe the output of lldb commands to any normal shell command.

```
(lldb) command script import /path/to/lldbsh.py

(lldb) sh image list | wc -c
    3898

(lldb) sh env | grep SDKROOT
  SDKROOT=/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk
```

\* does not improve symbolication speed :(