# yiddish-reader
## A set of ConTeXt environments and fonts for Yiddish anthology publishing, with sample texts

### To compile on Linux:
- Install [ConTeXt Standalone](https://www.contextgarden.net/ConTeXt_Standalone)

- Copy the files in `./context-hack` into `context_dir/tex/texmf-context/tex/context/base/mkiv`

- (optional) Create a shell script to set up the environment and compile. For example:

```
#/bin/bash

source context_dir/tex/setuptex
context mayses.tex --jobname=mayses-letter --result=mayses-letter  --purge
context mayses.tex --mode=book --purge
```

Remember to replace `context_dir` with the directory where you installed ConTeXt Standalone.

Thanks to Hans Hagen and Wolfgang Schuster for the quick right-to-left fix. Hopefully it will soon be part of the standard distribution and all this setup won't be necessary.

### Fonts
Fonts are included from [Aharon Varady](https://github.com/aharonium/fonts)'s repository for ease and convenience. Thanks to Aharon, [Culmus Project](http://culmus.sourceforge.net/), and [Michal Sahar](https://github.com/MichalSahar) for the fonts.

### The Texts
Special thanks to [Raphael Finkel](http://www.cs.uky.edu/~raphael/) for making OCR'd texts in Yiddish available before anyone else on the Internet!
